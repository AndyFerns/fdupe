"""
_summary_ : Command line interface for fdupe
TODO: add the tui logic here  
TODO: implement the cross system file deletion logic here
"""

import argparse

def initialize_parser():
    # first parse args
    parser = argparse.ArgumentParser(
        description="fdupe - find duplicate files"
    )

    parser.add_argument(
        "directory",
        help="Directory to scan, fdupe will only recursively scan from this directory"
    )

    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete Duplicate Files"
    )
    
    return parser.parse_args()