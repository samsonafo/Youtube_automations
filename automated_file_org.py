import os
import shutil #high level operations on files and collections of files


#define directories
desktop_dir = "/Users/samson.afolabi/Desktop/"
destination_dir = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
   "Videos": [".mp4", ".mkv", ".avi",".mov"], 

}


#organise files
for filename in os.listdir(desktop_dir):
    src_path = os.path.join(desktop_dir, filename)
    if os.path.isfile(src_path):
        ext = os.path.splitext(filename)[1]
        for folder, extensions in destination_dir.items():
            if ext in extensions:
                dest_dir = os.path.join(desktop_dir, folder)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(src_path, dest_dir)
                break

print("Files organized.")