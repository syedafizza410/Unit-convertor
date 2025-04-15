#Project: 02: Unit Convertor Using Python and Streamlit!

import streamlit as st 
st.markdown(
    """
    <style>
    body {
        background-color: #fff;
        color: black;
    }
    .stApp{
        background-color: linear-gradient(135deg, #0000FF, #FF0000);
        padding: 30px;
        border-radius: 15px;
        }
    h1{
        text-align: center;
        font-size: 35px;
        color: black;
    }
    .stButton>button{
        background: #0000FF;
        color: black;
        font-size: 15px;
        paddingL 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        
    }
    .result-box {
        font-size: 20px
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 203, 201, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1> Unit Convertor using Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length , weight and temperature.")

conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
         to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])  
elif conversion_type == "Weight":
    with col1:
         from_unit = st.selectbox("From", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Miligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value -273.15) * 9/5+32 if to_unit == "Fahrenhiet" else value
    return value

if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>" , unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by UmmeFizza </div>", unsafe_allow_html=True)

