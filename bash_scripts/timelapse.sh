#!/bin/bash

# ffmpeg -i /mnt/c/Users/Benjamin/Videos/2023-11-16-11-39-05.mkv -filter_complex "[0:v]setpts=PTS/12[v];[v]crop=550:550:340:65" -an /mnt/c/Users/Benjamin/Videos/timelapse_2023-11-16-11-39-05.mp4

# Define Variables
INPUT_PATH="/mnt/c/Users/Benjamin/Videos/2023-11-16-11-39-05.mkv"
OUTPUT_PATH="/mnt/c/Users/Benjamin/Videos/timelapse_2023-11-16-11-39-05.mp4"
CROP_WIDTH=550
CROP_HEIGHT=550
CROP_X=340
CROP_Y=65
SPEED_FACTOR=12

# Run FFmpeg command with variables
ffmpeg - "$INPUT_PATH" -filter_complex "[0:v]setpts=PTS/$SPEED_FACTOR[v];[v]crop=$CROP_WIDTH:$CROP_HEIGHT:$CROP_X:$CROP_Y" -an "$OUTPUT_PATH"
