import os
import hashlib

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