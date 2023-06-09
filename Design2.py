import streamlit as st
from utilities import get_yt, transcribe_yt

# Center align the search bar
st.markdown('<h1 style="text-align: center;">📝 TFF Moderation App</h1>', unsafe_allow_html=True)

# Create a container for the output
output_container = st.empty()

# Sidebar
st.sidebar.header('Input parameter')

with st.sidebar.form(key='my_form'):
    URL = st.text_input('Enter URL of YouTube video:')
    submit_button = st.form_submit_button(label='Go')

# Run custom functions if URL is entered 
if submit_button:
    with st.spinner('Generating output...'):
        get_yt(URL)
        transcribe_yt()

    # Display the output container with the download button
    with open("transcription.zip", "rb") as zip_download:
        output_container.markdown('## Output')
        btn = st.download_button(
            label="Download ZIP",
            data=zip_download,
            file_name="transcription.zip",
            mime="application/zip"
        )

with st.sidebar.expander('Example URL'):
    st.code('https://www.youtube.com/watch?v=twG4mr6Jov0')
