from gui.gui import AppGui
from tkinter import Tk


if __name__ == "__main__":
    ventana = Tk() 
    ventana.wm_title("Z_Find 1.0")
    app = AppGui(ventana)
    app.mainloop()
