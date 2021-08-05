#Created by: Arjith
#Date:19-06-2021
#Purpose:Generating subtitles for videos using srt file
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import requests
import cv2



def generator(txt): 
    return TextClip(txt, font='Arial', fontsize=16, color='white')


subtitles = SubtitlesClip("Tom Cruise.srt", generator)

video = VideoFileClip("Tom Cruise.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])

result.write_videofile("Tom.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a",
                       remove_temp=True, codec="libx264", audio_codec="aac")
cap=cv2.VideoCapture('Tom.mp4')
while(True):
    ret,frame=cap.read()

    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()