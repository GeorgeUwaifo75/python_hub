import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set up the plot
ypoints = np.array([3, 8, 1, 10])

# Create figure and axis
fig, ax = plt.subplots()
ax.plot(ypoints, linestyle='dotted')

# Optional: Add labels
ax.set_title('Dotted Line Plot')
ax.set_xlabel('Index')
ax.set_ylabel('Value')

# Display in Streamlit
st.pyplot(fig)

# Optional: Add Streamlit header
st.header('Matplotlib Plot in Streamlit')
