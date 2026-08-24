import tkinter as tk
from tkinter import ttk

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Senhas da Fila")

        # Tela de entrada
        self.frame_entrada = ttk.Frame(self.root, padding="10")
        self.frame_entrada.grid(row=0, column=0, padx=10, pady=10)

        self.label_entrada = ttk.Label(self.frame_entrada, text="Digite até 4 senhas:")
        self.label_entrada.grid(row=0, column=0, columnspan=2, pady=5)

        self.entradas = []
        for i in range(4):
            ttk.Label(self.frame_entrada, text=f"Senha {i + 1}:").grid(row=i + 1, column=0, padx=5, pady=5)
            entrada = ttk.Entry(self.frame_entrada)
            entrada.grid(row=i + 1, column=1, padx=5, pady=5)
            self.entradas.append(entrada)

        self.botao_adicionar = ttk.Button(self.frame_entrada, text="Adicionar Senhas", command=self.adicionar_senhas)
        self.botao_adicionar.grid(row=5, column=0, columnspan=2, pady=10)

        # Tela de exibição
        self.frame_exibicao = ttk.Frame(self.root, padding="10")
        self.frame_exibicao.grid(row=0, column=50, padx=300, pady=200)

        self.label_exibicao = ttk.Label(self.frame_exibicao, text="Senhas na Fila:")
        self.label_exibicao.grid(row=0, column=0, columnspan=20, pady=50)

        self.senha_labels = []
        for i in range(4):
            label = ttk.Label(self.frame_exibicao, text="", font=("Arial", 30))
            label.grid(row=i + 1, column=0, columnspan=2, pady=5)
            self.senha_labels.append(label)

    def adicionar_senhas(self):
        """Adiciona senhas das entradas à lista e atualiza a tela de exibição."""
        senhas = [entrada.get() for entrada in self.entradas]
        for i, senha in enumerate(senhas):
            if senha:
                self.senha_labels[i].config(text=f"Senha {i + 1}: {senha}")

        # Limpa as entradas após adicionar as senhas
        for entrada in self.entradas:
            entrada.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
