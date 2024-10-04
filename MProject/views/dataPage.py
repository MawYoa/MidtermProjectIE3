import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Slider for adjusting data range (e.g., filter by hours of study)
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

# --- Plot Histograms ---
sns.set(style="whitegrid")

st.write("Histograms of Selected Columns:")

# Check if there is data to plot
if not df_cleaned.empty:
    # Clear the plot before creating a new one
    plt.clf()

    # Create the histograms
    df_cleaned.hist(bins=10, edgecolor='black', layout=(2, 3), figsize=(12, 10))

    # Add title and adjust layout
    plt.suptitle('Histograms (Filtered Data)', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Display the plot in Streamlit
    st.pyplot(plt)
else:
    st.write("No data available for the selected filters.")
