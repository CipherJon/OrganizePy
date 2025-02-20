import os
from file_organizer.config import FILE_TYPES, BASE_DIR
from file_organizer.organizer import organize_files

def main():
    organize_files(BASE_DIR, FILE_TYPES)

if __name__ == "__main__":
    main()