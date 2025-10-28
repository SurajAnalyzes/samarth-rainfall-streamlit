import streamlit as st
import pandas as pd

# --- (A) Title for your App ---
st.title("Project Samarth Demo: Rainfall Data")
st.header("Build For Bharat Fellowship")

# --- (B) Load the Data ---
# Use the same CSV file name you uploaded
file_name = "Sub_Division_IMD_2017.csv"

# This loads the data
@st.cache_data  # Caches the data for faster loading
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found. Make sure it's in the same folder as app.py.")
        return None

df = load_data(file_name)

if df is not None:
    # --- (C) Create the "Q&A" Filter ---
    st.subheader("Select a Subdivision to see its data:")
    
    # Get all unique subdivision names for the dropdown
    # (The column name in your data is 'SUBDIVISION')
    all_subdivisions = df['SUBDIVISION'].unique()
    
    # Create the dropdown menu
    selected_option = st.selectbox(
        "Which subdivision do you want to see?",
        all_subdivisions
    )

    # --- (D) Show the Answer ---
    st.header(f"Showing results for: {selected_option}")
    
    # Filter the data to show only the selected subdivision
    results_df = df[df['SUBDIVISION'] == selected_option]
    
    # Display the filtered data as a table
    st.dataframe(results_df)

    # --- (E) Cite Your Source (Very Important!) ---
    st.subheader("Data Source (Traceability):")
    st.caption("Data from: data.gov.in (Sub-Divisional Monthly Rainfall from 1901 to 2017)")