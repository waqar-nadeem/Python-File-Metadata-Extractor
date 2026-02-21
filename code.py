import os
import sys
import platform
from datetime import datetime

def get_file_metadata(path):
    if not os.path.exists(path):
        return None

    stats = os.stat(path)

    metadata = {
        "File Name": os.path.basename(path),
        "Absolute Path": os.path.abspath(path),
        "Size (bytes)": stats.st_size,
        "Created": datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
        "Last Modified": datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
        "Last Accessed": datetime.fromtimestamp(stats.st_atime).strftime("%Y-%m-%d %H:%M:%S"),
        "File Type": "Directory" if os.path.isdir(path) else "File",
        "Operating System": platform.system()
    }

    return metadata

if __name__ == "__main__":
    path = input("Enter file or directory path: ").strip()

    metadata = get_file_metadata(path)

    if metadata:
        print("\nFile Metadata:\n")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("Path does not exist.")
