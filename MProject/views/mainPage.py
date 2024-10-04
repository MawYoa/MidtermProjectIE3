import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

# Title of the Streamlit app
st.title('Interactive Student Performance Dashboard')
st.write("📊 This dataset comprises various attributes related to student performance, including hours of study, practice, teamwork involvement, midterm exam scores, final exam scores, overall scores, and corresponding grades.")

# Load the dataset
df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# Display raw data
st.write("Raw Data:")
st.write(df_sample)

# --- User Controls for Interactive Filtering ---
# Select columns for visualization (numeric columns only)
numeric_columns = df_sample.select_dtypes(include=[float, int]).columns.tolist()
selected_columns = st.multiselect("Select columns to visualize", numeric_columns, default=numeric_columns)

# Slider for adjusting data range (e.g., filter by Midterm Exam Scores)
min_value, max_value = st.slider(
    'Filter by Midterm Exam Scores (Range)',
    float(df_sample['MidTerm'].min()), 
    float(df_sample['MidTerm'].max()), 
    (float(df_sample['MidTerm'].min()), float(df_sample['MidTerm'].max()))
)

# Filter data based on the slider range
df_filtered = df_sample[(df_sample['MidTerm'] >= min_value) & (df_sample['MidTerm'] <= max_value)]

st.write(f"Filtered Data (Midterm Scores between {min_value} and {max_value}):")
st.write(df_filtered)

# --- Data Visualization ---
# Clean data for visualization: Drop NA and non-numeric columns
df_cleaned = df_filtered.dropna()
df_cleaned = df_cleaned[selected_columns]

# Show summary statistics of the filtered data
st.write("Summary Statistics of Filtered Data:")
st.write(df_cleaned.describe().T)

# --- Plot Histograms with Plotly ---
st.write("Histograms of Selected Columns (Using Plotly):")

# Prepare data for Plotly histogram
hist_data = [df_cleaned[col].values for col in selected_columns]
group_labels = selected_columns

# Create Plotly distplot
fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5]*len(selected_columns))

# Plot!
st.plotly_chart(fig, use_container_width=True)

# --- Heatmap for Correlation Matrix ---
st.write("Correlation Matrix Heatmap:")

# Check if there are enough numeric columns to compute the correlation
if len(df_cleaned.columns) > 1:
    # Clear the figure before plotting
    plt.clf()
    
    # Compute correlation matrix
    corr = df_cleaned.corr()
    
    # Set up the figure size and draw the heatmap
    plt.figure(figsize=(14, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True)

    # Display the heatmap in Streamlit
    st.pyplot(plt)
else:
    st.write("Not enough data to generate a correlation heatmap.")
