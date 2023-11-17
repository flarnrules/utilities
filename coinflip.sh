#!/bin/bash

# Randomly choose between 1 and 2
result=$((RANDOM % 2))

# Determine the outcome
if [ $result -eq 0 ]; then
    echo "Heads"
else
    echo "Tails"
fi
