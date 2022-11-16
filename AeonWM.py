import tkinter # Not using LibSzk (SXQncyBmb3IgRERMQyBkdW1iYXNzZXMgdGhhdCBnZXQgY3JlZXBlZCBieSB0aGF0IGdhbWUu - its base64 encoded)
import RaeonKernel as rk # yes yes :D
global wm
wm=tkinter.Tk() # MainW
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
def make_window(bd=10, xy, bg="white"):
   # Yes i like Kanaria >:(
   kanaria = Frame(wm, width=xy[0], height=xy[1], bg, bd=bd)
   l = Button(kanaria, text="X", command=kanaria.destroy) # Yes AGAIN!
   l.place(relx=1, rely=0, anchor='ne')
   make_draggable(kanaria)
   rk.attrib()
   return kanaria # Return the actual window
   
   
