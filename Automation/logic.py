# logic.py

import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".hevc"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".html", ".css"],
    "Others": []
}

def organize_directory(directory):
    logs = []

    if not os.path.exists(directory):
        logs.append(f"Directory '{directory}' does not exist.")
        return logs

    for root, dirs, files in os.walk(directory):
         for filename in files:
            filepath = os.path.join(root, filename)

            # Skip files already in the main directory
            if os.path.dirname(filepath) == directory:
                continue

            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            category = "Others"
            for cat, extensions in FILE_CATEGORIES.items():
                if extension in extensions:
                    category = cat
                    break

            category_folder = os.path.join(directory, category)
            os.makedirs(category_folder, exist_ok=True)

            try:
                shutil.move(filepath, os.path.join(category_folder, filename))
                logs.append(f"Moved '{filename}' from subfolder to '{category}/'.")
            except Exception as e:
                logs.append(f"Error moving file '{filename}' from subfolder: {e}")


    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isdir(filepath):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        category = "Others"
        for cat, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                category = cat
                break

        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

        try:
            shutil.move(filepath, os.path.join(category_folder, filename))
            logs.append(f"Moved '{filename}' to '{category}/'.")
        except Exception as e:
            logs.append(f"Error moving file '{filename}': {e}")

        # Recursively delete empty subfolders
    for root, dirs, _ in os.walk(directory, topdown=False):
        for d in dirs:
            folder_path = os.path.join(root, d)
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)
                    logs.append(f"Deleted empty subfolder: {folder_path}")
                except Exception as e:
                    logs.append(f"Could not delete subfolder: {folder_path} -> {e}")

    return logs