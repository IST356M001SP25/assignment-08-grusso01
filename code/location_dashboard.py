'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

data = pd.read_csv('./cache/tickets_in_top_locations.csv')
st.title('Top Locations for Parking Tickets in Syracuse')
st.caption('This shows the parking tickets that were issued in the top locations with $1,000 or more in total violation amounts.')

unique_locations = data['location'].unique()
selected_location = st.selectbox('Select a location:', unique_locations)

if selected_location:
    subset = data[data['location'] == selected_location]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total tickets issued", subset.shape[0])
        fig1, ax1 = plt.subplots()
        ax1.set_title('Tickets Issued by Hour of Day')
        sns.barplot(data=subset, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.metric("Total amount", f"$ {subset['amount'].sum()}")
        fig2, ax2 = plt.subplots()
        ax2.set_title('Tickets Issued by Day of Week')
        sns.barplot(data=subset, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax2)
        st.pyplot(fig2)

    st.map(subset[['lat', 'lon']])