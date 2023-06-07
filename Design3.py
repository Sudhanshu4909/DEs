import streamlit as st

# Set page layout to centered
st.set_page_config(layout="centered")

# Page title
st.title("📝 TFF Moderation App")

# Centered input parameter section
st.header("Input Parameter")

with st.form(key='my_form'):
    # URL input
    URL = st.text_input('Enter URL of YouTube video')
    submit_button = st.form_submit_button(label='Go')

# Main content
if submit_button:
    # Display processing message
    st.info('Processing...')

    # Display results
    st.header('Transcription Results')

    # Display text
    with st.expander('Transcribed Text'):
        st.success("This is a sample transcribed text.")

    # Download button for the transcribed text
    with st.expander('Download Transcribed Text'):
        st.download_button(label='Download', data="Sample Text", file_name='yt.txt')

    # Display content safety labels
    with st.expander('Content Safety Labels'):
        st.json({"label": "Safe"})

    # Download button for the content safety labels
    with st.expander('Download Content Safety Labels'):
        st.download_button(label='Download', data='{"label": "Safe"}', file_name='yt.json')

