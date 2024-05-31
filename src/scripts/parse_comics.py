import os
import shutil

# Define the origin and destination directories
origin_dir = r'C:\Users\metaj\Downloads\Rick Griffin Comics\Comics Holding Spot\Zootopia'
destination_dir = r'C:\Users\metaj\Documents\GitHub\griffintest\your_content\zootopia - night terrors\comics'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# List of dates for the 'Post date' field
dates = [
    "March 26, 2016", "March 26, 2016", "March 26, 2016",
    "March 26, 2016", "March 26, 2016", "March 26, 2016",
    "March 26, 2016"
]

# Get the list of images in the origin directory, sorted to process them in order
images = sorted([f for f in os.listdir(origin_dir) if os.path.isfile(os.path.join(origin_dir, f))])

# Go through each image in the origin directory
for image_index, image in enumerate(images, start=1):
    image_path = os.path.join(origin_dir, image)

    # Create a new directory for the current image
    new_folder_name = f"{image_index:03d}"
    new_folder_path = os.path.join(destination_dir, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Copy the image to the new directory
    shutil.copy(image_path, os.path.join(new_folder_path, image))

    # Create an empty post.txt file in the new directory
    post_txt_path = os.path.join(new_folder_path, 'post.txt')
    with open(post_txt_path, 'w') as post_txt_file:
        pass  # Create an empty file

    # Determine the title for the info.ini file
    title = f"Zootopia - Night Terrors Page {image_index:03d}"

    # Get the post date for the current image
    post_date = dates[image_index - 1] if image_index - 1 < len(dates) else ""

    # Create the info.ini file with the required content
    image_filename = os.path.basename(image_path)
    info_ini_content = f"""Title = {title}
Post date = {post_date}
Filename = {image_filename}
Alt text = 
Storyline = 
Characters = 
Tags = 
"""
    info_ini_path = os.path.join(new_folder_path, 'info.ini')
    with open(info_ini_path, 'w') as info_ini_file:
        info_ini_file.write(info_ini_content)

print("Images have been successfully copied into sequential folders with post.txt and info.ini files.")
