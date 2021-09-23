import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import plotly.express as px
import joblib
import base64


data = pd.read_excel('waterpotability.xlsx')
data = data.iloc[:,1:]
original_data = pd.read_excel('waterpotability.xlsx')
feature_list = {'ph':0,'Hardness':0,'Solids':0,'Chloramines':0,'Sulfate':0,'Conductivity':0,'Organic_carbon':0,'Trihalomethanes':0,'Turbidity':0}

classifier = joblib.load('classifier.sav')
main_bg = "aqua.jpg"
main_bg_ext = "jpg"

side_bg = "aqua.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Water Potability Prediction !!!!!!!')
st.subheader('Predict the water you drink is pure or not ??')
st.sidebar.header('Predict The Purity')
for j in feature_list.keys():
    feature_list[j] = st.sidebar.text_input(f'enter value for {j}')




if st.sidebar.button('Predict'):
    pred = classifier.predict([list(feature_list.values())])
    if pred[0]==0:
        st.sidebar.markdown('water is not so potable for drinking purpose')
    else:
        st.sidebar.markdown('water is potable for drinking purpose')
    
    
st.image('water.jpg')
header = st.container()
body = st.container()
with header:
    col1,col2 = st.columns(2)
    plot_type = col1.selectbox('Plot the feature',['histogram','line plot','area chart'])
    feat = col1.selectbox('Which feature',['ph','Chloramines','Organic_carbon','Turbidity','Solids','Conductivity','Hardness','Trihalomethanes','Sulfate'])
    if plot_type == 'histogram':
        col2.bar_chart(data[feat][:90])
        col1.header(f'{plot_type} of {feat} feature')
    if plot_type == 'line plot':
        col2.line_chart(data[feat][:90])
        col1.header(f'{plot_type} of {feat} feature')
    if plot_type == 'area chart':
        col2.area_chart(data[feat][:90])
        col1.header(f'{plot_type} of {feat} feature')
with body:
    col1, col2 = st.columns(2)
    col1.header('About Me')
    col1.markdown('''My name is Harish Gehlot , I'm pursuing my Computer Science Degree and love to do Machine Learning stuff''')
    col2.header('About Project')
    col2.markdown("Are you researching for water potability check, Just fill the content of water and here you go")

        
