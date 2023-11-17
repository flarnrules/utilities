#!/bin/bash

# Array of input files (add or remove files as needed)
input_files=(
    "/mnt/c/Users/Benjamin/Videos/timelapses/timelapse_dwg3_tl_1.mp4"
    "/mnt/c/Users/Benjamin/Videos/timelapses/timelapse_dwg3_tl_2.mp4"
    
    # Add more files here
)

# Output file path
output_file="/mnt/c/Users/Benjamin/Videos/timelapses/stitched_dwg3.mp4"

# Temporary file for the file list
temp_file_list=$(mktemp /tmp/filelist.XXXXXX.txt)

# Generate a file list for FFmpeg
for file in "${input_files[@]}"; do
    echo "file '$file'" >> "$temp_file_list"
done

# Stitch the clips together
ffmpeg -f concat -safe 0 -i "$temp_file_list" -c copy "$output_file"

# Remove the temporary file
rm "$temp_file_list"

echo "Stitching complete. Output file is $output_file"
