import streamlit as st
from docutils.nodes import contact
from streamlit_option_menu import option_menu
import home
import dashboard
import about
import contact
# Set page config at the top
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Dashboard","Contact Us"],
                           icons=['house', 'bar-chart-line','envelope'], menu_icon="app-indicator", default_index=0)

if selected == "Home":
    home.display()
elif selected == "Dashboard":
    dashboard.display()
elif selected == "Contact Us":
    contact.display()