from tkinter import font
import tkinter.ttk

from PIL import Image, ImageTk
import PIL.Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('320x400')
root.title("Image converter")
root.config(bg="#ffffff")

image = PIL.Image.open("img.jpg")
test = ImageTk.PhotoImage(image)

Label(image = test, bg="#fff").pack()
Label(root, text="Image converter", font="Verdana 20 bold", fg="#404042", bg="#ffffff").pack()
Label(root, text="@Mirko-r", font="Verdana 20 bold", fg="#404042", bg="#ffffff").pack()

width = IntVar()
height = IntVar()

Label(root, text="Size = ", font="Verdana 10 bold", fg="#404042", bg="#ffffff").place(x=10, y=200)
Label(root, text="X ", font="Verdana 10 bold", fg="#404042", bg="#ffffff").place(x=166, y=200)
Label(root, text="Widht = ", font="Verdana 10 bold", fg="#404042", bg="#ffffff").place(x=70, y=250)
Label(root, text="Height = ", font="Verdana 10 bold", fg="#404042", bg="#ffffff").place(x=195, y=250)

Entry(root, textvariable=width, font="Verdana 10 bold", fg="#404042", bg="#ffffff", borderwidth=3, width=9).place(x=70, y=200)
Entry(root, textvariable=height, font="Verdana 10 bold", fg="#404042", bg="#ffffff", borderwidth=3, width=9).place(x=190, y=200)

Label(root, text="Select Target Format", font="Verdana 10 bold", fg="#404042", bg="#ffffff").place(x=10, y=330)
from1 = StringVar()
jpgto = tkinter.ttk.Combobox(root, width=10, textvariable=from1)
jpgto["values"] = ("PNG", "GIF", "ICO")
jpgto.place(x=190, y=330)
jpgto.current(0)

def ChooseFile():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file", 
                                            filetypes=(
                                                ("JPG File", "*.jpg"),
                                                ("all files", "*.*")
                                            ))
    label_file_explorer.configure(text="File : "+filename)

def StartConvert():
    WSize = width.get()
    HSize = height.get()

    name = filename.split("/")
    finalname = name[-1].replace(".jpeg", "")
    
    with open(str(filename), "r+b") as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [WSize, HSize])
            cover.save(f'{finalname}.{from1.get().strip().lower()}', image.format)

    Label(root, text="Image Convert Successfully", fg="#404042", bg="#ffffff", font="Verdana 10 bold").place(x=57, y=410)

label_file_explorer = Label(root, text="File: ", width=50, height=4, fg="#404042", bg="#ffffff")
label_file_explorer.pack()

Button(root, text="Choose File", bg="#404042", fg="#ffffff", font="Verdana 10 bold", command=ChooseFile).place(x=40, y=300)
Button(root, text="Start Convert", bg="#404042", fg="#ffffff", font="Verdana 10 bold", command=StartConvert).place(x=100, y=300)
Label(root, text="Here, you cam find an image \n converter for your needs \n for example, a jpg to png converter.",
        fg="#404042", bg="#ffffff").place(x = 57, y=430)
root.mainloop()