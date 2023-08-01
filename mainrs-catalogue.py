
import os

# Starting directory
start_dir = os.path.expanduser("~")

# Output file
output_file = os.path.join(start_dir, "main.rs.combo.txt")

# Search for 'main.rs' files
files_found = []
for dirpath, dirnames, filenames in os.walk(start_dir):
    for filename in filenames:
        if filename == "main.rs":
            file_path = os.path.join(dirpath, filename)
            files_found.append(file_path)

# Write file paths and contents to the output file
with open(output_file, "w") as f_out:
    for file_path in files_found:
        with open(file_path, "r") as f_in:
            content = f_in.read()
        f_out.write(f"{file_path}\n{content}\n\n")

