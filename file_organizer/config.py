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