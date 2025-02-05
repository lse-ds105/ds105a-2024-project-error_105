import streamlit as st
import streamlit.components.v1 as components

# Set the page title and layout
st.set_page_config(page_title="Pokémon Biomes", layout="wide")

# Title Section
st.title("🌍 Where Would Pokémon Stay in the Real World?")
st.image("https://i.imgur.com/E6Nluee.gif", caption="Explore the habitats of Pokémon!", use_column_width=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Introduction", "Goals", "Interactive Map", "Search Pokémon", "Conclusion"])

# Introduction Section
