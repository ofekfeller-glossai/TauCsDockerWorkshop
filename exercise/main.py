import os
import pathlib
from moviepy.editor import *



def get_video_path():
    default_path = (pathlib.Path(__file__).parent / "video" / "bird.mp4").as_posix()
    video_path = os.environ.get("VIDEO_PATH", default_path)
    return video_path


def process_video(video_path):
    print(f'Processing {video_path=}')
    clip = VideoFileClip(video_path)
  
    # getting subclip as video is large
    #clip = clip.subclip(55, 65)
  
    # rotating clip by 45 degree
    clip = clip.rotate(45)
  
    # showing clip
    #clip.ipython_display(width = 480)
    clip.write_videofile(str(pathlib.Path(video_path).parent / "new_video.mp4"))
    return clip
    

if __name__ == '__main__':
    your_name = 'Put your name here!'
    video_path = get_video_path()
    
    print(f'Running from inside {your_name}\'s container :)')
    process_video(video_path=video_path)
