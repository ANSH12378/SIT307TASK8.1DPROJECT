
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("housing_price_model.pkl")

st.title("Sydney Housing Price Predictor")

st.write("Enter the property details below to estimate its sale price.")

# Property inputs
suburb = st.selectbox(
    "Suburb",
    ["Blacktown", "Parramatta", "Mosman"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "House", "Townhouse", "Studio"]
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=6,
    value=1
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=10,
    value=1
)

# Predict when button is clicked
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "suburb": [suburb],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "parking": [parking],
        "property_type_ml": [property_type]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Sale Price: ${prediction:,.0f}"
    )
