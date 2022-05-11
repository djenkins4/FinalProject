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

'''def passengers_and_price(x, y):
    global data
    # Creates scatter plot
    plt.plot(passengers, price)
    plt.xlabel('Number of Passengers')
    plt.ylabel('Price')
    plt.title('Relationship between Price and Passengers')
    plt.xticks([1, 2, 3, 4, 5, 6])
    plt.yticks(price)

    num_pass = []
    price_list = []
    for row in data:
        st.write(row)
        num_pass = int(row["passenger_count"])  # values read in are strings!
        price_list = float(row["fare_amount"])
        passengers.append(num_pass)
        price.append(price_list)

    st.write("#ofPASSENGERS:", passengers)
    st.write("PRICES:", price)

    st.pyplot(passengers, price)'''


def most_expensive_ubers(data, col):
    # Creates a map of most expensive Ubers

    # Creates a bar chart of most expensive Ubers
    data["fare_amount"].astype(float).value_counts().plot(kind="bar", color=col)
    plt.xlabel("key")
    plt.ylabel("Price")
    plt.title("Top 5 Most Expensive Ubers")


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
        st.pyplot(most_expensive_ubers(data, 'green'), clear_figure=True)


main()
