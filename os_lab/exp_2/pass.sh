#!/bin/bash

# Read the first password
read -sp "Enter your password: " password
echo

# Read the confirmation password
read -sp "Confirm your password: " confirm_password
echo

# Check if both passwords match
if [ "$password" = "$confirm_password" ]; then
  echo "Passwords match."
else
  echo "Passwords do not match."
fi
