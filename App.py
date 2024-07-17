import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
#A singl efunction to do all these steps
st.sidebar.success("Select what you want to check SMS or email")
st.title('This is an Application to segegate between Spam and Not spam messages!')

st.text("Choose for SMS or Email spam detection ➡️")