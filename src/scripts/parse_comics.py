import os
import shutil

# Define the base directory where the issues are located
base_dir = r'C:\Users\metaj\Downloads\Rick Griffin Comics\Comics Holding Spot\A&H Club'
# Define the new output base directory where the images will be placed
output_base_dir = r'C:\Users\metaj\Documents\GitHub\griffintest\your_content\ah-club\comics'

# Ensure the output base directory exists
os.makedirs(output_base_dir, exist_ok=True)

# Get the list of issue directories, sorted to process them in order
issue_dirs = sorted(
    [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith('Issue')])

global_image_count = 1

# List of dates for the 'Post date' field
dates = [
    "2015-06-19", "2015-06-19", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12",
    "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12",
    "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12",
    "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12", "2015-07-12",
    "2015-07-12", "2015-07-21", "2015-07-25", "2015-08-01", "2015-08-09", "2015-09-19",
    "2015-09-26", "2015-10-03", "2015-10-24", "2015-10-31", "2015-11-15", "2015-12-05",
    "2016-01-16", "2016-02-13", "2016-02-20", "2016-02-27", "2016-03-05", "2016-03-19",
    "2016-04-09", "2016-04-23", "2016-05-29", "2016-06-18", "2016-07-23", "2016-07-30",
    "2016-08-27", "2016-09-17", "2016-09-24", "2016-10-01", "2016-10-08", "2016-10-14",
    "2016-10-22", "2016-10-29", "2016-11-05", "2016-11-12", "2016-12-03", "2016-12-10",
    "2017-01-07", "2017-01-14", "2017-02-11", "2017-03-03", "2017-04-15", "2017-04-22",
    "2017-05-20", "2017-06-17", "2017-07-01", "2017-07-22", "2017-08-12", "2017-09-16",
    "2017-10-21", "2017-10-28", "2017-11-25", "2018-01-06", "2018-01-20", "2018-03-24",
    "2018-04-07", "2018-08-25", "2018-09-01", "2018-09-21", "2018-10-13", "2018-10-27",
    "2018-11-17", "2018-12-01", "2019-01-26", "2019-02-23", "2019-03-09", "2019-04-06",
    "2019-04-27", "2019-05-18", "2019-06-08", "2019-07-13", "2019-08-24", "2019-09-14",
    "2019-10-19", "2019-11-30", "2020-01-25", "2020-02-15", "2020-02-29", "2020-03-14",
    "2020-03-21", "2020-03-28", "2020-08-22", "2020-08-29", "2020-09-05", "2020-09-19",
    "2020-10-03", "2020-10-17", "2020-12-12", "2021-01-02", "2021-01-31", "2021-02-27",
    "2021-04-03", "2021-04-24", "2021-05-01", "2021-06-06", "2021-06-29", "2021-07-03",
    "2021-07-10", "2021-08-14", "2021-08-21", "2021-10-01", "2021-10-26", "2021-11-11",
    "2021-12-01", "2021-12-17", "2022-01-04", "2022-01-21", "2022-02-08", "2022-02-25",
    "2022-03-15", "2022-04-01", "2022-04-19", "2022-05-06", "2022-05-24", "2022-06-10",
    "2022-06-28", "2022-07-15", "2022-08-02", "2022-08-20", "2022-09-06", "2022-09-23",
    "2022-10-11", "2022-10-28", "2022-11-15", "2022-12-01", "2022-12-20", "2023-01-13",
    "2023-01-31", "2023-02-17"
]

# Ensure the date list is long enough
if len(dates) < sum(len(os.listdir(os.path.join(base_dir, d))) for d in issue_dirs):
    raise ValueError("Not enough dates provided for the number of images.")

# Go through each issue directory
for issue_index, issue_dir in enumerate(issue_dirs, start=1):
    issue_path = os.path.join(base_dir, issue_dir)

    # Get the list of images in the current issue directory, sorted to process them in order
    images = sorted([f for f in os.listdir(issue_path) if os.path.isfile(os.path.join(issue_path, f))])

    # Go through each image in the current issue directory
    for local_image_count, image in enumerate(images, start=1):
        image_path = os.path.join(issue_path, image)

        # Create a new directory for the current image
        new_folder_name = f"{global_image_count:03d}"
        new_folder_path = os.path.join(output_base_dir, new_folder_name)
        os.makedirs(new_folder_path, exist_ok=True)

        # Copy the image to the new directory
        shutil.copy(image_path, os.path.join(new_folder_path, image))

        # Create an empty post.txt file in the new directory
        post_txt_path = os.path.join(new_folder_path, 'post.txt')
        with open(post_txt_path, 'w') as post_txt_file:
            pass  # Create an empty file

        # Determine the title for the info.ini file
        if local_image_count == 1:
            title = f"A&H Club #{issue_index} Cover"
        else:
            title = f"A&H Club #{issue_index} Page {local_image_count - 1}"

        # Get the post date for the current image
        post_date = dates[global_image_count - 1]

        # Debug: Print the folder name and post date to check alignment
        print(f"Creating folder: {new_folder_name}, Post date: {post_date}")

        # Create the info.ini file with the required content
        image_filename = os.path.basename(image_path)
        info_ini_content = f"""Title = {title}
Post date = {post_date}
Filename = {image_filename}
Alt text = 
Storyline = {issue_dir}
Characters = 
Tags = 
"""
        info_ini_path = os.path.join(new_folder_path, 'info.ini')
        with open(info_ini_path, 'w') as info_ini_file:
            info_ini_file.write(info_ini_content)

        # Increment the global image count
        global_image_count += 1

print("Images have been successfully copied into sequential folders with post.txt and info.ini files.")
