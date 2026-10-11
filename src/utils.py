"""
_summary_: Main file to implement fdupe file operations and functional utilities
"""

from collections import defaultdict
import hashlib

def find_files(root):
    files = []
    
    for path in root.rglob("*"):
        if path.is_file():
            # if returns true, append to list of paths
            files.append(path)
    
    return files    

# sort by filesize now
def group_by_filesize(files):
    group = defaultdict(list)
    
    for f in files:
        size = f.stat().st_size
        group[size].append(f)
        
    return group

# hash function
def hash_file(path):
    with path.open("rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()
    

# Find files with identical contents
def find_dupes(files):
    size_groups = group_by_filesize(files)
    hash_groups = defaultdict(list)
    
    # checking for different sized files and NOT hashing them
    # paths is a better var name rather than file
    for paths in size_groups.values():
        if len(paths) < 2:
            continue

        for path in paths:
            #hash here
            hashes = hash_file(path)

            hash_groups[hashes].append(path)
            # tfw you have to debug indentation in python
    
    return {
        hashes: paths for hashes, 
        paths in hash_groups.items() 
        if len(paths) > 1
    }

# helper to print duplicates
def print_dupes(dupes):
    if not dupes:
        print("No dupes found!\n")
        return
    
    print(f"Found {len(dupes)} number of duplicate group(s)\n")
    
    for i, p in enumerate(dupes.values(), start = 1):
        print(f"Group {i}\n")

        for path in p:
            print(f" {path}\n")