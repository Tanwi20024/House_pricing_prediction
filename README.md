# House_pricing_prediction
Linear regression model to predict house price based on features such as the number of rooms, location, size and other relevant factors.

link - https://housepricingprediction-55bjmlhfbu2tp3hfmzfihf.streamlit.app

# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview
This project predicts house sale prices based on features like
number of rooms, location, size, quality and year built.
Built using Python and Linear Regression on the Kaggle House Prices dataset.

## 📊 Dataset
- Source: Kaggle House Prices Competition
- 1460 houses with 81 features each
- Target variable: SalePrice

## 🔍 Features Used
- Size (Living area, Basement, First floor)
- Rooms (Bedrooms, Bathrooms, Total rooms)
- Location (Neighborhood)
- Quality rating (1-10)
- Year built
- Garage capacity

## 🤖 Model
- Algorithm: Linear Regression
- R² Score: 0.87 (87% accuracy)
- MAE: ~$21,000
- RMSE: ~$31,000

## 🛠️ Tools Used
- Python
- Google Colab
- Pandas, Numpy
- Scikit-learn
- Matplotlib, Seaborn

## ▶️ How to Run
1. Open `House_Price_Prediction.ipynb` in Google Colab
2. Upload `train.csv` from Kaggle
3. Run all cells step by step

## 📁 Files
- `House_Price_Prediction.ipynb` — Main notebook
- `house_price_model.pkl` — Saved trained model
- `scaler.pkl` — Saved scaler
