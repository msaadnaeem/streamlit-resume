import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
colLeft,colRight=st.columns(2)
with colLeft:
    st.title('Resume')
    st.header('John Doe')

with colRight:
    pic=Image.open('dp.png')
    st.image(pic,width=175)   


colLeft,colRight=st.columns(2)
with colLeft:
    st.subheader('Bio Data')
    st.write('Name: John Doe')
    st.write('Email: johndoe@gmail.com')

with colRight:
    st.subheader('Education')
    st.write('Masters: Oxford University')
    st.write('Bachelors: Oxford University')

skills={
    'Skills':['Python','SQL','Excel'],
    'Levels':[30,20,50]
}

skillsDf=pd.DataFrame(skills)
st.write(skillsDf)

fig=px.pie(skillsDf, values='Levels', names='Skills', title='My Skills')
st.plotly_chart(fig)
