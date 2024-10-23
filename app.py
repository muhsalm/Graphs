import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set the Streamlit app layout
st.set_page_config(page_title="Graph Plotter", layout="wide")

# Title of the app
st.title("Graph Plotter")

# Input fields for x and y values
x_values = st.text_input("Enter X Values (comma-separated)", "A, B, C, D")
y_values = st.text_input("Enter Y Values (comma-separated)", "2, 3, 5, 7")
graph_title = st.text_input("Enter Title of the Graph", "My Graph Title")
x_axis_title = st.text_input("Enter Title for X-Axis", "X Axis Title")
y_axis_title = st.text_input("Enter Title for Y-Axis", "Y Axis Title")

# Select box for graph type
graph_type = st.selectbox("Select Graph Type", ["Line", "Bar", "Scatter", "Area", "Histogram", "Pie", "Box"])

# Button to plot the graph
if st.button("Plot Graph"):
    try:
        # Convert input strings to lists
        x = x_values.split(",")
        y = np.array(list(map(float, y_values.split(","))))
        
        # Validate the lengths of x and y
        if len(x) != len(y):
            st.error("The number of X values must match the number of Y values.")
        else:
            # Normalize y values to get colors
            norm = plt.Normalize(y.min(), y.max())
            colors = plt.cm.Blues(norm(y))

            # Create the plot with a black background
            plt.figure(facecolor='black')
            plt.gca().set_facecolor('black')

            if graph_type == "Line":
                plt.plot(x, y, color='blue', linewidth=2)
            elif graph_type == "Bar":
                plt.bar(x, y, color=colors)
            elif graph_type == "Scatter":
                plt.scatter(x, y, color=colors)
            elif graph_type == "Area":
                plt.fill_between(x, y, color='blue', alpha=0.5)
            elif graph_type == "Histogram":
                plt.hist(y, bins=len(y), color='blue', alpha=0.7)
            elif graph_type == "Pie":
                plt.pie(y, labels=x, colors=colors, autopct='%1.1f%%', startangle=90)
                plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
            elif graph_type == "Box":
                plt.boxplot(y)
                plt.xticks([1], [x_axis_title])  # Single box plot

            # Set labels and titles
            plt.xlabel(x_axis_title, color='white')
            plt.ylabel(y_axis_title, color='white')
            plt.title(graph_title, color='white')
            plt.xticks(color='white')
            plt.yticks(color='white')

            # Show the plot
            st.pyplot(plt)
    except ValueError:
        st.error("Please ensure Y values are numeric.")
