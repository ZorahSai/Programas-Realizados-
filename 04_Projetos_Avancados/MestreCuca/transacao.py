import datetime as dt


class Transacao:
    def __init__(self, tipo: str, descricao: str, valor: float, data: str = "", id_transacao =None):
        self.id = id_transacao
        self.tipo = tipo.lower()  
        self.descricao = descricao
        self.valor = float(valor)
        self.data = self.validar_data(data)

    def validar_data(self, data_str):
        """Valida data no formato dd/mm/aaaa e impede datas futuras, gerando exceções para a interface tratar."""
        if isinstance(data_str, dt.datetime):
            return data_str
            
        if not data_str:
            return dt.datetime.now()
            
        try:
            data = dt.datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data inválida! Digite no formato dd/mm/aaaa.")
            
        hoje = dt.datetime.today()
        if data > hoje:
            raise ValueError("A data não pode estar no futuro!")
            
        return data
            
    def __str__(self):
        return f"[{self.data.strftime('%d/%m/%Y')}] {self.tipo.upper()} - {self.descricao} : R$ {self.valor:.2f}"
    
