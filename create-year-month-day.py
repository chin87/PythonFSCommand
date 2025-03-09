import os
from datetime import datetime

def create_folders_and_files(base_folder):
    current_year = datetime.now().year
    start_year = current_year - 19  # Last 20 years including current year

    for year in range(start_year, current_year + 1):
        year_folder = os.path.join(base_folder, str(year))
        os.makedirs(year_folder, exist_ok=True)
        
        for month in range(1, 13):
            month_folder = os.path.join(year_folder, f"{month:02d}")
            os.makedirs(month_folder, exist_ok=True)
            
            for day in range(1, 32):  # Handling variable days per month
                try:
                    date = datetime(year, month, day)  # Validate if date exists
                    file_path = os.path.join(month_folder, f"{day:02d}.txt")
                    with open(file_path, 'w') as file:
                        file.write(f"This is {date.strftime('%Y-%m-%d')}")
                except ValueError:
                    continue  # Skip invalid dates

if __name__ == "__main__":
    base_folder = os.getcwd()  # Change this path if needed
    create_folders_and_files(base_folder)