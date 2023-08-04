#!/bin/bash

# Backup the original podanvil.py file
cp podanvil.py podanvil.py.bak

# Create new Python files
echo > pod_utils.py
echo > general_utils.py

# Define the functions that will go in each file
pod_functions=("deploy_pod" "get_pod_url" "is_accessible")
general_functions=("generate_name" "get_active_node")

# Move the functions to the appropriate files
for function in "${pod_functions[@]}"; do
    sed -n "/def ${function}/,/^$/p" podanvil.py >> pod_utils.py
done

for function in "${general_functions[@]}"; do
    sed -n "/def ${function}/,/^$/p" podanvil.py >> general_utils.py
done

# Remove the moved functions from the original file
for function in "${pod_functions[@]}" "${general_functions[@]}"; do
    sed -i "/def ${function}/,/^$/d" podanvil.py
done

# Add import statements to the original file
echo "from pod_utils import *" >> podanvil.py
echo "from general_utils import *" >> podanvil.py

