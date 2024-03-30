from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta
from pytube import Playlist
from pytube import YouTube


import sys
import json

def convertSecondsToTime(seconds_string):
  raw_seconds = int(seconds_string)
  return timedelta(seconds=raw_seconds)

def writeTranscriptToFile(filename, video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    filename = filename.replace('?', '')
    
    with open(filename+".txt", "w", encoding="utf-8") as f:
        for line in transcript: 
            f.write("{} {}\n".format(convertSecondsToTime(line['start']), line['text']))   


if (len(sys.argv) != 2):
  print ('Invalid number of parameters')
  print('usage:  GetTranscripts <youtube url>')
  exit()

yt = YouTube(sys.argv[1])

writeTranscriptToFile(yt.title, yt.video_id)

