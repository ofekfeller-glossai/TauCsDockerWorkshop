### Goal
* Implement a basic video editing black-box tool.
* Input: video file
* Output: same video with some manipulation

### Implement your code in `main.py`
1. Input file logic was implemented for you
2. Manipulate the video file and generate a new one
3. Save your output in the same folder

* Ideas for packages and manipulations to use:
   *	Cv2
        * Text on screen - https://www.geeksforgeeks.org/python-opencv-write-text-on-video/

        * Crop parts of the video - https://www.geeksforgeeks.org/moviepy-getting-cut-out-of-video-file-clip/

        * Slow motion - https://www.codespeedy.com/creating-a-slow-motion-video-using-opencv-in-python/

        * Drow a rectangle on screen - https://www.geeksforgeeks.org/how-to-draw-filled-rectangle-to-every-frame-of-video-by-using-python-opencv/

  * Moviepy –
    * Text on screen - https://www.geeksforgeeks.org/moviepy-inserting-text-in-the-video/

    * Rotating video - https://www.geeksforgeeks.org/moviepy-rotating-video-file/

    * Freeze painting effect - https://zulko.github.io/moviepy/examples/painting_effect.html

    * Change movie speed (fast/slow motion) - https://www.geeksforgeeks.org/moviepy-applying-speed-effect-on-video-clip/

    * Mirroring video - https://www.geeksforgeeks.org/moviepy-mirroring-video-file-clip-for-x-axis/?ref=rp

    * Blurring movie - https://zulko.github.io/moviepy/examples/quick_recipes.html#blurring-all-frames-of-a-video


### Build your Docker image:
* Write the `Dockerfile`
* Make sure to include your code + install all necessary requirements
* Enter exercise folder: `cd exercise`
* From this project's dir run (replace _<yourname>_ with your name) - including the `.` at the end of the line:
  * `docker build -t taucsclub/cs_club_docker_workshop:<yourname> .`

### Run a container locally:
* `docker run --rm -it taucsclub/cs_club_docker_workshop:<yourname>`

* Explanation:
  * `--rm` - Automatically remove the container when it exits
  * `-it` -  instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container.

### Deploy your image to DockerHub
* Login to you docker hub account
* docker push taucsclub/cs_club_docker_workshop:<yourname>



### Pull your friend's image from DockerHub
* `docker pull taucsclub/cs_club_docker_workshop:<your_friends_name>`

### Passing a parameter and a file into the docker container
* Run the following command (replace all _<...>_, with your own values):
    * <some_folder_in_your_local_filesystem> - folder that conains a video file to work on
    * <video_file_name> - the actual file name
    * <your_friends_name> - your friend's image name
* `docker run --rm --mount type=bind,src='C:\Users\Yonatan\Desktop\TauCsDockerWorkshop\exercise\video',dst='/tmp/video' -e VIDEO_PATH='tmp/video/bird.mp4' taucsclub/cs_club_docker_workshop:>`


* Explanation:
  * `--rm` - Automatically remove the container when it exits
  * `-e` - Set environment variables
  * `--mount` - allows you to mount volumes, in our case, a specific file
