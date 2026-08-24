#Criação de uma interface grafica usando tkinter

import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira interface")
janela.geometry("450x240")

mensagem = tk.Label(janela, text="Hello Word!")
mensagem.pack(pady=30)
tk.Button(janela, text="Continuar").pack()
tk.Text(janela).pack(pady=10, padx= 10)

janela.mainloop()