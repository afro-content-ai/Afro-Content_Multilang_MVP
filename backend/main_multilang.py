# main_multilang.py
# ✨ Afro Content Multilang MVP — by Afro Content AI
# Generates AI videos with English/Arabic text, translation, captions, and voice

import openai
from gtts import gTTS
from moviepy.editor import *
from deep_translator import GoogleTranslator
import os

# ✅ STEP 1 — SETUP YOUR OPENAI KEY
openai.api_key = os.getenv("OPENAI_API_KEY") or "paste-your-api-key-here"

# ✅ STEP 2 — ENTER YOUR TEXT
text_en = "Welcome to Afro Content AI — your intelligent multilingual content creator. We bring ideas to life in English and Arabic."

# ✅ STEP 3 — TRANSLATE TO ARABIC
text_ar = GoogleTranslator(source='en', target='ar').translate(text_en)

print("English:", text_en)
print("Arabic:", text_ar)

# ✅ STEP 4 — VOICE GENERATION
voice_en = gTTS(text=text_en, lang='en')
voice_en.save("voice_en.mp3")

voice_ar = gTTS(text=text_ar, lang='ar')
voice_ar.save("voice_ar.mp3")

# ✅ STEP 5 — COMBINE AUDIO
final_audio = AudioFileClip("voice_en.mp3").fx(afx.audio_fadein, 1)
final_audio = concatenate_audioclips([
    AudioFileClip("voice_en.mp3"),
    AudioFileClip("voice_ar.mp3")
])

# ✅ STEP 6 — CREATE VIDEO BACKGROUND
clip = ColorClip(size=(1280, 720), color=(15, 15, 15), duration=final_audio.duration)

# ✅ STEP 7 — ADD TEXT CAPTIONS
txt_en = TextClip(text_en, fontsize=45, color='white', size=(1200, None), method='caption').set_position('center').set_duration(final_audio.duration/2)
txt_ar = TextClip(text_ar, fontsize=50, font='Arial', color='yellow', size=(1200, None), method='caption').set_position('center').set_start(final_audio.duration/2).set_duration(final_audio.duration/2)

# ✅ STEP 8 — COMBINE ALL
video = CompositeVideoClip([clip, txt_en, txt_ar])
video = video.set_audio(final_audio)

# ✅ STEP 9 — EXPORT
output_path = "Afro_Content_Multilang_Output.mp4"
video.write_videofile(output_path, fps=24)

print("✅ Done! Created multilingual video:", output_path)
