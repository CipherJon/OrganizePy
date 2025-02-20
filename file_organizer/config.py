import os

# Base directory to organize
BASE_DIR = os.path.expanduser("~/Downloads")

# File types and their corresponding directories
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "archives": [".zip", ".tar.gz", ".rar"],
    "videos": [".mp4", ".mov"],
    "music": [".mp3", ".wav"],
}