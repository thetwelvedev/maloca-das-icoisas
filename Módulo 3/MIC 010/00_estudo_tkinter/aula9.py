from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Listbox")
janela.geometry("250x200")

listbox = Listbox(janela, height=8)
listbox.grid(row=0, column=0)

def test():
    print(listbox.get(ACTIVE))
    l = Label(janela, text=listbox.get(ACTIVE), width=20)
    l.grid(row=0, column=1)


linguagens_programacao = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "Go", "Swift"]

for i in linguagens_programacao:
    listbox.insert(END, i)

b = Button(janela, text="Imprimir", command=test)
b.grid(row=1, column=0)

janela.mainloop()