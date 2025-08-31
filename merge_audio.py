import os
from pydub import AudioSegment

# Folder with your audio files
INPUT_DIR = "audio"
OUTPUT_FILE = os.path.join(INPUT_DIR, "interview_merged.mp3")
SILENCE_MS = 300  # gap between lines (ms)

def main():
    files = sorted(f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".mp3"))
    if not files:
        print("No MP3 files found in 'audio/' folder.")
        return

    print("Merging these files:", files)

    merged = AudioSegment.silent(duration=0)
    gap = AudioSegment.silent(duration=SILENCE_MS)

    for f in files:
        seg = AudioSegment.from_mp3(os.path.join(INPUT_DIR, f))
        merged += seg + gap

    merged.export(OUTPUT_FILE, format="mp3")
    print("✅ Merged file saved as:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
