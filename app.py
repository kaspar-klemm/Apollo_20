import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from Apollo_20.duplicate_detector import duplicate_detector
from Apollo_20.dl_model_predictor import image_categoriser
from Apollo_20.cosine_similarity import execute

print(dir())

st.markdown("""# Apollo
## Picture Recognition System
Welcome to your Storage Space Generator""")


if st.checkbox('Interested in the Founders?'):
    st.write('''
        Kaspar Klemm, Nikolaus Lutterotti, Florian Immes, Timour Nour
        ''' )

if st.checkbox('Interested in the Process?'):
    st.write('''This Application helps you to detect pictures you might no longer need.
    Your pictures will be scanned in three different folders namely: Duplicates, Screenshots and similar pictures.
    None of the pictures will be deleted without your consent nor will your library be changed in any way.
    All we do is show you which pictures you might not need and help you generate more storage space.
    All you have to do is grant us access to your library the rest will be done automatically.''')

if st.checkbox('Allow Access & choose Images'):
    st.set_option('deprecation.showfileUploaderEncoding', False)

    folder_path = st.text_input("Please enter your folder here")

if st.button('Press to filter out duplicates'):
    st.balloons()
    st.write('''Your Images are being scanned for duplicates''')

    st.write(duplicate_detector(folder_path=folder_path))
    st.success('Images successfully scanned for duplicates. Pictures have been placed in the duplicates folder')

if st.button('Press to filter out screenshots and pictures of notes and documents'):
    st.balloons()
    st.write('''Your Images are being scanned for screenshots and notes/documents''')

    st.write(image_categoriser(folder_path=folder_path))
    st.success('Images successfully scanned. Pictures have been placed in the screenshots and notes folders')

if st.button('Press to create folders with similar picutres'):
    st.balloons()
    st.write('''Your Images are being scanned for similar pictures''')

    st.write(execute(folder_path=folder_path))
    st.success('Images successfully scanned for similar pictures. Pictures have been placed in the similar pictures folder')

