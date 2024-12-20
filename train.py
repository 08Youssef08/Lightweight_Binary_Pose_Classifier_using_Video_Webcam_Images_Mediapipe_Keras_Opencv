import os
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import resample
from tensorflow import keras
from tensorflow.keras import layers
import pickle
from utils.prerocess import remove_outliers, balance_data, standardize_features

# Argument parser
parser = argparse.ArgumentParser(description="Train and evaluate a deep learning model on a dataset.")
parser.add_argument('--data_path', type=str, required=True, help="Path to the dataset (CSV file).")
parser.add_argument('--output_model', type=str, required=True, help="Path to save the trained model.")
parser.add_argument('--epochs', type=int, default=100, help="Number of epochs for training the model.")
parser.add_argument('--batch_size', type=int, default=32, help="Batch size for training the model.")
parser.add_argument('--test_size', type=float, default=0.3, help="Proportion of data to be used for testing.")
parser.add_argument('--state_column', type=str, default='state', help="Name of the target column in the dataset.")
parser.add_argument('--threshold', type=float, default=3.0, help="Z-score threshold for outlier removal.")

# Parse the arguments
args = parser.parse_args()

# Assign values from parsed arguments to variables
data_path = args.data_path
output_model = args.output_model
epochs = args.epochs
batch_size = args.batch_size
test_size = args.test_size
state_column = args.state_column
threshold = args.threshold

# Load the dataset
df = pd.read_csv(data_path)
X = df.drop(state_column, axis=1)  # Features
y = df[state_column]  # Target value

# Encode categorical labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Remove outliers
X_no_outliers = remove_outliers(X, threshold=threshold)
y_no_outliers = y_encoded[(X_no_outliers.index)]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_no_outliers, y_no_outliers, test_size=test_size, random_state=443, shuffle=True)

# Balance the data using oversampling
X_resampled, y_resampled = balance_data(X_train, y_train)

# Standardize the features
X_train_scaled, X_test_scaled = standardize_features(X_resampled, X_test)

# Build a deep learning model
model = keras.Sequential([
    layers.InputLayer(input_shape=(X_train_scaled.shape[1],)),  # Input layer
    layers.Dense(64, activation='relu'),  # Hidden layer 1
    layers.Dense(32, activation='relu'),  # Hidden layer 2
    layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_resampled, epochs=epochs, batch_size=batch_size, validation_data=(X_test_scaled, y_test))

# Evaluate the model on the test data
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test accuracy: {accuracy:.4f}")

# Save the trained model
with open(output_model, 'wb') as f:
    pickle.dump(model, f)
    print(f"Model saved to {output_model}")
