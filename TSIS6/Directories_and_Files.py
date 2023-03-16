import os
path = "./files/txt.py"
# 1
#print(os.listdir(path = "./files"))

# 2
#print(os.access(path, os.F_OK)) # - объект существует
#print(os.access(path, os.R_OK)) # - доступен на чтение
#print(os.access(path, os.W_OK)) # - доступен на запись
#print(os.access(path, os.X_OK)) # - доступен на исполнение

# 3
#if os.path.exists(path): # True
#    basename = os.path.basename(path) # - базовое имя пути
#    dirname = os.path.dirname(path) # - возвращает имя директории пути path
    #print(basename)
    #print(dirname)
#else: # False
    #print("The path does not exist")

# 4

# 5

# 6
#import string
#files = string.ascii_uppercase
#for i in files:
#    file_name = i + ".txt"
#    with open(file_name, "w") as file:
#        file.write("Hello World!")

# 7
import shutil
#shutil.copy(r"C:\Users\Hito\Code\TSIS6\files\text.txt", "text_1.txt")

# 8
#if os.path.exists(r"C:\Users\Hito\Code\A.txt"):
#    os.remove(r"C:\Users\Hito\Code\A.txt")
#else:
#    print("The file does not exist")