import streamlit as st
import numpy as np
import pandas as pd


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
    #uploaded_files = st.file_uploader("Multiple File Uploader", type="png", "jpg", "jpeg", accept_multiple_files = True)

    #if uploaded_file is not None:
        #data = pd.read_csv(uploaded_file)
        #st.write(data)


    folder_path = st.text_input("Enter folder path where your pictures are stored")

if st.button(' 🎈🎈Start Scan 🎈🎈'):
    st.balloons()
    print ('Access granted')
    st.write('''Your Images are being scanned. This may take up to 2 minutes
    depending on the amount of Data. Lean back and we'll do the magic for you.''')
    st.write(duplicate_detector(folder_path))

if st.checkbox('Show progress bar'):
    import time

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Sacnning {i+1} %')
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
