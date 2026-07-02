
import streamlit as st
import numpy as np
import pickle

# Load saved model, scaler and encoder
model = pickle.load(open('house_price_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

# Title
st.title("🏠 House Price Predictor")
st.write("Fill in the details below to predict the sale price of a house!")
st.divider()

# Input sliders
col1, col2 = st.columns(2)

with col1:
    gr_liv_area   = st.slider("Living Area (sqft)",    500,  5000, 1500)
    total_bsmt    = st.slider("Basement Size (sqft)",    0,  3000,  800)
    first_flr     = st.slider("First Floor (sqft)",    500,  4000,  900)
    bedrooms      = st.slider("Bedrooms",                1,    10,    3)
    full_bath     = st.slider("Full Bathrooms",          1,     4,    2)
    half_bath     = st.slider("Half Bathrooms",          0,     2,    1)

with col2:
    tot_rms       = st.slider("Total Rooms",             2,    14,    7)
    garage_cars   = st.slider("Garage Capacity",         0,     4,    2)
    year_built    = st.slider("Year Built",           1900,  2024, 2005)
    overall_qual  = st.slider("Overall Quality (1-10)", 1,    10,    7)
    lot_area      = st.slider("Lot Area (sqft)",      1000, 20000, 8000)
    neighborhood  = st.slider("Neighborhood (1-25)",     1,    25,   10)

st.divider()

# Predict button
if st.button("💰 Predict House Price"):
    # Prepare input
    features = np.array([[
        gr_liv_area, total_bsmt, first_flr,
        bedrooms, full_bath, half_bath,
        tot_rms, garage_cars, year_built,
        overall_qual, lot_area, neighborhood
    ]])

    # Scale and predict
    features_sc     = scaler.transform(features)
    pred_log        = model.predict(features_sc)
    predicted_price = np.expm1(pred_log)[0]

    # Show result
    st.success(f"💰 Predicted Sale Price: ${predicted_price:,.0f}")

    # Show input summary
    st.subheader("📋 House Summary")
    col3, col4, col5 = st.columns(3)
    col3.metric("Bedrooms",    bedrooms)
    col4.metric("Bathrooms",   full_bath)
    col5.metric("Living Area", f"{gr_liv_area} sqft")

    col6, col7, col8 = st.columns(3)
    col6.metric("Year Built",  year_built)
    col7.metric("Quality",     f"{overall_qual}/10")
    col8.metric("Garage",      f"{garage_cars} cars")

st.divider()
st.caption("Built with Python, Scikit-learn and Streamlit")
