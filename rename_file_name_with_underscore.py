import os

def rename_files_and_folders(base_folder):
    for root, dirs, files in os.walk(base_folder, topdown=False):
        # Rename files
        for file in files:
            new_file_name = file.replace(" ", "_")
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_file_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
        
        # Rename directories
        for dir_name in dirs:
            new_dir_name = dir_name.replace(" ", "_")
            old_path = os.path.join(root, dir_name)
            new_path = os.path.join(root, new_dir_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    base_folder = os.getcwd()  # Use the folder where the script is located
    rename_files_and_folders(base_folder)