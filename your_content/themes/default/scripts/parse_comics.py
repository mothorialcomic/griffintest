import os
import shutil

# Define the origin and destination directories
origin_dir = r'C:\Users\metaj\Downloads\Rick Griffin Comics\Comics Holding Spot\Hayven Celestia\Skinchange SFW'
destination_dir = r'C:\Users\metaj\Documents\GitHub\griffintest\your_content\skinchange\comics'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# List of dates for the 'Post date' field (currently empty)
dates = [
    "2021-10-08", "2021-10-19", "2021-11-05",
    "2021-11-23", "2021-12-10", "2021-12-25",
    "2021-12-28", "2022-01-14", "2022-02-01",
    "2022-02-18", "2022-03-08", "2022-03-25",
    "2022-04-12", "2022-04-29", "2022-05-17",
    "2022-06-03", "2022-06-21", "2022-07-08",
    "2022-07-26", "2022-08-12", "2022-08-30",
    "2022-09-16", "2022-10-04", "2022-10-21",
    "2022-11-08", "2022-11-25", "2022-12-13",
    "2022-12-25", "2023-01-06", "2023-01-24",
    "2023-02-10", "2023-02-28", "2023-03-07",
    "2023-04-07", "2023-04-14", "2023-04-25",
    "2023-05-02", "2023-05-12", "2023-05-19",
    "2023-05-26", "2023-06-02", "2023-06-09",
    "2023-06-16", "2023-10-20", "2023-10-23",
    "2023-10-27", "2023-10-30", "2023-11-03",
    "2023-11-06", "2023-11-10", "2023-11-13",
    "2023-11-17", "2023-11-20", "2023-11-24",
    "2023-11-27", "2023-12-01", "2023-12-04",
    "2023-12-08", "2023-12-11", "2023-12-15"
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
    title = f"Skinchange - Page {image_index}"

    # Get the post date for the current image if dates list is provided
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
