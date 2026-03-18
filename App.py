from dotenv import load_dotenv
import os 
from elevenlabs.client import ElevenLabs

# Load API key
load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    print("API key not found")
    exit()

client = ElevenLabs(api_key=api_key)

# Voice IDs
VOICE_ARIA = "EXAVITQu4vr4xnSDxMaL"
VOICE_WEBB = "ErXwobaYiN019PkySvjV"
VOICE_NARRATOR = "EXAVITQu4vr4xnSDxMaL"

# Read script
with open("Science Fiction.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Generating conversation audio...")

with open("final_output.mp3", "wb") as output_file:

    for line in lines:
        line = line.strip()

        if not line or line == "END":
            continue

        if line.startswith("ARIA:"):
            text = line.replace("ARIA:", "").strip()
            voice = VOICE_ARIA

        elif line.startswith("Captain Webb:"):
            text = line.replace("Captain Webb:", "").strip()   
            voice = VOICE_WEBB

        else:
            text = line
            voice = VOICE_NARRATOR

        print(f"Processing: {text[:40]}...")

        audio_stream = client.text_to_speech.convert(
            voice_id=voice,
            model_id="eleven_multilingual_v2",
            text=text
        )

        for chunk in audio_stream:
            output_file.write(chunk)

print("✅ Conversation audio generated: final_output.mp3")
