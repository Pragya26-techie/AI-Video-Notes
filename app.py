# app.py
from utils import *

def generate_video_notes(video_url):
    video_id = extract_video_id(video_url)

    if not video_id:
        print("Invalid URL")
        return

    transcript = get_transcript(video_id)

    if "Error" in transcript:
        print(transcript)
        return

    chunks = chunk_text(transcript)[:15]

    notes = []

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        if summary.strip():
            notes.append(f"- {summary}")

    print("\n".join(notes))


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    generate_video_notes(url)