import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in New york city NYC")

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
            
            
DATE_COLUMN = 'data/time'

def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return
    
data_load_state = st.text("Data Loading.....")
data = load_data(10000)
data_load_state.text("DONE")

if st.checkbox("Show Raw data"):
    st.subheader("Row data")
    st.write(data)
    
st.subheader("Number of pickup per hour")
hist_values = np.histogram(data[DATA_COLUMN].dt.hour, bins=24, range=(0,24))[0]
 
st.bar_chart(hist_values)

hour_to_filter = st.slider("hour", 0,23, 17)
filtered_data = data[data[DATA_COLUMN].dt.hour == hour_to_filter]

st.subheader("Map of all pickups at %s:00" % hour_to_filter)
st.map(filtered_data)