### Implement your code in `main.py`

### Build your Docker image:
* Write the `Dockerfile`
* Make sure to include your code + install all necessary requirements
* From this project's dir run (replace _<yourname>_ with your name):
  * `docker build -t <yourname> .`

### Run a container locally:
* `docker run --rm -it <yourname>`
* Explanation:
  * `--rm` - Automatically remove the container when it exits
  * `-it` -  instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container.

### Deploy your image to DockerHub
* TODO: OFEK

### Pull your friend's image from DockerHub
* TODO: OFEK

### Passing a parameter and a file into the docker container
* Run the following command (replace _<your_friend_image_name>_ with your friend's image name):
* `docker run --rm --mount type=bind,src='<some_video_file_from_your_local_filesystem>',dst='/tmp/my_video.mp4' -e VIDEO_PATH='/tmp/my_video.mp4' <your_friend_image_name>`
* Explanation:
  * `--rm` - Automatically remove the container when it exits
  * `-e` - Set environment variables
  * `--mount` - allows you to mount volumes, in our case, a specific file