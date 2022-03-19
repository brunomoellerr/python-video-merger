
# python-video-merger
script to merge videos and audios into a single video

it's ***required*** to have in a spreadsheet the name of the files you would like to merge into spreadsheets folder.

folder structure I'm using is:

--output
--spreadsheets
--videos
merger.py

spreadsheets is where I store the spreadsheet being used to define what will be the order of the merge. 
in the example below is video1 + video2 + video3 and the audio. the output will be named as output1 and stored in output folder

the spreadsheet should have the following format containing the path where the files are stored
| videos/video1.mp4 | videos/video2.mp4 |videos/video3.mp4 |  videos/audio1.mp3 |output1
|--|--|--|--|--
|  |  |  |  |
