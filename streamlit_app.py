import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Portföljanalys',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)


st.title("Portföljanalys")
