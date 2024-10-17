from tkinter import *
from tkinter.colorchooser import *
# ---------------------------------
root = Tk()
root.title("Color Picker")
root.iconbitmap('assets/icon.ico')
frame = Frame(root)
# ---------------------------------
def copy(txt):
    root.clipboard_append(txt)
    
def getColor():
    color = askcolor(title='choose your color')
    top = Toplevel()
    top.iconbitmap('assets/icon.ico')
    Label(top, text='RGB: {}'
          '\n'
          'HASH: {}'.format(color[0], color[1])).pack()
    Button(top, text='copy RGB', command=lambda: copy(color[0])).pack()
    Button(top, text='copy HASH', command=lambda: copy(color[1])).pack()
    
Button(frame, text='Select Color', command=getColor).pack()
frame.pack()
mainloop()
