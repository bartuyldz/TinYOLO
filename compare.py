import os

def compare_directories(directory1, directory2, output_file):
    # List files in both directories
    files1 = set(os.path.splitext(f)[0] for f in os.listdir(directory1))  # Remove extensions
    files2 = set(os.path.splitext(f)[0] for f in os.listdir(directory2))  # Remove extensions
    
    # Find files that are in directory1 but not in directory2 and vice versa
    missing_in_dir2 = files1 - files2
    missing_in_dir1 = files2 - files1
    
    # Write the missing files to a text file
    with open(output_file, 'w') as f:
        f.write("Missing in directory2 (labels):\n")
        for file in missing_in_dir2:
            f.write(f"{file}\n")
        
        f.write("\nMissing in directory1 (images):\n")
        for file in missing_in_dir1:
            f.write(f"{file}\n")
    
    print(f"Missing files have been written to {output_file}")
    
    # Return the missing files so they can be used elsewhere if needed
    return missing_in_dir2, missing_in_dir1

# Example usage
dir1 = './images/total'  # replace with actual path to the first directory
dir2 = './labels'  # replace with actual path to the second directory
output_file = 'missing_files.txt'  # output file to save the missing file names

# Ensure the function returns the missing files
missing_in_dir2, missing_in_dir1 = compare_directories(dir1, dir2, output_file)
