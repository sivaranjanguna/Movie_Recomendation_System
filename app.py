import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
import io

# ----------------------------------------------------
# Page Setup (Dark Netflix Theme)
# ----------------------------------------------------
st.set_page_config(page_title="Netflix Movie Recommendation", layout="wide")

st.markdown("""
    <style>
        body { background-color: #0d0d0d; }
        .title { 
            font-size: 46px; 
            font-weight: 800; 
            color: #E50914; 
            text-align:center; 
            margin-top: -40px;
            text-shadow: 0px 0px 20px rgba(229,9,20,0.6);
        }
        .movie-card img {
            border
