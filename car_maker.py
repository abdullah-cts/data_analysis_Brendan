# importing packages

import streamlit as st
import plotly.express as px
import pandas as pd

# read the excel file into a Pandas dataframe
# need to install openpyxl to read and/or write excel file. Alternate option is to convert the excel file into a csv file
car_dataframe = pd.read_excel("car_make.xlsx")
# shuffle the dataframe inplace, so the plot does not look monotonous
car_dataframe = car_dataframe.sample(frac=1).reset_index(drop=True)

# getting all the column names
col_names = list(car_dataframe.columns)

st.header("Car production from different makers")

# A dropdown option box to choose a year
option = st.selectbox("Choose a year", ("2016", "2020", "2021"))

if option == "2016":
    fig = px.bar(car_dataframe, x=col_names[0], y=col_names[1], color=col_names[0])
elif option == "2020":
    fig = px.bar(car_dataframe, x=col_names[0], y=col_names[2], color=col_names[0])
else:
    fig = px.bar(car_dataframe, x=col_names[0], y=col_names[3], color=col_names[0])

st.plotly_chart(fig)

# change of production calculation from year 2016 to year 2021
st.header("Change of production from 2016 to 2021")
# creating a new column
production_change = (car_dataframe[col_names[3]] - car_dataframe[col_names[1]]) / 100
# adding the created column into the existing dataframe
car_dataframe['Production change'] = production_change

change_fig = px.bar(car_dataframe, x=col_names[0], y='Production change', color=col_names[0])
st.plotly_chart(change_fig)









