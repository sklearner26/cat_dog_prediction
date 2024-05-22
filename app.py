import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pickle

from keras.models import load_model
model = load_model("cat_model1.pkl")

#model=pickle.load(open("cat_model1.pkl",'rb'))
st.title(":red[CAT Vs DOG PREDICTION]")

file=st.file_uploader("Upload a image for prediction",type=['jpg','png','jpeg'])

#prediction function
def prediction(file):
         img=Image.open(file)
         image=np.array(img)
         img=plt.resize(image,(256,256))
         if img.shape!=(1,256,256,3):
          st.write("Give Another Image")
          exit()
         img=img.reshape((1,256,256,3))
         pred=model.predict(img)
         return pred

if file is None:
  st.write(":blue[Please upload image for predicion]")
else:
    img=Image.open(file)
    st.image(img)
    bt=st.button('predict')
    if bt:
     pred=prediction(file)
     if pred==0:
       st.success("It is a  Cat")
     elif pred==1:
       st.success("It is a Dog")
     else:
       st.warning("Please provide another image")

for i in range(10):
  st.text(" ")

option = st.selectbox(
    'Give a Feedback by choose below option',
    ('Right Prediction','Wrong Prediction'),index=None,
   placeholder="Select any option...")
if option=='Right Prediction':
  st.success('Thankyou for feedback')
  st.balloons()
elif option=='Wrong Prediction':
  st.warning("Sorry for the mistake")
  st.warning("I try to improve it")
