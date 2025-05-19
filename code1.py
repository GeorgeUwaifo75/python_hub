import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Code test hub")

# Set up the plot
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

fig, ax = plt.subplots()
ax.plot(xpoints, ypoints)

# Display the plot in Streamlit
st.pyplot(fig)

# Optional: Add a title
st.title('Simple Line Plot')
