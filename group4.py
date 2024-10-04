import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D

st.title('Analyzing Laptops and Their Prices')

"## GROUP 4 - BM3"

st.write("The purpose of this is to convert our previous Data Visualization activity in Google Colab Notebook into a Streamlit Web Application")
st.write("Also check the GitHub Repository for the source code")

"# Describing the Dataset"

df = pd.read_csv("laptop_price - dataset.csv")
df

df.info()

st.write("The sum of each categorical column can be seen below")

sum = df.isna().sum()
sum

desc = df.describe()
desc

"# Company Column"

company = df['Company'].value_counts()
company


# CPU Frequency Bar Graph (JOHN LARENCE LUSAYA)
st.title('CPU Frequency (GHz)')
st.write("The data indicates a strong preference for CPUs in the 2.00 GHz to 2.90 GHz range, highlighting consumer demand trends and market availability. CPUs with lower frequencies are less frequently found.")