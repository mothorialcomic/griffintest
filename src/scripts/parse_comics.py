import glob
import os.path

mydir = r"C:\Users\metaj\Downloads\Rick Griffin Comics\Comics Holding Spot\Housepets\Book 1"

file_list = glob.glob(mydir + "/*.png") # Include slash or it will search in the wrong directory!!
for file_path in sorted(file_list):
    file_name = os.path.basename(file_path)
    print (file_name)
