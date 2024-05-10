import streamlit as st
from catboost import CatBoostRegressor

# Load the trained CatBoost model
model = CatBoostRegressor()
model.load_model("catboost_model_house_v2.cbm")

def predict_house_price(overall_qual, lot_area, overall_cond, year_built, year_remod_add,
                        total_bsmt_sf, first_flr_sf, second_flr_sf, gr_liv_area, full_bath,
                        half_bath, bedroom_abv_gr, kitchen_abv_gr, tot_rms_abv_grd,
                        garage_cars, garage_area, sale_price):
    # Perform prediction
    prediction = model.predict([[overall_qual, lot_area, overall_cond, year_built, year_remod_add,
                                  total_bsmt_sf, first_flr_sf, second_flr_sf, gr_liv_area, full_bath,
                                  half_bath, bedroom_abv_gr, kitchen_abv_gr, tot_rms_abv_grd,
                                  garage_cars, garage_area, sale_price]])[0]
    return prediction

def about():
    st.title("About")
    st.write("This web application predicts house prices based on various features.")
    st.subheader("Parameters:")
    st.write("- Overall Quality: Rating of overall material and finish of the house (1-10).")
    st.write("- Lot Area: Lot size in square feet.")
    st.write("- Overall Condition: Rating of overall condition of the house (1-10).")
    st.write("- Year Built: Original construction year.")
    st.write("- Year Remodeled: Remodel year (same as construction year if no remodeling or additions).")
    st.write("- Total Basement SF: Total square feet of basement area.")
    st.write("- First Floor SF: Square footage of first floor.")
    st.write("- Second Floor SF: Square footage of second floor.")
    st.write("- Above Ground Living Area SF: Square footage of above ground living area.")
    st.write("- Full Bath: Number of full bathrooms.")
    st.write("- Half Bath: Number of half bathrooms.")
    st.write("- Bedroom Above Grade: Number of bedrooms above ground.")
    st.write("- Kitchen Above Grade: Number of kitchens above ground.")
    st.write("- Total Rooms Above Grade: Total rooms above grade (does not include bathrooms).")
    st.write("- Garage Cars: Size of garage in car capacity.")
    st.write("- Garage Area: Size of garage in square feet.")
    st.write("- Sale Price: Sale price of the house.")
    st.subheader("About the Author:")
    st.write("This web application was created by Omkareshwar. Connect with me on [![GitHub](https://img.shields.io/badge/GitHub-omkareshwar9849-blue?logo=github)](https://github.com/omkareshwar9849) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Omkar%20Eshwar-blue?logo=linkedin)](https://www.linkedin.com/in/omkar1520/).")
    # st.image("profile_picture.jpg", caption="Your Name", use_column_width=True)

def main():
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
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
        lot_area = st.number_input("Lot Area", min_value=0, value=10000)
        overall_cond = st.number_input("Overall Condition", min_value=1, max_value=10, value=5)
        year_built = st.number_input("Year Built", min_value=1800, max_value=2022, value=2000)
        year_remod_add = st.number_input("Year Remodeled", min_value=1800, max_value=2022, value=2000)
        total_bsmt_sf = st.number_input("Total Basement SF", min_value=0, value=1000)
        first_flr_sf = st.number_input("First Floor SF", min_value=0, value=1000)
        second_flr_sf = st.number_input("Second Floor SF", min_value=0, value=500)
        gr_liv_area = st.number_input("Above Ground Living Area SF", min_value=0, value=1500)
        full_bath = st.number_input("Full Bath", min_value=0, value=2)
        half_bath = st.number_input("Half Bath", min_value=0, value=1)
        bedroom_abv_gr = st.number_input("Bedroom Above Grade", min_value=0, value=3)
        kitchen_abv_gr = st.number_input("Kitchen Above Grade", min_value=0, value=1)
        tot_rms_abv_grd = st.number_input("Total Rooms Above Grade", min_value=0, value=6)
        garage_cars = st.number_input("Garage Cars", min_value=0, value=2)
        garage_area = st.number_input("Garage Area", min_value=0, value=500)
        sale_price = st.number_input("Sale Price", min_value=0, value=200000)

        if st.button("Predict Price"):
            # Perform prediction
            prediction = predict_house_price(overall_qual, lot_area, overall_cond, year_built, year_remod_add,
                                             total_bsmt_sf, first_flr_sf, second_flr_sf, gr_liv_area, full_bath,
                                             half_bath, bedroom_abv_gr, kitchen_abv_gr, tot_rms_abv_grd,
                                             garage_cars, garage_area, sale_price)
            st.success(f"The predicted price of the house is: ${prediction:,.2f}")

    elif choice == "About":
        about()

if __name__ == "__main__":
    main()
