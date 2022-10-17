import pickle
import streamlit as st

st.title('waste: biodegradable or non-biodegradable?')

with open('cnn.waste', 'rb') as pickle_in:
    model = pickle.dump(model, pickle_in)