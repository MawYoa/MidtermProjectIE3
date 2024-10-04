import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('My First Streamlit App')
st.write('Welcome to my Streamlit app!')


df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")
st.write(df_sample)


df_cleaned = df_sample.dropna()
df_cleaned = df_cleaned.select_dtypes(include=[float, int])

st.write(df_cleaned)

numeric_cols = df_cleaned.columns

stats_df = pd.DataFrame({
    'count': df_cleaned[numeric_cols].count(),
    'mean': df_cleaned[numeric_cols].mean(),
    'median': df_cleaned[numeric_cols].median(),
    'mode': df_cleaned[numeric_cols].mode().iloc[0],  
    'std': df_cleaned[numeric_cols].std(),
    'variance': df_cleaned[numeric_cols].var(),
    'min': df_cleaned[numeric_cols].min(),
    'max': df_cleaned[numeric_cols].max(),
    'range': df_cleaned[numeric_cols].max() - df_cleaned[numeric_cols].min(),
    '25%': df_cleaned[numeric_cols].quantile(0.25),
    '50%': df_cleaned[numeric_cols].quantile(0.50),
    '75%': df_cleaned[numeric_cols].quantile(0.75)
})


stats_df = stats_df.T
stats_df = stats_df.round(2)

st.write("Summary Statistics:")
st.write(stats_df)

# DATA VISUALIZATION

# BARGRAPH

sns.set(style="whitegrid")

st.write("Histograms:")
plt.figure(figsize=(12, 8))
df_cleaned.hist(bins=10, edgecolor='black', layout=(2, 3), figsize=(12, 10))

plt.suptitle('Histograms', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

st.pyplot(plt)