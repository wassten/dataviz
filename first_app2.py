import streamlit as st
import numpy as np
import pandas as pd 
import time
import matplotlib.pyplot as plt 
import seaborn as sns
from functools import wraps
from time import time

# Create an empty dataframe
data = pd.DataFrame(columns=["Random"])
st.text("Original dataframe")

# with every interaction, the script runs from top to bottom
# resulting in the empty dataframe
st.dataframe(data) 

# random value to append; could be a num_input widget if you want
random_value = np.random.randn()

if st.button("Append random value"):
    st.text("Updated dataframe")
    data = data.append({'Random': 2}, ignore_index=True)
    data = data.append({'Random': 4}, ignore_index=True)

# still empty as state is not persisted
st.text("Original dataframe")
st.dataframe(data)



st.title('Test')

