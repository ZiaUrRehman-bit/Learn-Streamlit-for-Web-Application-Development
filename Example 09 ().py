import streamlit as st
import folium

st.title("Map Visualization")

# Create a map
m = folium.Map(location=[51.5074, 0.1278], zoom_start=10)

# Add markers
folium.Marker([51.5074, 0.1278], tooltip="London").add_to(m)
folium.Marker([48.8566, 2.3522], tooltip="Paris").add_to(m)

# Display the map
st.write("Interactive Map:")
st.write(m)
