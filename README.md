# Customer Churn Prediction using Artificial Neural Network (ANN) - ([App_Link](https://churnpredictionusingann.streamlit.app/))

A machine learning project that predicts customer churn using an Artificial Neural Network (ANN) built with TensorFlow/Keras. The project includes data preprocessing, model training, evaluation, and a Streamlit web application for real-time predictions.

## 📊 Project Overview

This project analyzes customer data to predict whether a customer is likely to churn (leave the service). The model uses various customer features such as credit score, geography, gender, age, tenure, balance, and other banking-related information to make predictions.

## 🎯 Objectives

- Build an accurate customer churn prediction model using deep learning
- Create a user-friendly web interface for making predictions
- Provide insights into customer behavior patterns
- Enable proactive customer retention strategies

## 📁 Project Structure

```
├── app.py                      # Streamlit web application
├── experiments.ipynb           # Model development and training notebook
├── prediction.ipynb           # Prediction examples and testing
├── Churn_Modelling.csv        # Dataset
├── model.h5                   # Trained ANN model
├── scaler.pkl                 # StandardScaler for feature scaling
├── label_encoder_gender.pkl   # LabelEncoder for gender encoding
├── onehot_encoder_geo.pkl     # OneHotEncoder for geography encoding
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── logs/                      # TensorBoard logs
    └── fit/
        └── 20251001-195317/   # Training logs with timestamps
```

## 🔧 Features

### Model Features
- **Credit Score**: Customer's credit score (350-850)
- **Geography**: Customer's location (France, Germany, Spain)
- **Gender**: Customer's gender (Male/Female)
- **Age**: Customer's age (18-92)
- **Tenure**: Number of years as a customer (0-10)
- **Balance**: Account balance
- **Number of Products**: Number of bank products used (1-4)
- **Has Credit Card**: Whether customer has a credit card (0/1)
- **Is Active Member**: Whether customer is active (0/1)
- **Estimated Salary**: Customer's estimated salary

### Target Variable
- **Exited**: Whether the customer churned (1) or not (0)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "ANN Classification Project"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "import tensorflow; print(tensorflow.__version__)"
   ```

## 🖥️ Usage

### Running the Streamlit Web Application

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Input customer data** using the interactive interface:
   - Select geography from dropdown
   - Choose gender
   - Adjust sliders for age, credit score, tenure, and number of products
   - Enter balance and estimated salary
   - Select credit card and active member status

4. **Get predictions** with probability scores and churn likelihood

### Using Jupyter Notebooks

1. **Model Development:**
   ```bash
   jupyter notebook experiments.ipynb
   ```

2. **Making Predictions:**
   ```bash
   jupyter notebook prediction.ipynb
   ```

## 🧠 Model Architecture

The ANN model includes:
- **Input Layer**: 11 features after preprocessing
- **Hidden Layers**: Multiple dense layers with ReLU activation
- **Output Layer**: Single neuron with sigmoid activation for binary classification
- **Optimization**: Adam optimizer
- **Loss Function**: Binary crossentropy
- **Callbacks**: Early stopping and TensorBoard logging

## 📈 Model Performance

The model training includes:
- **Train/Test Split**: Data split for training and validation
- **Feature Scaling**: StandardScaler for numerical features
- **Encoding**: 
  - LabelEncoder for gender
  - OneHotEncoder for geography
- **Monitoring**: TensorBoard logs for training visualization
- **Early Stopping**: Prevents overfitting

## 🔍 Data Preprocessing

1. **Data Cleaning**: Remove unnecessary columns (RowNumber, CustomerId, Surname)
2. **Encoding**: 
   - Gender: Label encoding (Male/Female → 0/1)
   - Geography: One-hot encoding (France, Germany, Spain)
3. **Scaling**: StandardScaler for numerical features
4. **Train/Test Split**: Separate data for training and evaluation

## 📊 Monitoring and Visualization

- **TensorBoard**: Training metrics and loss visualization
- **Model Checkpoints**: Save best performing models
- **Prediction Confidence**: Probability scores for churn likelihood

## 🛠️ Technical Stack

- **Framework**: TensorFlow/Keras
- **Web App**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Preprocessing**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Monitoring**: TensorBoard

## 📦 Dependencies

```
tensorflow==2.17.0
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
tensorboard
ipykernel
```

## 📄 Files Description

- **`app.py`**: Main Streamlit application with user interface
- **`experiments.ipynb`**: Complete model development workflow
- **`prediction.ipynb`**: Examples of making predictions with trained model
- **`Churn_Modelling.csv`**: Original dataset with customer information
- **`model.h5`**: Trained neural network model
- **Pickle files**: Saved preprocessing objects (scalers, encoders)


## 👤 Author

**Vineet Patel**
- Email: vineetpatel468@gmail.com
- GitHub: [@vineet416](https://github.com/vineet416)
- LinkedIn: [@vineet416](https://www.linkedin.com/in/vineet416/)


---

⭐ If you found this project helpful, please give it a star!