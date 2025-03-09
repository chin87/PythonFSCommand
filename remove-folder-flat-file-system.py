import os
import shutil

def move_files_to_base(base_folder):
    for root, dirs, files in os.walk(base_folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            new_path = os.path.join(base_folder, file)
            counter = 1
            
            # Ensure unique file name if a file with same name exists
            while os.path.exists(new_path):
                name, ext = os.path.splitext(file)
                new_path = os.path.join(base_folder, f"{name}_{counter}{ext}")
                counter += 1
            
            shutil.move(file_path, new_path)
            print(f"Moved: {file_path} -> {new_path}")
        
        # Remove empty directories
        if root != base_folder and not os.listdir(root):
            os.rmdir(root)
            print(f"Removed empty folder: {root}")

if __name__ == "__main__":
    base_folder = os.getcwd()  # Use the folder where the script is located
    move_files_to_base(base_folder)