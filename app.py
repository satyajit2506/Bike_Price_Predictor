import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load Model and Encoders
# ----------------------------
model = joblib.load("price_prediction_model.pkl")
brand_encoder = joblib.load("brand_label_encoder.pkl")
owner_encoder = joblib.load("owner_label_encoder.pkl")
location_encoder = joblib.load("location_freq_map.pkl")
model_variant_encoder = joblib.load("model_variant_freq_map.pkl")

# ----------------------------
# Streamlit Page Config & Style
# ----------------------------
st.set_page_config(page_title="Vehicle Price Predictor", page_icon="🚗", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #232526, #414345);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    h1, h2, h3 {
        color: #FFD700 !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #ffcc00;
        color: black;
    }
    .stNumberInput > div > div > input, 
    .stSelectbox > div > div > div {
        background-color: #2e2e3a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.title("🚗 Vehicle Price Prediction App")
st.write("### Get the estimated market price of your vehicle instantly using a trained ML model.")
st.markdown("---")

# ----------------------------
# Sidebar Input Fields
# ----------------------------
st.sidebar.header("🔧 Enter Vehicle Details")

model_year = st.sidebar.number_input("Model Year", min_value=1990, max_value=2025, value=2020)
kms_driven = st.sidebar.number_input("KMs Driven", min_value=0, max_value=300000, value=20000)

# Selectboxes for categorical features (use encoder classes_)
brand_name = st.sidebar.selectbox("Brand", sorted(list(brand_encoder.classes_)))
owner_name = st.sidebar.selectbox("Owner Type", sorted(list(owner_encoder.classes_)))
location_name = st.sidebar.selectbox("Location", sorted(list(location_encoder.keys())))
model_variant_name = st.sidebar.selectbox("Model Variant", sorted(list(model_variant_encoder.keys())))

mileage = st.sidebar.number_input("Mileage (kmpl)", min_value=0.0, value=45.0)
power = st.sidebar.number_input("Power (bhp)", min_value=0.0, value=15.0)
engine_cc = st.sidebar.number_input("Engine CC", min_value=50.0, value=150.0)

# ----------------------------
# Encode Inputs
# ----------------------------
try:
    brand_encoded = int(brand_encoder.transform([brand_name])[0])
    owner_encoded = int(owner_encoder.transform([owner_name])[0])
except Exception:
    st.error("⚠️ Error encoding brand or owner. Please check your encoder files.")
    st.stop()

# frequency-encoded ones (dicts)
location_encoded = location_encoder.get(location_name, 0)
model_variant_encoded = model_variant_encoder.get(model_variant_name, 0)

# ----------------------------
# Create Input DataFrame
# ----------------------------
user_data = pd.DataFrame([{
    'model_year': model_year,
    'kms_driven': kms_driven,
    'owner': owner_encoded,
    'location': location_encoded,
    'mileage': mileage,
    'power': power,
    'brand': brand_encoded,
    'engine_cc': engine_cc,
    'model_variant_encoded': model_variant_encoded
}])

# ----------------------------
# Predict Button
# ----------------------------
if st.button("🔍 Predict Price"):
    predicted_price = model.predict(user_data)[0]
    st.success(f"💰 **Estimated Price:** ₹{predicted_price:,.2f}")
    st.balloons()

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("✨ Built by Satyajit using Random Forest Regressor")
