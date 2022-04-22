from tkinter import *
from PIL import Image, ImageTk
mahmudul_root = Tk()
mahmudul_root.geometry("1255x944")
# image = Image.open("C:\Users\dell\Desktop\login_form\back.png")
photo = PhotoImage(file="back.jpg")
varun_label = Label(image=photo)
varun_label.pack()
mahmudul_root.mainloop()