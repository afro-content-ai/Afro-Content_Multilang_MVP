from deep_translator import GoogleTranslator
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os

def create_content(text, target_lang="ar"):
    print("Translating text...")
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)

    print("Generating voice...")
    tts = gTTS(translated, lang=target_lang)
    tts.save("audio.mp3")

    print("Creating video...")
    # Create a 5-second video using a placeholder image
    clip = ImageClip("https://picsum.photos/640/360").set_duration(5)
    audio = AudioFileClip("audio.mp3")
    clip = clip.set_audio(audio)
    clip.write_videofile("output.mp4", fps=24)

    print("✅ Done! Created output.mp4 successfully.")

if __name__ == "__main__":
    create_content("Welcome to Afro Content AI, your multilingual content assistant.")
