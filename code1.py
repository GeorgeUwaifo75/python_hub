import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title for the Streamlit app
st.title("Car Age vs. Speed Scatter Plot")

# Data for Day 1
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Data for Day 2
x2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Day 1 (blue circles)
ax.scatter(x1, y1, color='blue', label='Day 1', alpha=0.7)

# Plot Day 2 (red triangles)
ax.scatter(x2, y2, color='red', marker='^', label='Day 2', alpha=0.7)

# Customize the plot
ax.set_xlabel("Car Age")
ax.set_ylabel("Speed (km/h)")
ax.set_title("Comparison of Car Age vs. Speed (Day 1 vs. Day 2)")
ax.legend()  # Show legend
ax.grid(True, linestyle='--', alpha=0.5)  # Add grid

# Display the plot in Streamlit
st.pyplot(fig)

# Optional: Show raw data in an expandable section
with st.expander("Show Raw Data"):
    st.write("**Day 1 Data (Age, Speed):**")
    st.write(list(zip(x1, y1)))
    
    st.write("**Day 2 Data (Age, Speed):**")
    st.write(list(zip(x2, y2)))
