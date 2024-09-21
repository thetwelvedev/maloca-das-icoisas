from tkinter import *
from tkinter import messagebox

def acionar_bluetooth():
    print("Bluetooth acionado!")
    messagebox.showinfo("Bluetooth", "Mecanismo via Bluetooth foi acionado!")

def fechar():
    print("Fechando interface...")
    janela.destroy()

# janela principal
janela = Tk()
janela.title("Controle de Dispositivos")
janela.configure(background='dark blue')
janela.geometry("300x200")

# mensagem na tela
mensagem = Label(janela, text="Conecte-se ao Blutooth", bg='grey', fg='white', font=('Arial', 10))
mensagem.pack(pady=20)

# botões

btn_bluetooth = Button(janela, text="Conectar Bluetooth", command=acionar_bluetooth)
btn_bluetooth.configure(background='grey', fg='white')
btn_bluetooth.pack(pady=10)

btn_sair = Button(janela, text="Fechar", command=fechar)
btn_sair.configure(background='grey', fg='white')
btn_sair.pack(pady=10)

# Execução da janela principal
janela.mainloop()
