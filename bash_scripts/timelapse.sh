#!/bin/bash

# ffmpeg -i /mnt/c/Users/Benjamin/Videos/2023-11-16-11-39-05.mkv -filter_complex "[0:v]setpts=PTS/12[v];[v]crop=5:550:340:65" -an /mnt/c/Users/Benjamin/Videos/timelapse_2023-11-16-11-39-05.mp4

# Define Variables # Both screens are 1920 x 1080
INPUT_PATH="/mnt/c/Users/Benjamin/Videos/Timelapses/drawing4.mkv"
OUTPUT_PATH="/mnt/c/Users/Benjamin/Videos/Timelapses/tl_drawing4.mp4"
CROP_WIDTH=603
CROP_HEIGHT=610
CROP_X=0
CROP_Y=0
SPEED_FACTOR=16

# Run FFmpeg command with variables
ffmpeg -i "$INPUT_PATH" -filter_complex "[0:v]setpts=PTS/$SPEED_FACTOR[v];[v]crop=$CROP_WIDTH:$CROP_HEIGHT:$CROP_X:$CROP_Y" -an "$OUTPUT_PATH"

