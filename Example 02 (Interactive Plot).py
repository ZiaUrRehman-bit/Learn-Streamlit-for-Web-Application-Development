import streamlit as st
import plotly.express as px

st.title("Interactive Plot Example")

# User input
x = st.slider("Select a range for x:", 0, 10, (3, 7))

# Create a dynamic plot
fig = px.line(x=list(range(x[0], x[1] + 1)), y=[x**2 for x in range(x[0], x[1] + 1)])
st.plotly_chart(fig)
