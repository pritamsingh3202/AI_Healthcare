# step 1a: steup text to speech-TTS-model gTTS

from dotenv import load_dotenv
load_dotenv()
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"
    
    audioobj = gTTS(text=input_text,
                    lang=language,
                    slow=False
                )
    audioobj.save(output_filepath)
    
    
input_text= "Hello Pritam, I am AI Voice Assistent. How can I assist you today?"

# text_to_speech_with_gtts_old(input_text= input_text, output_filepath="output.mp3")


# step 2: steup speech-TTS-model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY= os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client= ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio= client.generate(
        text=input_text,
        voice="Alice",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
        
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")




# step 3: Use Model for Text output to voice


import subprocess 
import platform


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    
    audioobj = gTTS(text=input_text,
                    lang=language,
                    slow=False
                )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'])  # FIXED LINE
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
input_text = "Hello Pritam, I am AI Voice Assistent. How can I assist you today?"

# text_to_speech_with_gtts(input_text=input_text, output_filepath="output.mp3")



def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Alice",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'])  # FIXED LINE
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3")


