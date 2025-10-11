import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_folder(folder_path):
    """
    Organizes files in the given folder based on file type.
    """
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Determine the category of the file
        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                category_path = os.path.join(folder_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)  # Create folder if it doesn't exist
                shutil.move(file_path, os.path.join(category_path, filename))
                moved = True
                break

        # If file type not found, move to "Others"
        if not moved:
            others_path = os.path.join(folder_path, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            shutil.move(file_path, os.path.join(others_path, filename))

    print("Folder organized successfully!")

# Example usage
if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    organize_folder(folder)
