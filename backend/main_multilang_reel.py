import os, time, random, requests
from gtts import gTTS
from deep_translator import GoogleTranslator
from moviepy.editor import *
from pathlib import Path

# === SETUP ===
OUTPUT = "Afro_Content_Reel.mp4"
PROMPT = "Create a 1-minute motivational content about success, written for Afro Content AI."
LANGS = {"en": "English", "ar": "Arabic"}

# === 1. Generate text (can replace this with AI API) ===
english_text = "Success is not about speed, it's about consistency. Every small step brings you closer to greatness."
arabic_text = GoogleTranslator(source='en', target='ar').translate(english_text)

print("English:", english_text)
print("Arabic:", arabic_text)

# === 2. Convert both texts to speech ===
tts_en = gTTS(english_text, lang='en')
tts_en.save("voice_en.mp3")

tts_ar = gTTS(arabic_text, lang='ar')
tts_ar.save("voice_ar.mp3")

# === 3. Merge voices sequentially ===
audio_clips = [AudioFileClip("voice_en.mp3"), AudioFileClip("voice_ar.mp3")]
final_audio = concatenate_audioclips(audio_clips)
final_audio.write_audiofile("voice_mix.mp3")

# === 4. Pick random background images ===
# You can replace these URLs with your own brand visuals
images = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1483721310020-03333e577078"
]

clips = []
for i, url in enumerate(images):
    img_path = f"img{i}.jpg"
    open(img_path, "wb").write(requests.get(url).content)
    clip = ImageClip(img_path).set_duration(final_audio.duration / len(images))
    clips.append(clip)

# === 5. Merge visuals and add audio ===
video = concatenate_videoclips(clips, method="compose")
video = video.set_audio(AudioFileClip("voice_mix.mp3"))

# Add simple subtitles
txt_clip = TextClip(
    f"{english_text}\n\n{arabic_text}",
    fontsize=40, color='white', size=video.size, method='caption', bg_color='black'
).set_duration(video.duration).set_position(("center", "bottom"))

final = CompositeVideoClip([video, txt_clip])
final.write_videofile(OUTPUT, fps=24)

print("✅ Done! Created multilingual reel:", OUTPUT)
