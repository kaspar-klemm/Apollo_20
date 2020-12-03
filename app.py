import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from Apollo_20.duplicate_detector import duplicate_detector
from Apollo_20.dl_model_predictor import image_categoriser
from Apollo_20.cosine_similarity import execute

print(dir())

st.markdown("""# Picture Recognition System
## Apollo_20
Welcome to your Storage Space Generator""")


if st.checkbox('interested in the Founders?'):
    st.write('''
        Kaspar Klemm, Nikolaus Lutterotti, Florian Immes, Timour Nour
        ''' )

if st.checkbox('interested in the Process?'):
    st.write('''This Application halps you to detect pictures you might no longer need.
    Your pictures will be scanned in three different Folders namely: Dublicates, Screenshots and similar pictures.
    None of the pictures will be deleted without your consent nor will your library be changed in any way.
    All we do is show you cases that could help you generate more storage space.
    All you have to do is grant us access to your library the rest will be done automatically.''')

if st.checkbox('Allow Access & choose Images'):
    st.set_option('deprecation.showfileUploaderEncoding', False)

    #multiple_files = st.file_uploader(
    #"Multiple File Uploader",
    #accept_multiple_files=True)

    #filenames = []
    #for file in multiple_files:
        #filenames.append(f"{file.name}")
        #image = file.read()
        #st.write(print(type(image)))
        #file_container = st.beta_expander(
        #f"File name: {file.name} ({file.size}b)")
        #file_container.write(file.getvalue())
        #st.write(print(filenames))

    folder_path = st.text_input("Please enter your folder here")

if st.button('Press to filter out duplicates'):
    st.balloons()
    st.write('''Your Images are being scanned for duplicates''')

    st.write(duplicate_detector(folder_path=folder_path))
    st.success('Images successfully scanned')

if st.button('Press to create folders with similar picutres'):

    st.write(execute(folder_path=folder_path))
    st.success('Images successfully scanned')

if st.button('Press to filter out screenshots and pictures of notes and documents'):

    st.write(image_categoriser(folder_path=folder_path))
    st.success('Images successfully scanned')
