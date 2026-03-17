import streamlit as st
import os

from modules.audio_extractor import extract_audio
from modules.speech_to_text import speech_to_text
from modules.translator import translate_text
from modules.text_to_speech import text_to_speech
from modules.video_dubber import dub_video

# ✅ Hide Streamlit UI
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ✅ Page Config
st.set_page_config(
    page_title="AI Video Dubbing System",
    page_icon="🎬",
    layout="wide"
)

# ✅ Create temp folder safely
if not os.path.exists("temp"):
    os.makedirs("temp")

# ✅ Title
st.markdown("<h1 style='text-align:center;'>🎬 AI Automatic Video Dubbing</h1>", unsafe_allow_html=True)

st.sidebar.header("⚙ Language Settings")

language = st.sidebar.selectbox(
    "Select Target Language",
    ["Konkani", "Maithili"]
)

# ✅ Upload
uploaded_file = st.file_uploader(
    "📤 Upload Educational Video",
    type=["mp4", "mov", "avi"]
)

col1, col2 = st.columns(2)

if uploaded_file is not None:

    input_path = "temp/input_video.mp4"

    # save uploaded video
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    col1.subheader("🎥 Original Video")
    col1.video(input_path)

    if st.button("🚀 Start Dubbing"):

        with st.spinner("⏳ Processing... Please wait"):

            progress = st.progress(0)

            # Step 1: Audio Extraction
            st.info("🔊 Extracting Audio...")
            audio = extract_audio(input_path)
            progress.progress(20)

            # Step 2: Speech to Text
            st.info("🧠 Speech to Text...")
            text = speech_to_text(audio)
            progress.progress(40)

            st.text_area("📄 Original Text", text)

            # Step 3: Translation
            st.info("🌐 Translating...")
            translated = translate_text(text, language)
            progress.progress(60)

            st.text_area("📝 Translated Text", translated)

            # Step 4: Subtitle Preview
            st.subheader("📺 Subtitles Preview")
            st.write(translated)

            # Step 5: Text to Speech
            st.info("🎙 Generating Voice...")
            voice = text_to_speech(translated)
            progress.progress(80)

            # Step 6: Video Dubbing
            st.info("🎬 Creating Dubbed Video...")
            output = dub_video(input_path, voice)
            progress.progress(100)

        col2.subheader("🎬 Dubbed Video")
        col2.video(output)

        st.success("✅ Dubbing Completed!")

        # Download
        with open(output, "rb") as f:
            st.download_button(
                "⬇ Download Dubbed Video",
                f,
                file_name="dubbed_video.mp4"
            )

# ✅ Footer
st.markdown("""
<hr>
<p style='text-align:center'>
AI Video Dubbing System | Final Year Project
</p>
""", unsafe_allow_html=True)