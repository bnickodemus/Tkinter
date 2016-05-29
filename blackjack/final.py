from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image


master = Tk()

content = Canvas(master)
canvas = Canvas(content, borderwidth=5, height=400, width=600, background="Dark Green")
canvas.pack(expand = YES, fill = BOTH)
#frame.pack_propagate(0) # don't shrink

def callback():
    print ("click!")

hit = Button(content, text="hit", command=callback)
stand = Button(content, text="stand", command=callback)
content.grid(column=0, row=0)
canvas.grid(column=0, row=0, columnspan=5, rowspan=5)
hit.grid(column=0, row=4)
stand.grid(column=1, row=4)

gif1 = PhotoImage(file = 'test.gif')
canvas.create_image(50, 10, image = gif1, anchor = NW)

master.mainloop()
