from tkinter import Frame, Label, Button, Entry


class AppGui(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=520, height=170)
        self.master = master
        self.pack()
        self.crear_componentes()


    def crear_componentes(self):
        # se crean los componentes
        self.btn_buscar = Button(self, text="Buscar", command=None)
        self.lbl_buscar_mac = Label(self, text="Buscar")
        self.txt_mac = Entry(self)

        # se posicionan los componentes
        self.btn_buscar.pack()
        self.lbl_buscar_mac.pack()
        self.txt_mac.pack()


    def formatear_mac(self, MAC: str):
        pass
