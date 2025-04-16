import os
import streamlit as st
import tempfile

from brain_doc import encode_img, analyze_img_with_query
from voice_patient import record_audio, transcribe_audio
from ai_voice import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AI Doctor with Vision and Voice", layout="centered")

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

st.title("AI Doctor with Vision and Voice")
st.markdown("Upload a voice message and a medical image to get an AI-powered response from your AI Doctor.")

# File uploaders
audio_file = st.file_uploader("Upload a voice message (MP3/WAV)", type=["mp3", "wav"])
image_file = st.file_uploader("Upload a medical image", type=["jpg", "jpeg", "png"])

if st.button("Analyze"):
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_audio:
            tmp_audio.write(audio_file.read())
            tmp_audio_path = tmp_audio.name

        with st.spinner("Transcribing audio..."):
            stt_output = transcribe_audio(
                GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                audio_filepath=tmp_audio_path,
                stt_model="whisper-large-v3"
            )
            st.success("Transcription complete.")
            st.markdown("**Transcribed Text:**")
            st.text(stt_output)
    else:
        st.warning("Please upload an audio file.")
        st.stop()

    if image_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
            tmp_img.write(image_file.read())
            tmp_img_path = tmp_img.name

        with st.spinner("Analyzing image and generating doctor response..."):
            doctor_response = analyze_img_with_query(
                query=system_prompt + stt_output,
                image=encode_img(tmp_img_path),
                model="meta-llama/llama-4-maverick-17b-128e-instruct"
            )
            st.success("Doctor's response generated.")
            st.markdown("**Doctor's Advice:**")
            st.text(doctor_response)

        with st.spinner("Converting to voice..."):
            audio_output = text_to_speech_with_elevenlabs(
                input_text=doctor_response,
                output_filepath="final.mp3"
            )
            st.audio("final.mp3", format="audio/mp3")
    else:
        st.warning("Please upload a medical image.")
