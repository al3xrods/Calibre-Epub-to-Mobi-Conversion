import os
import glob
import shutil
import time

path = os.path.join("C:", "Users", "97254", "Downloads")
moveto = os.path.join("C:", "Users", "97254", "Documents", "Calibre Books")

files = [f for f in os.listdir(path) if f.endswith('.epub')]

try:
    for f in files:
        src = os.path.join(path, f)
        dest = os.path.join(moveto, f)
        os.replace(src, dest)

    print('Epub Files Transferred Successfully.')
except FileNotFoundError:
    print('Epub Files not found.')

#=================================================
# Calibre Book Conversion
os.system('start "" "' + os.path.join("C:", "Program Files", "Calibre2", "calibre.exe") + '"') #Open Calibre
time.sleep(10)
user_input = str(input('Transfer Books? (Y/N) ')).lower()

books_path = os.path.join(path, "New Folder")
files_path = glob.glob(os.path.join(books_path, "**", "*"), recursive=True)

if user_input == 'y':
    try:
        for file in files_path:
            if file.endswith('.mobi'):
                with open(file, 'rb') as f:
                    shutil.move(file, path) # move all .mobi files to Downloads folder.
        print('Converted books transferred.')
        time.sleep(2)
        os.system("taskkill /f /im calibre.exe") # Terminate Calibre
        time.sleep(1)

    except FileNotFoundError:
        print('Files Not Found.')
    except Exception as e:
       print("All Done!")
