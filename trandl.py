import argparse
import os
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from a YouTube URL."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_transcript(video_id):
    """Fetch transcript from YouTube."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def format_transcript(transcript):
    """Format transcript with timestamps."""
    formatted = []
    for entry in transcript:
        minutes = int(entry['start'] // 60)
        seconds = int(entry['start'] % 60)
        timestamp = f"[{minutes:02}:{seconds:02}]"
        formatted.append(f"{timestamp} {entry['text']}")
    return "\n".join(formatted)

def save_to_file(content, output_file):
    """Save formatted transcript to a file."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="Download YouTube transcript.")
    parser.add_argument("-u", "--url", required=True, help="YouTube video URL")
    parser.add_argument("-o", "--output", required=True, help="Output file name")
    args = parser.parse_args()
    
    video_id = get_video_id(args.url)
    if not video_id:
        print("Invalid YouTube URL.")
        return
    
    transcript = fetch_transcript(video_id)
    if not transcript:
        print("Could not fetch transcript.")
        return
    
    formatted_transcript = format_transcript(transcript)
    save_to_file(formatted_transcript, args.output)
    print(f"Transcript saved to {args.output}")

if __name__ == "__main__":
    main()
