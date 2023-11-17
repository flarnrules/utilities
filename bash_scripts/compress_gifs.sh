#!/bin/bash

for gif in *.gif; do
    gifsicle -i "$gif" --optimize=3 -o "compressed_$gif"
done
