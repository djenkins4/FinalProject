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
    # Creates a map of most expensive Ubers

    # Creates a bar chart of the frequency of each possible number of passengers in an Uber
    data["passenger_count"].astype(int).value_counts().plot(kind="bar", color=col)
    plt.xlabel("Number of Passengers")
    plt.ylabel("Number of Ubers")
    plt.title("Number of Ubers Carrying Each Possible Number of Passengers")
    return plt

# def number_of_passengers

# Creates a pie chart of how frequently people were dropped off at each location


def main():
    data = pd.read_csv('uber.csv')
    data = data.drop(labels=0, axis=0)
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


main()
