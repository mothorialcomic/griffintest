import glob
import os.path
import shutil

mydir = r"C:\Users\metaj\Downloads\Rick Griffin Comics\Comics Holding Spot\Housepets"
comicsfolder = r"C:\Users\metaj\Documents\GitHub\griffintest\your_content\housepets\comics"
i = 1
book_list = sorted(glob.glob(mydir+r"\*"), key=lambda s: int(os.path.basename(s)[5:]))
for book_path in book_list:
    print(book_path)
    file_list = glob.glob(book_path + "/*.png")  # Include slash or it will search in the wrong directory!!
    book_name = os.path.basename(book_path)
    for file_path in sorted(file_list):
        file_name = os.path.basename(file_path)
        date = file_name[:10]
        title = file_name[11:-4].replace("-", " ").title()
        title = title.replace("Im", "I'm").replace("Aint", "Ain't").replace("Cant", "Can't").replace("Didnt", "Didn't").replace("Doesnt", "Doesn't").replace("Dont", "Don't").replace("Hadnt", "Hadn't").replace("Hasnt", "Hasn't").replace("Havent", "Haven't").replace("Hed", "He'd").replace("Hes", "He's").replace("Shes", "She's").replace("Id", "I'd").replace("Hows", "How's").replace("Howd", "How'd").replace("Ill", "I'll").replace("Ive", "I've").replace("Isnt", "Isn't").replace("Itll", "It'll").replace("Its", "It's").replace("Lets", "Let's").replace("Shell", "She'll").replace("Theyll", "They'll").replace("Werent", "Weren't").replace("Youd", "You'd").replace("Youll", "You'll")
        foldername = "{:04}".format(i)
        os.mkdir(os.path.join(comicsfolder, foldername))
        shutil.copy(file_path, os.path.join(comicsfolder, foldername, file_name))
        with open(os.path.join(comicsfolder, foldername, "info.ini"), "w") as f:
            f.write(f"""Title = {title}
Post date = {date}
Filename = {file_name}
Alt text = 
Storyline = {book_name}
Characters = 
Tags = """)
        with open(os.path.join(comicsfolder, foldername, "post.txt"), "w") as f:
            f.write("")
        i += 1
