# YouTube Transcript Downloader

## Description

This Python script allows users to download the transcript of a YouTube video and save it as a text file with timestamps. It extracts the transcript using the `youtube_transcript_api` library and formats it with minute and second markers for readability.

## Features

- Extracts transcripts from YouTube videos.
- Formats timestamps in `[MM:SS]` format.
- Saves the transcript to a specified output file.
- Simple command-line usage.

## Prerequisites

Make sure you have Python installed. You also need to install the required dependency:

```sh
pip3 install youtube-transcript-api
```

## Usage

Run the script using the following command:

```sh
python3 trandl.py -u <YouTube_URL> -o <output_file>
```

### Example:

```sh
python3 trandl.py -u https://www.youtube.com/watch?v=something -o output.txt
```

This will fetch the transcript of the given YouTube video and save it in `output.txt`.

## Script Breakdown

1. Extracts the video ID from the YouTube URL.
2. Fetches the transcript using `youtube_transcript_api`.
3. Formats the transcript with timestamps.
4. Saves the formatted transcript to a text file.

## Error Handling

- If the provided URL is invalid, an error message will be displayed.
- If no transcript is available for the video, the script will notify the user.

## License

This project is open-source and free to use.

## Author

Developed by Htet Naing Lin
