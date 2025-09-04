#!/bin/bash

# Find the file with the specified name and rename it
find -L ../fwh -type f -name "*Observer2.png" | while read -r file; do
    # Extract the directory name containing "AOA" in its path
    folder_name=$(dirname "$file" | grep -o '/AOA[^/]*' | sed 's#^/##')

    # Rename the file with the folder name
    if [[ -n $folder_name ]]; then
        new_name=FWHObserver2_"$folder_name.png"
        cp "$file" "$new_name"
        echo "Renamed '$file' to '$new_name'"
    else
        echo "Error: Folder name with 'AOA' not found in the path of '$file'"
    fi
done

