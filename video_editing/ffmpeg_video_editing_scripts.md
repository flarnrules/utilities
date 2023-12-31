# Ffmpeg Video editing scripts

Some general information about ffmpeg:

`ffmpeg -i input.mkv -filter_complex "[0:v]setpts=PTS/(TIMELAPSE_FACTOR)[v];[v]crop=W:H:X:Y" -an output.mkv`

- input.mkv can be mp4
- TIMELAPSE_FACTOR needs to be replaced with an integer, like 4, which would mean 4x as fast.
- W:H:X:Y are crop parameters (Width, Height, X-coordinate, Y-coordinate)
- The `-an` flag omits audio.


### to access videos from windows

`/mnt/c/Users/Benjamin/Videos/my_video_name.mp4`

so a working script might look like this:
`ffmpeg -i /mnt/c/Users/Benjamin/Videos/2023-11-16-11-39-05.mkv -filter_complex "[0:v]setpts=PTS/4[v];[v]crop=640:640:320:50" -an timelapse_2023-11-16-11-39-05.mkv`

the workflow right now is definitely VS Code for this project.
Also, emacs is just too hard to actually develop with.
unfortunuately, launching vs code is a huge pain for me right now.

Once the files have been run through ffmpeg, if they have been turned into gifs, we can compress them with gifcicle. Here's how that would work:

`gifsicle -i input.gif --optimize=3 -o output.gif`