#!/bin/bash

# Define a default commit message
default_msg="optimize"

# Use the provided commit message if available, otherwise use the default
msg="${1:-$default_msg}"

# Perform the git operations
git add .
git commit -m "$msg"
git push origin main
