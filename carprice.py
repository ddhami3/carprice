import numpy as np 
import streamlit as st
luxury = 0

def model1(x):
    x = np.array(x)
    coeff = np.array([-5.449e-06, 0.0044, 0.0133, -0.0489, -0.0569, 0.3272])
    y = 11.3940+(np.sum(np.multiply(x, coeff)))
    return round(np.exp(y),0)

st.title('Used Car Price Estimator')
st.write('By Omar Qusos and Hamilton Chang')

mileage = st.slider('Max Mileage', 0, 80000, 0, 20)
city_mpg = st.slider('City MPG', 11, 54, 11, 1)highway_mpg = st.slider('Highway MPG', 16, 50, 16, 1)
year = st.slider('Model Year', 2014, 2018, 2014, 1)lux = st.checkbox('Luxury')
if lux:
    luxury = 1
    x = [mileage, city_mpg, highway_mpg, year, luxury]
    st.write('Your Car is worth Approximately')
st.write(model1(x))