import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor
import joblib

# Load the trained CatBoost model
model = CatBoostRegressor()
model.load_model("catboost_model_house.cbm")

def predict_house_price(overall_qual, year_built, total_bsmt_sf, first_flr_sf, gr_liv_area):
    # Perform prediction
    prediction = model.predict([[overall_qual, year_built, total_bsmt_sf, first_flr_sf, gr_liv_area]])[0]
    return prediction

def main():
    st.title("House Price Prediction")
    st.markdown(
        """
        <div style="background-color:#025246;padding:10px;border-radius:10px">
        <h2 style="color:white;text-align:center;">Predict House Price</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add input fields for each feature
    overall_qual = st.number_input("Overall Quality", min_value=1, max_value=10, value=5)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2022, value=2000)
    total_bsmt_sf = st.number_input("Total Basement SF", min_value=0, value=1000)
    first_flr_sf = st.number_input("First Floor SF", min_value=0, value=1000)
    gr_liv_area = st.number_input("Above Ground Living Area SF", min_value=0, value=1500)

    if st.button("Predict Price"):
        # Perform prediction
        prediction = predict_house_price(overall_qual, year_built, total_bsmt_sf, first_flr_sf, gr_liv_area)
        st.success(f"The predicted price of the house is: ${prediction:,.2f}")

if __name__ == "__main__":
    main()
