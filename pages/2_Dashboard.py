import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data(ttl=0)
def load_data():
    return pd.read_csv("cleaned_bangalore_data.csv")

df = load_data()
st.title("📈 Analytics Dashboard")

viz_option = st.selectbox("Choose a Visualization", ["Avg Price by Location", "Price Distribution by BHK", "Location-wise Price vs Sqft"])

if viz_option == "Avg Price by Location":
    avg_prices = df.groupby('location')['price'].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 4))
    avg_prices.plot(kind='bar', color="#FF5733", ax=ax)
    ax.set_ylabel("Price (Lakhs)")
    st.pyplot(fig)

elif viz_option == "Price Distribution by BHK":
    fig, ax = plt.subplots()
    df.boxplot(column='price', by='bhk', ax=ax, grid=False)
    ax.set_ylabel("Price (Lakhs)")
    st.pyplot(fig)

elif viz_option == "Location-wise Price vs Sqft":
    loc = st.selectbox("Select Location", df['location'].unique())
    subset = df[df['location'] == loc]
    fig, ax = plt.subplots()
    ax.scatter(subset['total_sqft'], subset['price'], color="green")
    ax.set_xlabel("Total Sqft")
    ax.set_ylabel("Price (Lakhs)")
    ax.set_title(f"Price vs Sqft in {loc}")
    st.pyplot(fig)
