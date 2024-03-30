# Getting Started #
This is a guide for using the python script in this folder to download transcripts from the videos in a YouTube playlist.
## Installation
If you don’t have Python, you will need to install it from here: [Download Python](https://www.python.org/downloads/)
## Modules
You will need a couple of third party modules to make this work:
###Pytube

This module will let us get the playlist and related videos. To install, run the following command line:

```> py -m pip install pytube```
### Youtube-transcript-api

This module will let us retrieve the transcript from a YouTube video. To install, run the following command line: 

```> py -m pip install youtube-transcript-api ```
# Program
The program is as follows. You can put this into a file named GetTranscripts.py
```
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta
from pytube import Playlist

import sys
import json

def convertSecondsToTime(seconds_string):
  raw_seconds = int(seconds_string)
  return timedelta(seconds=raw_seconds)

def writeTranscriptToFile(filename, video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open(filename+".txt", "w", encoding="utf-8") as f:
        for line in transcript: 
            f.write("{} {}\n".format(convertSecondsToTime(line['start']), line['text']))   


if (len(sys.argv) != 2):
  print ('Invalid number of parameters')
  print('usage:  GetTranscripts <full youtube playlist url>')
  exit()

playlist = Playlist(sys.argv[1])

for video in playlist.videos:
    print ("Downloading transcript: {}".format(video.title))
    writeTranscriptToFile(video.title, video.video_id)
```
## Running the program
You can run the program from the command line. Launch your preferred console ie. Windows Command Prompt and enter the following:

```> py GetTranscripts.py <full youtube playlist url>```

You should start seeing output like this:

```
Downloading transcript: Path of Night Episode 1 - Baptized in Blood
Downloading transcript: Path of Night Episode 2 - The Sheriff and the Shark
Downloading transcript: Path of Night Episode 3 - New Year's Kiss
…
```

