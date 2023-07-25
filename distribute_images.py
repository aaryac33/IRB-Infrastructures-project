import os
import shutil
import random

def divide_images_into_folders(source_folder, n):
    # Get a list of all image files in the source folder
    image_files = [file for file in os.listdir(source_folder) if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]
    
    # Calculate the number of images per subfolder (approximately)
    images_per_subfolder = len(image_files) // n
    
    # Shuffle the image files randomly
    random.shuffle(image_files)
    
    # Create n subfolders and distribute the images
    for i in range(n):
        subfolder_path = os.path.join(source_folder, f"Subfolder_{i+1}")
        os.makedirs(subfolder_path, exist_ok=True)
        
        start_index = i * images_per_subfolder
        end_index = start_index + images_per_subfolder if i < n-1 else len(image_files)
        
        for j in range(start_index, end_index):
            image_file = image_files[j]
            source_file_path = os.path.join(source_folder, image_file)
            target_file_path = os.path.join(subfolder_path, image_file)
            shutil.move(source_file_path, target_file_path)
    
    print(f"{len(image_files)} images distributed into {n} subfolders.")

if __name__ == "__main__":
    source_folder = r"C:\Users\aarya\OneDrive\Desktop\Assert.ai\IRBframes\Subfolder_7"  # Replace with the path to your source folder containing images
    n = 2  # Replace with the number of subfolders you want
    divide_images_into_folders(source_folder, n)