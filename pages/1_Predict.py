import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import shap

# Load model and data
model = pickle.load(open("flat_price_model.pkl", "rb"))
feature_names = model.feature_names_in_
locations = [f for f in feature_names if f not in ['total_sqft', 'bath', 'bhk']]

@st.cache_data(ttl=0)
def load_data():
    return pd.read_csv("cleaned_bangalore_data.csv")

df = load_data()

# Custom CSS for sexy button
st.markdown("""
    <style>
        body {background-color: #121212; color: #FFFFFF;}
        .stButton>button {
            background: linear-gradient(135deg, #ff4b2b, #ff416c);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 30px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.4s ease-in-out;
            box-shadow: 0 4px 10px rgba(255, 65, 108, 0.4);
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            transform: scale(1.08);
            box-shadow: 0 6px 18px rgba(255, 65, 108, 0.6);
        }
        .stButton>button:active {
            transform: scale(0.95);
            box-shadow: 0 2px 6px rgba(255, 65, 108, 0.4);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Predict Flat Price")

location = st.selectbox("📍 Location", locations)
sqft = st.slider("📏 Total Area (sqft)", 500, 5000, step=50)
bhk = st.selectbox("🛏️ Bedrooms (BHK)", [1, 2, 3, 4, 5])
bath = st.selectbox("🚿 Bathrooms", [1, 2, 3, 4])
budget = st.number_input("💰 Your Budget (₹ Lakhs)", 10, 1000, step=5)

if st.button("🔥 Predict & Explain"):
    input_data = np.zeros(len(feature_names))
    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk
    if location in feature_names:
        loc_index = np.where(feature_names == location)[0][0]
        input_data[loc_index] = 1

    predicted_price = model.predict([input_data])[0]

    st.success(f"📌 Estimated Price: ₹ {predicted_price:.2f} Lakhs")
    
    if predicted_price <= budget:
        st.write("✅ Within budget! Great deal.")
        st.balloons()
    elif predicted_price <= budget * 1.1:
        st.write("⚠️ Slightly above budget. Consider negotiating.")
    else:
        st.write("❌ Overpriced. Check alternatives below.")

    # Price comparison
    fig, ax = plt.subplots()
    ax.bar(["Budget", "Predicted"], [budget, predicted_price], color=["#4CAF50", "#FF5733"])
    st.pyplot(fig)

    # Cheaper Alternatives
    st.markdown("## 🔍 Cheaper Alternatives")
    similar = df[(df['bhk'] == bhk) & (df['total_sqft'] >= sqft*0.8) & (df['total_sqft'] <= sqft*1.2)]
    if not similar.empty:
        cheaper = similar.groupby('location')['price'].mean().sort_values().head(3)
        st.table(cheaper.reset_index().rename(columns={'location': 'Location', 'price': 'Avg Price (Lakhs)'}))
    else:
        st.warning("No alternatives found.")
