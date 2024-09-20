from tkinter import * # carrega todos os módulos da biblioteca

def sair():
 janela.destroy()
janela = Tk()
janela.configure(background='green')
janela.geometry('500x400')
janela.title("Controle de Relés via interface gráfica")
btn = Button(janela,text="Sair", command = sair)
btn.pack(padx=100,pady=100)
janela.mainloop()