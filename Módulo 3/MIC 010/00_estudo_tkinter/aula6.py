from tkinter import *
from tkinter.ttk import * #Precisa disso para o combobox funcionar

janela = Tk()
janela.title("Combobox")
janela.geometry("500x500")

combo = Combobox(janela)
combo["values"] = (1, 2, 3, 4, "Par") #Valores a serem selecionados na combobox
combo.current(0) #O parâmetro é o index da lista feita com os valores
combo.grid(row=0, column=0)
def obter():
    v = combo.get() #Vai sempre puxar o valor do .current
    label = Label(janela, text=v)
    label.grid(row=1, column=0)

janela.mainloop()