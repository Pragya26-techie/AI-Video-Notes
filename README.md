## AI Video Notes Generator
 An NLP-bsed project that automatically generates structured notes from YouTube videos using Transfromers models.

## Overview
This project extracts transcripts from YouTube videos and converts them into concise,meaningful bullet-point notes.It is designed to handle long videos efficiently using chunk-based processing and works best with English transcripts.

## Features:
- Extracts transcript from youtube videos
- Handles long videos using chunking
- Generates summaries using Transformer model(FLAN-T5)
- Basic multiingual handling (Hindi->English translation fallback)
- optimized for performance by limiting chunk processing

## Tech Stack
- Python
- PyTorch
- Hugging Face Transformers('Google/flan-t5-base)
- YouTube Transcript API

## How It Works
1.Extract video ID from YOuTube URL
2.Fetch transcript using API
3.Split transcript into smaller chunks
4.Generate summary for each chunk using Transformer model
5.Combine summaries into structured notes

## Project Structure
ai-video-notes/
- app.py #Main execution script
- utils.py # Helper functions
- reuirements.txt
- README.md

## How to RUn
### 1.Install dependemcies
pip install -r requirements.txt

### 2.Run the application
python app.py

### 3.Enter YouTube URL when prompted
---

## Challenges Faced
- Transcript availability varies across videos
- YouTube API rate limiting (IP blocking after multiple requests)
- Poor Summarization for non-english transcripts
- Handling long videos efficiently

## Solutions Implemented
- Added transcript selection fallback
- Limited chunk processing to reduce computation
- Improved prompt design for better summaries
- Added basic error handling for API failures

## Limitations
- work best for English videos
- Dependent on YouTube transcript availability
- Summary quality depends on model capability

## Future Improvements
- Use Whisper for transcript generation(remove API dependency)
- Build web interface using Streamlit
- Improve summary quality advanced models(BART,GPT)
- Add structured notes(heading + sections)

## Learnings
- Handling real-world API limitation
- Working with NLP transformer models
- Managing long text using chunking
- Debugging and optimizing ML pipelines

## Author
**PRAGYA**
------
