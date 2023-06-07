import streamlit as st

# Page title and logo
st.title("Audio Moderation App")
logo = "logo.png"  # Replace with your actual logo file name
st.image(logo, use_column_width=True)

# Main content
st.header("Upload Audio File")
file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

if file is not None:
    # Display audio player
    st.audio(file)

    # Moderation options
    st.subheader("Moderation Options")
    st.checkbox("Transcribe Audio")
    st.checkbox("Detect Profanity")
    st.checkbox("Identify Speaker")

    # Button to start moderation
    st.button("Start Moderation")
