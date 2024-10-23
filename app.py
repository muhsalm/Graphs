import streamlit as st
import matplotlib.pyplot as plt

# Set the Streamlit app layout
st.set_page_config(page_title="Graph Plotter", layout="wide")

# Title of the app
st.title("Graph Plotter")

# Input fields for X and Y values
x_values = st.text_input("Enter X Values (comma-separated)", "A, B, C, D")
y_values = st.text_input("Enter Y Values (comma-separated)", "2, 3, 5, 7")
graph_title = st.text_input("Enter Title of the Graph", "My Graph Title")
x_axis_title = st.text_input("Enter X-Axis Title", "Categories")
y_axis_title = st.text_input("Enter Y-Axis Title", "Values")

# Process input values
try:
    x = x_values.split(",")
    y = [float(val) for val in y_values.split(",")]

    if len(x) != len(y):
        st.error("The number of X and Y values must match.")
    else:
        # Plot the graph
        fig, ax = plt.subplots()
        ax.bar(x, y)
        ax.set_title(graph_title)
        ax.set_xlabel(x_axis_title)
        ax.set_ylabel(y_axis_title)

        # Display the graph in the Streamlit app
        st.pyplot(fig)
except ValueError:
    st.error("Please enter valid numeric values for Y.")
