import os
import shutil
from file_organizer.utils import ensure_dir_exists, calculate_file_hash, get_date_folder
from file_organizer.config import DUPLICATE_HANDLING, DATE_ORGANIZATION

def organize_files(base_dir, file_types):
    # Initialize duplicate tracking
    known_files = {}
    
    # Only set up duplicates_dir if duplicate handling is enabled
    if DUPLICATE_HANDLING.get("enabled", False):
        dup_dir = DUPLICATE_HANDLING.get("duplicates_dir", "duplicates")  # Default to "duplicates"
        full_dup_dir = os.path.join(base_dir, dup_dir)  # Make it relative to base_dir
        ensure_dir_exists(full_dup_dir)
    else:
        full_dup_dir = None  # Avoid using dup_dir when not enabled

    # Pre-scan existing files for duplicates
    if DUPLICATE_HANDLING.get("enabled", False):
        for root, _, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                detection_method = DUPLICATE_HANDLING.get("detection_method", "name")  # Default to "name"
                if detection_method == "hash":
                    file_id = calculate_file_hash(file_path)
                elif detection_method == "size":
                    file_id = os.path.getsize(file_path)
                else:  # name
                    file_id = file.lower()
                known_files[file_id] = file_path

    # Process new files
    for category, extensions in file_types.items():
        category_dir = os.path.join(base_dir, category)
        ensure_dir_exists(category_dir)

        for filename in os.listdir(base_dir):
            file_path = os.path.join(base_dir, filename)
            if not os.path.isfile(file_path):
                continue

            # Skip files that don't match any category
            if not any(filename.lower().endswith(ext) for ext in extensions):
                continue

            # Check for duplicates
            if DUPLICATE_HANDLING.get("enabled", False):
                detection_method = DUPLICATE_HANDLING.get("detection_method", "name")
                if detection_method == "hash":
                    file_id = calculate_file_hash(file_path)
                elif detection_method == "size":
                    file_id = os.path.getsize(file_path)
                else:  # name
                    file_id = filename.lower()

                if file_id in known_files:
                    original = known_files[file_id]
                    print(f"Duplicate found: {filename} matches {os.path.basename(original)}")
                    
                    handle_method = DUPLICATE_HANDLING.get("handle_duplicates", "move")  # Default to "move"
                    if handle_method == "move":
                        dup_path = os.path.join(full_dup_dir, filename)
                        shutil.move(file_path, dup_path)
                        print(f"Moved duplicate {filename} to {full_dup_dir}")
                    elif handle_method == "delete":
                        os.remove(file_path)
                        print(f"Deleted duplicate {filename}")
                    continue  # Skip normal processing for duplicates

                known_files[file_id] = file_path

            # Move file to category directory
            dst_path = os.path.join(category_dir, filename)
            shutil.move(file_path, dst_path)
            print(f"Moved {filename} to {category_dir}")