import os
import hashlib
import datetime

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def calculate_file_hash(file_path, algorithm='md5', chunk_size=4096):
    """Calculate file hash using specified algorithm"""
    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def get_date_folder(file_path, use_creation_date=True, folder_format="monthly"):
    """Get date-based folder path based on file metadata"""
    stat = os.stat(file_path)
    timestamp = stat.st_ctime if use_creation_date else stat.st_mtime
    date = datetime.datetime.fromtimestamp(timestamp)
    
    if folder_format == "quarterly":
        quarter = (date.month - 1) // 3 + 1
        return f"{date.year}-Q{quarter}"
    return f"{date.year}-{date.month:02d}"