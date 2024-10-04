from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("RadioButton")
janela.geometry("200x200")

rad1 = Radiobutton(janela, text="Primeiro", value=1)#Cada botão tem qu eter um valor diferente
rad1.grid(row=0, column=0)
rad2 = Radiobutton(janela, text="Segundo", value=2)
rad2.grid(row=0, column=1)
rad3 = Radiobutton(janela, text="Terceiro", value=3)
rad3.grid(row=0, column=2)

janela.mainloop()