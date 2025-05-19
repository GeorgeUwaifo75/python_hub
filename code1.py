import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

# Plot 1
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
ax1.plot(x1, y1)
ax1.set_title('Plot 1')

# Plot 2
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
ax2.plot(x2, y2)
ax2.set_title('Plot 2')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Optional: Add a title to the Streamlit app
st.header('Side-by-Side Plots')
