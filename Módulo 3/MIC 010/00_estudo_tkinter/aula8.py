from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("RadioButton")
janela.geometry("200x200")

def obter():
    print(f"O valor do botão selecionado é {selecionado.get()}.")

selecionado = StringVar()

rad1 = Radiobutton(janela, text="Primeiro", value="Primeiro", var=selecionado, command=obter)#Cada botão tem qu eter um valor diferente
rad1.grid(row=0, column=0)
rad2 = Radiobutton(janela, text="Segundo", value="Segundo", var=selecionado, command=obter)
rad2.grid(row=0, column=1)
rad3 = Radiobutton(janela, text="Terceiro", value="Terceiro", var=selecionado, command=obter)
rad3.grid(row=0, column=2)

janela.mainloop()