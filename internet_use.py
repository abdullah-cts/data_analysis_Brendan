# importing necessary packages

import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image

# reading the csv file
internet_use_data_frame = pd.read_csv("internet_use.csv")

# converting the year into integer
internet_use_data_frame["Year"] = internet_use_data_frame["Year"].astype(int)

# multiple column example
col1, col2 = st.columns(2)
with col1:
    st.title("Column One")
    st.write("Dataset stats")
    st.write(internet_use_data_frame.describe())

with col2:
    st.title("Column Two")
    st.write("Another column")
    st.write("You can other things over here")

# list of countries from the dataframe
country_or_area_name = pd.unique(internet_use_data_frame["Country or Area"])
# removing the nan from the list of counties
country_or_area_name = country_or_area_name[:-1]

# Page header
st.header("Internet Use")

# select one or more countries
countries = st.multiselect("Select one or more countries", country_or_area_name)

selected_data = internet_use_data_frame[internet_use_data_frame["Country or Area"].isin(countries)]

st.subheader("Line chart")
fig_one = px.line(selected_data, x="Year", y="Value", color="Country or Area")
st.plotly_chart(fig_one)

st.subheader("Bar chart")
fig_two = px.bar(selected_data, x="Year", y="Value", color="Country or Area")
st.plotly_chart(fig_two)

# sidebar example
st.sidebar.title("Test sidebar")
st.sidebar.write("This is an example text. This is just a line, but it could go more than one line")
image = Image.open("pattern.jpg")
st.sidebar.image(image)



