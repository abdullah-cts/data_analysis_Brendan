# importing necessary packages

import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import requests

# reading the csv file
internet_use_data_frame = pd.read_csv("internet_use.csv")

# converting the year into integer
internet_use_data_frame["Year"] = internet_use_data_frame["Year"].astype(int)

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
if len(countries) > 0:
    country_name = "https://restcountries.com/v3.1/name/" + countries[-1]
    response = requests.get(country_name)
    data = response.json()
    st.sidebar.header(data[0]["name"]["official"])
    st.sidebar.write(f'Capital: {data[0]["capital"][0]}')

    r = requests.get(data[0]["flags"]["png"])
    with open("flag.png", "wb") as f:
        f.write(r.content)

    # urlretrieve(data[0]["flags"]["png"], "flag.png")
    flag = Image.open("flag.png")
    st.sidebar.image(flag)
    st.sidebar.write(f"Population: {data[0]['population']}")
    st.sidebar.write(f"Driving side: {data[0]['car']['side']}")
    st.sidebar.write(f"First day of week: {data[0]['startOfWeek']}")