import streamlit as st

st.set_page_config(page_title="🏠 Flat Price Predictor", page_icon="🏠", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {background-color: #121212; color: #FFFFFF;}
        h1, h2, h3 {color: #FF5733;}
        .main {
            text-align: center;
        }
        @keyframes float {
            0% {transform: translateY(0);}
            50% {transform: translateY(-10px);}
            100% {transform: translateY(0);}
        }
        .floating-header {
            animation: float 3s ease-in-out infinite;
            font-size: 40px;
            font-weight: bold;
            color: #FF5733;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='floating-header'>🏠 Welcome to Flat Price Predictor</div>", unsafe_allow_html=True)
st.write("### Predict. Analyze. Decide with Confidence.")
st.write("---")
st.write("✅ **Features**:")
st.write("- AI-Powered Flat Price Prediction")
st.write("- Budget Check & Recommendation")
st.write("- Cheaper Alternatives")
st.write("- Explainable AI (SHAP)")
st.write("- Interactive Analytics Dashboard")

st.success("👉 Use the sidebar to navigate between **Predict**, **Dashboard**, and **About** pages.")
