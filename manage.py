from importlib.resources import path
import os
import shutil
from datetime import datetime
from turtle import title
import PIL.Image
# from PIL import Image

# Código abaixo é para rodar o programa onde as fotos estão!!!
# from tkinter import *
# import tkinter.filedialog

# janela = Tk()

# folder = tkinter.filedialog.askdirectory(title = 'Selecione a pasta que contem as fotos para ser organizadas')

# janela.destroy()



extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']

def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%y-%m-%d')

def photo_shooting_date(file):
    photo = PIL.Image.open(file)
    info = photo._getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

def move_photo(file):
    new_folder = folder_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file, new_folder + '/' + file)

def organize():
    photos = [
        filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
    ]
    for filename in photos:
        move_photo(filename)


print(organize())
