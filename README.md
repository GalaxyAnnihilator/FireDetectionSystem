# Fire Detection System

[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Pytorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)](https://ultralytics.com/)

Real-time detection of fire via household cameras

---

## 📂 Repository Hierarchy  

```bash
FireDetectionSystem/  
├── data/  
│   ├── raw/                 # Raw images/videos from cameras  
│   ├── processed/           # Labeled datasets (YOLO format)  
│   └── augmented/           # Augmented data (rotated, noised, etc.)  
│  
├── docs/  
│   ├── presentations/       # Demo slides and project updates  
│   └── reports/             # EDA, test results, and final report  
│  
├── models/                  # YOLOv8 weights (e.g., best.pt)  
│  
├── src/  
│   ├── data_processing.ipynb # Scripts for data augmentation   
│   │  
│   ├── train_model.ipynb    # YOLOv8 training & validation  
│   │  
│   ├── EDA.ipynb            # Exploratory Data Analysis  
│   │  
│   └── iot/                 # Telegram alert integration  
│       ├── telegram_api.py  
│       └── alarm_system.py  
│       
│  
├── tests/                   # Unit & integration tests  
│   ├── unit/  
│   └── integration/  
│  
├── deployment/              # Deployment with Flask API
│   ├── predict.py              
│   └── app.py 
│
├── .gitignore  
├── requirements.txt         # Python dependencies  
├── Dockerfile  
├── LICENSE  
└── README.md                # This file  
```

---

## 🛠️ Key Directories  

### 1. **`data/`**  
- **Purpose**: Stores all datasets (raw, labeled, augmented).  
- **Usage**:  
  - `raw/`: Unprocessed images/videos from cameras.  
  - `processed/`: Roboflow-annotated YOLO datasets.  
  - `augmented/`: Enhanced data for model robustness.  

### 2. **`src/`**  
- **Purpose**: Contains all source code modularized by functionality.  
- **Submodules**:  
  - `data_processing.ipynb`: Data preprocessing & augmentation.  
  - `train_model.ipynb`: YOLOv8 training, hyperparameter tuning, and evaluation.  
  - `iot/`: Telegram alerts integration.  

### 3. **`models/`**  
- **Purpose**: Hosts trained model checkpoints and edge-optimized versions.  
- **Files**:  
  - `best.pt`: Best-performing YOLOv8 weights.   

### 4. **`deployment/`**  
- **Purpose**: Deployment scripts and Docker configurations.  
- **Usage**:  
  - `app.py`: Create the Flask API to connect.  
  - `predict.py`: Load the best model to predict  

### 5. **`docs/`**  
- **Purpose**: Documentaion and Report 
- **Files**:  
  - `presentation/`: Slides for presentation (Google Slides format).  
  - `reports/`: Reports to show final result, what we have done throughout the project. 

---

## 🚀 Getting Started  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/GalaxyAnnihilator/FireDetectionSystem
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the model**:  
   ```bash
   python deployment/app.py
   ```
---

## 📜 License  
MIT License. See [LICENSE](LICENSE) for details.  
```