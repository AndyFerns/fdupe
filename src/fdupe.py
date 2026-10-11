from pathlib import Path 
import argparse

from cli import initialize_parser
from utils import find_files, find_dupes, print_dupes
from deleter import delete_dupes, DeletionError

def main():
    args = initialize_parser()
    root = Path(args.directory)
    
    # check input
    if not root.exists():
        raise DeletionError(f"\nDirectory doesnt exist! {root}")
    
    # else continue and find files:
    files: list = find_files(root)
    print(f"Scanned {len(files)} file(s)\n")
    
    # find and check for duplicates
    dupes = find_dupes(files)
    print_dupes(dupes)
    
    if args.delete and dupes:
        delete_dupes(dupes, root)
    
if __name__ == '__main__':
    main()
