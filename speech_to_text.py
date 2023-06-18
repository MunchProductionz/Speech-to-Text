import whisper
import openai
from languages import languages
from api_keys import keys

def speech_to_text(audio_filename, filetype="mp3", model="whisper-1", response_format="text", language="en"):
    
    # Set the OpenAI API key
    openai.api_key = keys["OPENAI_API_KEY"]
    
    # Set the path to the audio file and get the language code
    audio_filepath = "audio/" + audio_filename + "." + filetype
    language = languages[language.lower()]
    
    # Transcribe the audio file using the OpenAI API
    with open(audio_filepath, "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = model,
        response_format=response_format,
        language=language
    )
    print(transcript)
    
speech_to_text("test")