import streamlit as st
import streamlit.components.v1 as components
import os

# Set the page title that appears in your browser tab
st.set_page_config(page_title="FetalScan AI", layout="wide")

# --- PART 1: SHOW THE FACE (HTML) ---
try:
    with open("fetal_anemia_detection.html", 'r', encoding='utf-8') as f:
        html_data = f.read()
    # This displays your beautiful HTML design
    components.html(html_data, height=800, scrolling=True)
except FileNotFoundError:
    st.error("I can't find 'fetal_anemia_detection.html'. Make sure it's in the same folder!")

# --- PART 2: THE SIDEBAR CONTROLS ---
st.sidebar.title("Settings & Execution")
st.sidebar.info("Use the buttons below to trigger the Python logic.")

if st.sidebar.button("Run Anemia Detection (Brain)"):
    st.sidebar.warning("Starting the analysis...")
    # This tells your computer to run the Python file you already have
    os.system("python \"transfer_learning_for_the_anemia (1).py\"")
    st.sidebar.success("Process Finished!")

if st.sidebar.button("View Statistical Reports"):
    os.system("python \"anemia (1).py\"")
    st.sidebar.success("Reports Generated!")