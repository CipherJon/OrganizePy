import os

# Base directory to organize
BASE_DIR = os.path.expanduser("~/Downloads")

# File types and their corresponding directories
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".svg"],
    "documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".odt", ".rtf", ".csv", ".ods"],
    "archives": [".zip", ".tar.gz", ".rar", ".7z", ".bz2"],
    "videos": [".mp4", ".mov", ".mkv", ".avi", ".flv", ".wmv"],
    "music": [".mp3", ".wav", ".ogg", ".flac"],
    "others": []
}

# Duplicate detection settings
DUPLICATE_HANDLING = {
    "enabled": True,
    "detection_method": "hash",  # options: name, size, hash
    "handle_duplicates": "move",  # options: keep, move, delete
    "duplicates_dir": os.path.join(BASE_DIR, "_duplicates")
}

# Date-based organization settings
DATE_ORGANIZATION = {
    "enabled": False,
    "use_creation_date": True,
    "folder_format": "monthly",  # options: monthly, quarterly
}

# Date-based organization settings
DATE_ORGANIZATION = {
    "enabled": False,
    "use_creation_date": True,
    "folder_format": "monthly",  # options: monthly, quarterly
}