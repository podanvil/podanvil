#!/bin/bash

# Get UUID of the home-ext4 partition
uuid=$(sudo blkid | grep home-ext4 | awk -F " " '{print $2}' | tr -d "\"")

# Mount the home-ext4 partition to a temporary location
sudo mkdir /mnt/home-ext4
sudo mount -t ext4 $uuid /mnt/home-ext4

# Define source and target directories
source_dir="/home/"
target_dir="/mnt/home-ext4/"

# Run rsync to copy newer or non-existing files
rsync -avu --progress "$source_dir" "$target_dir"
