import pandas as pd
from moviepy.editor import *

def get_videos_to_merge(spreadsheet_name):
  dfs = pd.read_excel(f"spreadsheets/{spreadsheet_name}", sheet_name="Sheet1", engine="openpyxl", header=None)
  videos_to_be_merged = []
  for item in dfs.values:
    videos = [x for x in item[0:-2]]
    video_dict = {
      "videos": videos,
      "audio": item[-2],
      "output": f"output/{item[-1]}"
    }
    videos_to_be_merged.append(video_dict)

  return videos_to_be_merged

videos = get_videos_to_merge("spreadsheet1.xlsx")

for video in videos:
  clips = [VideoFileClip(x) for x in video["videos"]]
  concatenation = concatenate_videoclips(clips)
  audioclip = AudioFileClip(video["audio"])


  video_duration = concatenation.duration

  if video_duration < audioclip.duration:
    audioclip = audioclip.subclip(0, video_duration)
  
  concatenation.audio = audioclip
  concatenation.write_videofile(f"{video['output']}.mp4")

