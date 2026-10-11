"""_summary_ This file contains all the deletion logic and 
    is intentionally kept separate from the main application
"""

from pathlib import Path

class DeletionError(Exception):
    "Raise when a deletion safety check fails"    

def validate_target(path: Path, root: Path) -> Path:
    path = path.expanduser().resolve(strict=False)
    root = root.expanduser().resolve(strict=False)
   
    if not path.exists(): 
        raise DeletionError (
            f"File no longer exists {path}"
        )
    
    if not path.is_file():
        raise DeletionError (
            f"File no longer exists {path}"
        )
    
    # important check so that the util cannot delete files outside the opened directory!!!
    try:
        path.relative_to(root)
    except ValueError:
        raise DeletionError(
            f"Cant delete file outside scan directory: {path}"
        )
    return path

"""
_summary_ : Function to delete a selected file
"""
def delete_file(path: Path, root: Path) -> None:
    target = validate_target(path, root)
    
    # Crude method to delete files since implementing recycle bin deletion + 
    # undo is jus too much work lol ill get to it in another vid
    # TODO: actual platform specific deletion
    target.unlink()
    
"""
__Summary__: 
"""
def delete_dupes(dupes, root):
    total = sum(len(paths) - 1 for paths in dupes.values())
    # TODO implement interactive selection
    print(f"\nFound {total} duplicate file(s) which can be selected and deleted")
    answer = input("\n> Delete Duplicates? [y/n]: ").strip().lower()
    
    if (answer not in ["yes", "y", "Y", "Yes"]):
        print(f"Deletion Cancelled!")
        return

    deleted = 0
    failed = 0
    
    for paths in dupes.values():
        # retain only the first value and delete the 
        # rest in each duplicate group
        # TODO this logic is effectively invalidated once interactive deletion is implemented
        
        for path in paths[1:]:
            try:
                delete_file(path, root)
                print(f"\nDeleted! : {path}")
                deleted += 1
            
            except DeletionError as error:
                print(f"\nSkipped : {error}")
                failed += 1
                
        print(f"\nDeletion Complete!\n{deleted} file(s) deleted and {failed} file(s) skipped")
