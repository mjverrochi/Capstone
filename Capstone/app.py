from tensorflow.keras.models import load_model
import streamlit as st
import PIL

st.title('image classification of waste items')

st.text('is it biodegradable or non-biodegradable?')

model = load_model('models/waste_saved/')

# st.write(type(model))

img = st.file_uploader(label='Attach Image Here:')

predicted_class = model.predict([img])[0]

st.write(f"Your image is {predicted_class}!")