import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Code test hub")
st.write("Version:", matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
