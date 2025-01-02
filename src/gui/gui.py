from tkinter import Frame


class AppGui(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.crear_componentes()

    def crear_componentes(self):
        #self.btn_buscar = None
        #self.lbl = None
        pass
    