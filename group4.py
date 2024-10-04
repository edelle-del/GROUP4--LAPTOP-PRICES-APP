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

df['CPU_Frequency (GHz)'].value_counts()

data = {
    "CPU_Frequency (GHz)": [2.50, 2.80, 2.70, 1.60, 2.30, 2.00, 1.80, 2.60, 1.10, 2.40,
                            2.90, 3.00, 1.20, 1.44, 2.20, 1.50, 1.30, 3.60, 3.10, 2.10,
                            1.90, 0.90, 3.20, 1.00, 1.92],
    "count": [285, 165, 164, 124, 86, 86, 78, 74, 53, 50,
              19, 19, 15, 12, 11, 10, 6, 5, 3, 3,
              2, 2, 1, 1, 1]
}

df = pd.DataFrame(data)

cpu_frequency = df["CPU_Frequency (GHz)"].values
count = df["count"].values
x = np.arange(len(cpu_frequency))

plt.figure(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(cpu_frequency)))

plt.bar(x, count, color=colors)

plt.xlabel('CPU Frequency (GHz)')
plt.ylabel('Count')
plt.title('CPU Frequency Preference')

plt.xticks(x, cpu_frequency, rotation=40, ha='right', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

plt.show()
