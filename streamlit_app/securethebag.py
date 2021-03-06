import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports
from multipage import MultiPage
from pages import home, data_story, about, form, resources # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Secure the Bag: Diagnosing Food Insecurity in California")


# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("California Food Security", data_story.app)
app.add_page("Food Security Diagnostic Quiz", form.app)
app.add_page("Resources", resources.app)
app.add_page("About Us", about.app)



# The main app
app.run()
