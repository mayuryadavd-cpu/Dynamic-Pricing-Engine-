import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Price Optimizer", layout="wide")
st.title("💰 AI Dynamic Pricing Engine")

# Load model
model = joblib.load('model.pkl')

# Inputs
col1, col2, col3 = st.columns(3)

with col1:
    base_price = st.number_input("Base Price ($)", min_value=50, max_value=2000, value=500)

with col2:
    demand = st.slider("Current Demand (%)", 0, 100, 50)

with col3:
    inventory = st.slider("Inventory Level", 0, 500, 250)

# Calculate price
if st.button("🎯 Calculate Optimal Price", type="primary"):
    prediction = model.predict([[base_price, demand, inventory]])[0]
    
    # Apply rules
    final_price = max(prediction, base_price * 0.7)
    final_price = min(final_price, base_price * 1.5)
    
    # Show result
    st.success(f"### 💰 AI Recommended Price: **${final_price:.2f}**")
    
    # Show reasoning
    st.write("**Why this price?**")
    
    col1, col2 = st.columns(2)
    with col1:
        if demand > 70:
            st.warning(f"⚠️ High demand ({demand}%) → Price increased")
        elif demand < 30:
            st.success(f"✅ Low demand ({demand}%) → Price decreased")
        else:
            st.info(f"➡️ Normal demand ({demand}%) → No change")
    
    with col2:
        if inventory < 20:
            st.warning(f"⚠️ Low inventory ({inventory}) → Price increased")
        elif inventory > 400:
            st.success(f"✅ High inventory ({inventory}) → Price decreased")
        else:
            st.info(f"➡️ Normal inventory ({inventory}) → No change")