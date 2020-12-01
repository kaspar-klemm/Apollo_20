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

st.sidebar.markdown(f"""
    # Header Resizer
    """)

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

    #image_filepath = st.text_input("Please enter filepath where pictures are stored")
    #uploaded_files = st.file_uploader("Multiple File Uploader", type="png", accept_multiple_files = True)

    #if uploaded_files is not None:
        #save_path = st.write(os.getcwd())
        #for files in uploaded_files:
            #complete_name = save_path + files
            #file1 = open(completeName)
            #file1.close()

    folder_path = "IMAGES"

if st.button('Press to filter out duplicates'):
    st.balloons()
    st.write('''Your Images are being scanned for duplicates''')
    st.write(duplicate_detector(folder_path=folder_path))

if st.button('Press to filter out screenshots and pictures of notes and documents'):
    st.write(image_categoriser(folder_path=folder_path))

if st.button('Press to create folders with similar picutres'):
    st.write(execute(folder_path=folder_path))

if st.checkbox('Show progress bar'):
    import time

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Scanning {i+1} %')
        bar.progress(i + 1)
        time.sleep(0.1)

    if st.success('Images successfully scanned'):
        @st.cache
        def get_histo():
            print('get_histo called')
            df = pd.DataFrame(
                    np.random.randn(100, 1),
                    columns=['a']
                )

            return np.histogram(
                df.a, bins=3)[0]

        hist_values = get_histo()

        st.bar_chart(hist_values)

@st.cache
def get_select_box_data():
    print('get_select_box_data called')
    return pd.DataFrame({
          'Category': ("Duplicates", "Screenshots", "Similar Pictures"),
          'Number of pictures detected': ("n"),
          'Used Data Capacity': ("n MB")
        })

df = get_select_box_data()

option = st.selectbox('Select a category to filter', df['Category'])

filtered_df = df[df['Category'] == option]

st.write(filtered_df)
