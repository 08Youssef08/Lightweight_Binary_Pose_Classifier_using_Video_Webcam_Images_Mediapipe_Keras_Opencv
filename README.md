
# **Lightweight Binary Pose Classifier Using Video, Webcam, Images, Mediapipe, Keras, and OpenCV**

## **Overview**
The **Lightweight Binary Pose Classifier** is a framework designed to classify states like "Awake" or "Asleep" based on body pose data collected from videos, webcam feeds, or images. It leverages **MediaPipe**, **OpenCV**, and **Keras** to extract and analyze pose landmarks, train models, and perform real-time monitoring.  

### **Current Application**  
This project is currently specifically used for **baby awakeness monitoring**, offering insights into whether a baby is awake or asleep through non-invasive observation.  

> **Note:**  
This project is part of a **larger ongoing initiative** and is still under **development and testing**. While it remains a work in progress, the current version is **functional and useful** for experimenting and preliminary applications.

---

## **Features**
1. **State Monitoring:**
   - Detect and classify states using **live webcam feeds**, **video files**, or **static images**.
   - Outputs predictions based on pre-trained models.

2. **Data Collection:**
   - Extract pose landmarks from media sources and store them in CSV format for further analysis.
   - Works seamlessly with video files, live cameras, and images.

3. **Preprocessing Pipeline:**
   - Removes outliers, balances datasets, and standardizes features for effective training.
   - Supports customized preprocessing for various datasets.

4. **Deep Learning Model:**
   - Train lightweight binary classifiers using **Keras**.
   - Evaluate models with clear metrics like **accuracy** for classification performance.

5. **Modular Design:**
   - Components for **landmark extraction**, **data preprocessing**, **model training**, and **real-time inference** will easily be used independently or together.

---

## **Dependencies**
This project is built on **Python 3.8.18** 
Install dependencies using:
```bash
conda create -n StateEnv python=3.8.18
conda activate StateEnv
pip install -r requirements.txt
```

---

## **How to Use**

### **1. Data Collection**
Collect pose landmarks from a camera, video, or images.  
Run:
```bash
python collect_data.py --source [camera/video/image] --data_path [path/to/media] --state [Asleep/Awake] --output_csv [path/to/output.csv]
```

### **2. Train the Model**
Train a deep learning model using preprocessed data.  
Run:
```bash
python train.py --data_path [path/to/dataset.csv] --output_model [path/to/save/model.pkl] --epochs 100 --batch_size 32 --test_size 0.3 --state_column state
```

### **3. Monitor in Real-Time**
Use the trained model to classify states from media sources in real time.  
Run:
```bash
python monitor.py --source [camera/video/image] --data_path [path/to/media] --model_path [path/to/model.pkl]
```

---

## **Directory Structure**
```
Lightweight_Binary_Pose_Classifier/
├── utils/
│   ├── collectors.py           # For data collection
│   ├── monitore_utils.py       # For real-time monitoring
│   ├── preprocess.py           # Preprocessing functions
├── collect_data.py                  # Script for keypoint extraction, labeling and saving the csv
├── train.py              # Script for model training
├── monitor.py                  # Script for real-time monitoring
└── README.md                   # Project documentation
```

---

## **Future Improvements**
- Enhanced preprocessing of keypoint data
- Model optimization.
- Advanced visualization of landmarks and classification results.
-Integration with **IoT devices** and **mobile platforms** for enhanced portability.

---

## **Acknowledgments**
This project uses cutting-edge technologies like **MediaPipe**, **OpenCV**, and **Keras** to enable lightweight and effective body pose classification. It is an evolving solution aimed at improving **baby monitoring systems** and related applications.
