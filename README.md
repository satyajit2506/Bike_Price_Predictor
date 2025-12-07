🚴‍♂️ Bike Price Prediction using Machine Learning

An end-to-end machine learning project that predicts the selling price of a bike using a Random Forest Regression model. This project covers data cleaning, feature engineering, model training, evaluation, and deployment through an interactive prediction app.

📘 Project Summary

This project aims to build a reliable system capable of predicting bike prices based on historical data. The dataset contains features like brand, model, year, mileage, engine capacity, power, and ownership details. I performed complete preprocessing, handled missing values, encoded categorical variables, removed irrelevant features, and created a final dataset suitable for ML modeling.

The final model achieved high accuracy and provides highly relevant price predictions.

🗂️ Project Workflow
1️⃣ Data Collection

The dataset (CSV format) contains various features influencing bike prices such as:

Brand & Model

Year of Purchase

Engine CC

Mileage

Power

Torque

Owner Type

Condition

Kilometers Driven

Ex-Showroom Price

2️⃣ Data Cleaning & Preprocessing

A major part of the project involved preparing the raw data:

✔ Removed duplicates
✔ Treated missing/null values
✔ Removed unwanted/irrelevant columns
✔ Fixed inconsistent formats (string-to-int conversions, etc.)
✔ Handled outliers where necessary
✔ Standardized units (CC, mileage, power)

3️⃣ Feature Engineering

To improve the model quality:
✔ Label Encoding for ordinal categorical features
✔ One-Hot Encoding for multi-category columns
✔ Created additional meaningful columns (age, km/year etc.)
✔ Checked correlation and selected impactful features
✔ Feature scaling where needed

I also identified and visualized the Top 10 most important features affecting the bike price.

4️⃣ Model Building – Random Forest Regressor

I trained a RandomForestRegressor, which works well for non-linear, mixed-type datasets.

Model steps:

Train–test split

Hyperparameter tuning

Model fitting

Cross-validation

Error metrics evaluation

Metrics used:

MAE

RMSE

R² Score

The model achieved high accuracy and performs well on unseen data.

5️⃣ Deployment – Bike Price Predictor App

A complete prediction app was created where users input bike details such as:

Brand

Model

Year

Mileage

Engine CC

Power

Condition

Ownership

The app instantly predicts the expected selling price using the trained Random Forest model.

📁 Project Structure
├── data/
│   ├── bike_data.csv
├── notebooks/
│   ├── EDA.ipynb
│   ├── model_training.ipynb
├── app/
│   ├── app.py
│   ├── model.pkl
├── README.md
├── requirements.txt

🔧 Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Jupyter Notebook

Streamlit / Flask (for app)

🚀 How to Run the Project
Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app.py

📊 Key Highlights

✔ Clean and well-organized dataset
✔ Advanced feature engineering
✔ Highly accurate Random Forest Model
✔ Feature Importance visualization
✔ End-to-end deployment-ready project
✔ Real-world practical use case

🏁 Conclusion

This project demonstrates the complete lifecycle of an ML solution — from raw data to prediction app. With a strong Random Forest model, optimized preprocessing steps, and a user-friendly interface, it provides a practical and reliable bike price prediction system.
