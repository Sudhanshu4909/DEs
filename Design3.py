import streamlit as st
from pytube import YouTube
from utilities import get_yt, transcribe_yt

# Page title
st.title("📝 TFF Moderation App")

# Sidebar
st.sidebar.title("Input Parameter")

with st.sidebar.form(key='my_form'):
    # URL input
    URL = st.text_input('Enter URL of YouTube video')
    submit_button = st.form_submit_button(label='Go')

# Main content
if submit_button:
    # Display processing message
    st.info('Processing...')

    # Download and transcribe YouTube video
    get_yt(URL)
    transcribe_yt()

    # Display results
    st.header('Transcription Results')

    # Display text
    with st.expander('Transcribed Text'):
        with open("yt.txt", "r") as txt_file:
            text = txt_file.read()
            st.success(text)

    # Download button for the transcribed text
    with st.expander('Download Transcribed Text'):
        with open("yt.txt", "rb") as txt_file:
            st.download_button(label='Download', data=txt_file, file_name='yt.txt')

    # Display content safety labels
    with st.expander('Content Safety Labels'):
        with open("yt.json", "r") as json_file:
            content_safety_labels = json_file.read()
            st.json(content_safety_labels)

    # Download button for the content safety labels
    with st.expander('Download Content Safety Labels'):
        with open("yt.json", "rb") as json_file:
            st.download_button(label='Download', data=json_file, file_name='yt.json')
