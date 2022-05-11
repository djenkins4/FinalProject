"""
Name: Dylan Jenkins
Data: Uber
Description:
This program was created to answer 2 questions about the Uber data set: "What is the relationship between number of
passengers and price?" and "What are the most common locations for pickup and drop-off in this dataset?".
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import csv
import pydeck as pdk


def frequency_of_passengers(data, col):

    # Creates a bar chart of the frequency of each possible number of passengers in an Uber
    data["passenger_count"].astype(int).value_counts().plot(kind="bar", color=col)
    plt.xlabel("Number of Passengers")
    plt.ylabel("Number of Ubers")
    plt.title("Number of Ubers Carrying Each Possible Number of Passengers")
    return plt

def map_of_dropoffs(data, z=1):

    # Creates a map of dropoff locations
    tup = ("lat", "lon") 
    coordinates = data[["dropoff_latitude", "dropoff_longitude"]]
    coordinates = coordinates.rename(columns = {'Latitude':tup[0], 'Longitude':tup[1]})
    coordinates = coordinates.apply(pd.to_numeric)
    st.map(coordinates, zoom=z)

def main():
    # Reads File
    data = pd.read_csv('uber.csv')
    data = data.drop(labels=0, axis=0)
    # Drops invalid data
    for x in data.index:
        if data.loc[x, "passenger_count"] < 1 or data.loc[x, "passenger_count"] > 6:
            data.drop(x, inplace=True)
    # Creates pages
    page = st.sidebar.selectbox("Choose your page", ["Home Page", "Bar Chart", "Pie Chart", "Map"])
    if page == "Home Page":
        main_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">Uber Data</p>'
        sub_title = '<p style="font-family:sans-serif; color:Black; font-size: 22px;"></p>'
        st.markdown(main_title, unsafe_allow_html=True)
        st.markdown(sub_title, unsafe_allow_html=True)
        sub2_title = '<p style="font-family:sans-serif; color:Black; font-size: 16px;">by Dylan Jenkins</p>'
        st.markdown(sub2_title, unsafe_allow_html=True)
    elif page == "Bar Chart":
        st.title("Bar Chart")
        st.pyplot(frequency_of_passengers(data, 'green'), clear_figure=True)
    elif page == "Map":
        st.title("Map of Dropoffs")
        map_of_dropoffs(data)


main()
