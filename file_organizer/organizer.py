import os
import shutil
from file_organizer.utils import ensure_dir_exists

def organize_files(base_dir, file_types):
    for category, extensions in file_types.items():
        category_dir = os.path.join(base_dir, category)
        ensure_dir_exists(category_dir)

        for filename in os.listdir(base_dir):
            if any(filename.lower().endswith(ext) for ext in extensions):
                src_path = os.path.join(base_dir, filename)
                dst_path = os.path.join(category_dir, filename)
                shutil.move(src_path, dst_path)
                print(f"Moved {filename} to {category_dir}")