import os
import shutil

def move_files_to_base(base_folder):
    for root, dirs, files in os.walk(base_folder, topdown=False):
        # Skip hidden folders (starting with '.')
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.startswith('.'):  # Skip hidden files
                continue
            
            file_path = os.path.join(root, file)
            new_file_name = file.replace(" ", "_")  # Replace spaces with underscores
            new_path = os.path.join(base_folder, new_file_name)
            counter = 1
            
            # Ensure unique file name if a file with same name exists
            while os.path.exists(new_path):
                name, ext = os.path.splitext(new_file_name)
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