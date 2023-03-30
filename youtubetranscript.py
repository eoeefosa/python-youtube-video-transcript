# import the library
from youtube_transcript_api import YouTubeTranscriptApi

# get the video id from the url
example_url = "https://www.youtube.com/watch?v=b-OwzSvpKSY"
video_id = example_url.split("=")[1].split("&")[0]

# get the transcript as a list of dictionaries
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# write the transcript to a text file
with open("transcript.txt", "w") as f:
    for line in transcript:
        f.write(line["text"] + "\n")
