# Bitcoin Price Predictor

A machine learning project that predicts the **next-day Bitcoin price movement (UP/DOWN)** using historical cryptocurrency market data and a **Random Forest Classifier**.

## 📌 Project Overview

This project uses historical Bitcoin market data to identify patterns and predict whether the next day's price movement is likely to be **UP (1)** or **DOWN (0)**.

The project includes data preprocessing, feature engineering, model training, evaluation, and a prediction interface.

## 🚀 Features

* Historical Bitcoin data analysis
* Data preprocessing and feature engineering
* Random Forest classification
* Next-day price movement prediction
* Model evaluation using accuracy and confusion matrix
* Saved trained model using Joblib
* Flask-based prediction interface

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Joblib**
* **Flask**
* **HTML/CSS**

## 🤖 Machine Learning Approach

### Algorithm

**Random Forest Classifier**

The model is trained using historical Bitcoin market features to classify the next-day movement:

* `1` → UP
* `0` → DOWN

### Feature Engineering

The project derives useful features from the historical data, including:

* Open-Close price difference
* Low-High price difference
* Price change
* Quarter-end indicator

### Data Processing

The project uses:

* Train-test split with chronological ordering
* Feature scaling using `StandardScaler`
* Random Forest classification

### Model Configuration

The Random Forest model is configured with:

* `n_estimators = 300`
* `max_depth = 12`
* `random_state = 42`

## 📊 Model Evaluation

The model performance is evaluated using:

* Accuracy Score
* Confusion Matrix

These metrics are used to understand how accurately the model predicts the direction of Bitcoin price movement.

## 📂 Project Structure

```text
Bitcoin-Price-Predictor/
│
├── internproject.ipynb    # Data analysis and model training
├── frontproject.py        # Flask prediction application
├── bitcoin.csv            # Historical Bitcoin dataset
├── bitcoinprice.pkl       # Trained Random Forest model
└── README.md              # Project documentation
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ishwarishelke1/Bitcoin-Price-Predictor.git
cd Bitcoin-Price-Predictor
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib joblib flask
```

## ▶️ Run the Project

Run the Flask application:

```bash
python frontproject.py
```

Then open the local Flask URL displayed in the terminal in your browser.

## 🔮 Future Improvements

* Add more technical indicators such as RSI and moving averages
* Compare multiple machine learning algorithms
* Perform hyperparameter tuning
* Improve prediction performance with additional historical features
* Add interactive visualization of Bitcoin market trends

## 👩‍💻 Author

**Ishwari Shelke**

GitHub: [IshwariShelke1](https://github.com/Ishwarishelke1)
