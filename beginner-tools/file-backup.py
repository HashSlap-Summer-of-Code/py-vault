#!/usr/bin/env python3

"""
File Backup Script

Usage:
    python file-backup.py <filename>

Description:
    This script takes a source file path as a command-line argument,
    and creates a backup copy by appending `.bak` to the original filename.
    Example: mynotes.txt ➝ mynotes.txt.bak

Note:
    - The backup will be placed in the same directory as the original file.
    - If the file does not exist, it will print an appropriate error message.


"""

import sys
import os
import shutil

def backup_file(source_path):
    if not os.path.isfile(source_path):
        print(f"Error: File '{source_path}' does not exist.")
        return

    backup_path = source_path + ".bak"

    try:
        shutil.copy2(source_path, backup_path)
        print(f"Backup created: '{backup_path}'")
    except Exception as e:
        print(f"Failed to create backup: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python file-backup.py <filename>")
        return

    source_file = sys.argv[1]
    backup_file(source_file)

if __name__ == "__main__":
    main()
