from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Checkbutton")
janela.geometry("200x200")

chek = Checkbutton(janela, text="escolha")
chek.grid(row=0, column=0)
#https://youtu.be/Rt2KsysJpGE?si=dD8Zr3R0uRwuOCNk

janela.mainloop()