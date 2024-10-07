from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry("300x300")

frame_1 = Frame(janela, width=300, height=100, bg="red")
frame_1.grid(row=0, column=0)
frame_2 = Frame(janela, width=300, height=100, bg="green")
frame_2.grid(row=1, column=0)
frame_3 = Frame(janela, width=300, height=100, bg="blue")
frame_3.grid(row=2, column=0)

janela.mainloop()