### Goal
Implement a basic video editing black-box tool.
Input: video file
Output: same video with some manipulation

### Implement your code in `main.py`
1. Input file logic was implemented for you
2. Manipulate the video file and generate a new one
3. Save your output in the same folder

* Ideas for packages to use:
   * moviepy
   * cv2

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
* `docker run --rm --mount type=bind,src='<some_folder_in_your_local_filesystem>',dst='/tmp/video' -e VIDEO_PATH='/tmp/video/<video_file_name>' taucsclub/cs_club_docker_workshop:<your_friends_name>`
* Explanation:
  * `--rm` - Automatically remove the container when it exits
  * `-e` - Set environment variables
  * `--mount` - allows you to mount volumes, in our case, a specific file
