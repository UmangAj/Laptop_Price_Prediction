import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")

# Brand
company = st.selectbox("Company Name", df["Company"].unique())

# Type of Laptop
type = st.selectbox("Type of Laptop", df["TypeName"].unique())

# GPU
gpu = st.selectbox('GPU',df['Gpu Brand'].unique())

# CPU
cpu = st.selectbox('CPU',df['Cpu Brand'].unique())

# OS
os = st.selectbox('OS',df['os'].unique())

# RAM
ram = st.selectbox("RAM (in GB)", [2,4,6,8,12,16,24,32,64])

# HDD
hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])

# Touchscreen
touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])

# Screen Size
screen_size = st.number_input("Screen Size")

# Resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# IPS
ips = st.selectbox("IPS", ["Yes", "No"])

# Weight
weight = st.number_input("Weight of the Laptop")

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.write("### The predicted price is : Rs.  " + str(int(np.exp(pipe.predict(query)[0]))))



