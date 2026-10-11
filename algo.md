# Fdupe Algorithms

## Duplicate finding Algorithm

directory path -> recursively scan files -> check for duplicates ->group by size -> discard unique sizes -> hash candidates (sha 256)

Adding deletion to fdupe along with minor modularization because the codebase looks too monolithic lol

## Deletion Algorithm

-> ask user for confirmation on finding dupes
-> keep the first file (add a TUI later on (look into tui libs and choose the best for this util))
-> validate path !!!!!!! (v imp so taht i dont sudo rm -rf my entire filesystem)
-> handle errors (craete custom class for duplicate errors and populate later on)
