# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

if os.path.exists("data.csv"):
    df_csv = pd.read_csv("data.csv")
else:
    st.error("data.csv not found!")
    df_csv = None

try:
    with open("data.json", "r") as f:
        json_data = json.load(f)
except:
    st.error("data.json not found!")
    json_data = None

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Population of Japanese Cities") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.

if json_data is not None:
    df_json = pd.DataFrame(json_data["data_points"])
    chart_json = df_json.set_index("label")["value"]
    st.bar_chart(chart_json)
    st.caption("In units of 100k people")
    st.markdown("**Description:** This bar chart shows the population of major Japanese cities (excluding Tokyo) in 2025.")
else:
    st.error("No JSON data available.")

# GRAPH 2: DYNAMIC GRAPH
st.subheader("Filter Cities by Minimum Population") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.

if json_data is not None:
    df_json = pd.DataFrame(json_data["data_points"])
    minimum = int(df_json["value"].min())
    maximum = int(df_json["value"].max())
    
    st.session_state.setdefault("min_pop", minimum)
    min_pop = st.slider("Minimum Population (100k)", minimum, maximum, st.session_state["min_pop"])  #NEW

    filtered = df_json[df_json["value"] >= min_pop].set_index("label")["value"]
    st.bar_chart(filtered)
    
    st.caption("In units of 100k people") #NEW
    st.markdown("**Description:** Use the slider to filter cities by minimum population.")
    
else:
    st.error("No JSON data available.") #NEW

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Customize Your Fruit Basket") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

if df_csv is not None:
    st.session_state.setdefault("fruits", df_csv[["Category", "Value"]].to_dict("records"))

    if st.button("Restore from CSV"): #NEW
        st.session_state["fruits"] = df_csv[["Category", "Value"]].to_dict("records")

    new_cat = st.text_input("Category", value="Apple") #NEW
    new_val = st.number_input("Value", min_value=0, step=1, value=20) #NEW

    if st.button("Add / Update"):
        exists = False
        for f in st.session_state["fruits"]:
            if f["Category"] == new_cat:
                f["Value"] = int(new_val)
                exists = True
                break
        if not exists:
            st.session_state["fruits"].append({"Category": new_cat, "Value": int(new_val)})

    df_chart = pd.DataFrame(st.session_state["fruits"])
    updated = df_chart.set_index("Category")["Value"]
    st.bar_chart(updated)

    st.markdown("**Description:** Add and update fruit categories and their values using the text input and number input fields.")

else:
    st.error("No CSV data available.")