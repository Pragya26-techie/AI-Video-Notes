from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound
import re
import torch
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

#check if we have a GPU(CUDA) available to speed things up
device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "google/flan-t5-base"

#Load the tokenizer(translate text into numbers)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# Load the model(the neural network) and move it to the GPU/CPU
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

def extract_video_id(url):
  """Extracts video ID from different YouTube URL formats."""
  # we use Regex to hunt for the 11-character ID after 'v=' or 'youtu.be/'
  match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})",url)
  return match.group(1) if match else None

def get_transcript(video_id):
  """Fetch transcript using the NEW API format."""
  try:
     api = YouTubeTranscriptApi()
    #  transcript_list = api.list(video_id)
    #  print("Available transcripts:", transcript_list)
    #  try:
    #     transcript = transcript_list.find_manually_created_transcript(['en'])
    #     print("using manual English transcript")
    #  except:
    #    try:
    #      transcript = transcript_list.find_generated_transcript(['en'])
    #      print("Using auto English transcript")
    #    except:
    #     # step 3: fallback->Hindi
    #     transcript = transcript_list.find_generated_transcript(['hi'])
    #     print("Using Hindi transcript -> translating to English")
    #     transcript = transcript.translate('en')

     transcript = api.fetch(video_id)
    # we join list into  a single long string of text
     return " ".join([t.text for t in transcript])
  except TranscriptsDisabled:
    return "Error: Transcript are disabled for this video"
  except NoTranscriptFound:
    return "Error: No transcript found for this video."
  except Exception as e:
    return f"Error:{str(e)}"
  
def chunk_text(text,chunk_size=400):
  sentences = text.split(".")
  chunks,current_chunk = [],""

  for sentence in sentences:
    # Check if adding the next sentence exceeds our limit
    if len(current_chunk) + len(sentence) < chunk_size:
      current_chunk += sentence + ". "
    else:
      # if full,seal the chunk and start a new one
      chunks.append(current_chunk.strip())
      current_chunk = sentence + "."

  if current_chunk:
    chunks.append(current_chunk.strip())

  return chunks
def summarize_chunk(text_chunk):
  # we give the model a specific instruction(prompt engineering)
  prompt = f"""
  Summarize the following text clearly:
  {text_chunk}
  """

 #convert text to tensor numbers(inputs)
  inputs = tokenizer(
      prompt,
      return_tensors="pt",
      truncation=True,
      max_length=1024
  ).to(device)

 # Generate the summary
  summary_ids=model.generate(
    **inputs,
    max_new_tokens=120, #max length of summary
    num_beams=4, #Look for the  4 best apths
    length_penalty=1.0,# Balance between short and long
    early_stopping=True
)

# Decode back to text
  return tokenizer.decode(summary_ids[0], skip_special_tokens=True)