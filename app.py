import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import cv2
import numpy as np
from tensorflow.keras.models import load_model

st.title('image classification of waste items')

st.text('is it biodegradable or non-biodegradable?')

# loading model
model = load_model('models/waste_saved')

# creating file uploader
img_data = st.file_uploader('Attach Image Here:', type=['jpg'])

def import_and_predict(image_data, model):

    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

if img_data is None:
    st.text('Please upload an image file')
else:
    image = Image.open(img_data)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ['Biodegradeable', 'Non-Biodegradeable']
    string = "The item in this image is most likely "+class_names[np.argmax(predictions)]
    st.success(string)
