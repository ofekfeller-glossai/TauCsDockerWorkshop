import os
import pathlib


def get_video_path():
    default_path = (pathlib.Path(__file__).parent / "video" / "bird.mp4").as_posix()
    video_path = os.environ.get("VIDEO_PATH", default_path)
    return video_path


def process_video(video_path):
    print(f'Processing {video_path=}')
    
    ################################
    # Add your implementation here #
    ################################
    

if __name__ == '__main__':
    your_name = 'Put your name here!'
    video_path = get_video_path()
    
    print(f'Running from inside {your_name}\'s container :)')
    process_video(video_path=video_path)
