from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Listbox")
janela.geometry("250x200")

listbox = Listbox(janela, height=8)
listbox.grid(row=0, column=0)

linguagens_programacao = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "Go", "Swift"]

for i in linguagens_programacao:
    listbox.insert(END, i)

#obtem o primeiro item da lista
print(listbox.get(ACTIVE)) #Usar print para visualizar
#obtem item dO INDEX
print(listbox.get(1))
#obtem o INTERVALO
print(listbox.get(1, 2))

janela.mainloop()