import os
from deep_translator import GoogleTranslator
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip

# Example basic code for AI content
def create_content(text, language="en"):
    translated = GoogleTranslator(source='auto', target=language).translate(text)
    tts = gTTS(translated, lang=language)
    tts.save("audio.mp3")
    print("✅ Audio created successfully!")

if __name__ == "__main__":
    create_content("Welcome to Afro Content AI!")
