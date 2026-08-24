import os 

class Usuario:
    def __init__(self, nome: str):
        self.nome = nome.strip().lower()
        self.pasta = 'registros'
        os.makedirs(self.pasta, exist_ok=True)
        self.arquivo = os.path.join(self.pasta, f"{self.nome}.db")
        self.transacoes = []

    def __str__(self):
        return f"Usuário: {self.nome}, Registros: {len(self.transacoes)}"
