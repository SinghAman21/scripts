#!/bin/bash

# Prompt user to enter values
read -p "Enter space-separated values: " values

# Convert input string into an array
read -r -a values <<< "$values"

# Initialize max with the first element of the array
max=${values[0]}

# Loop through each number in the array
for num in "${values[@]}"; do
    # Check if current number is greater than max
    if (( num > max )); then
        max=$num
    fi
done

# Print the maximum value
echo "Max: $max"
