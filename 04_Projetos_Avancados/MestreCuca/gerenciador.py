import sqlite3
import datetime as dt
from collections import defaultdict
from transacao import Transacao
from usuario import Usuario

class Gerenciador:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self._inicializar_db()
        self.carregar_registros()

    # Método auxiliar para sempre retornar uma nova conexão
    def _get_connection(self):
        return sqlite3.connect(self.usuario.arquivo)

    def _inicializar_db(self):
        # O 'with' garante que a conexão será fechada após executar o bloco
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    valor REAL NOT NULL,
                    data TEXT NOT NULL
                )
            """)
            conn.commit()

    def carregar_registros(self):
        self.usuario.transacoes = []
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, tipo, descricao, valor, data FROM transacoes ORDER BY data DESC")
            for row in cursor.fetchall():
                data_obj = dt.datetime.fromisoformat(row[4])
                transacao = Transacao(row[1], row[2], row[3], data_obj, id_transacao=row[0])
                self.usuario.transacoes.append(transacao)

    def registrar(self, tipo, descricao, valor, data=""):
        transacao = Transacao(tipo, descricao, valor, data)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO transacoes (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)",
                (transacao.tipo, transacao.descricao, transacao.valor, transacao.data.isoformat())
            )
            conn.commit()
        self.carregar_registros()

    def limpar_historico(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transacoes")
            conn.commit()
        self.usuario.transacoes = []

    def excluir_transacao(self, transacao_a_excluir):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transacoes WHERE id = ?", (transacao_a_excluir.id,))
            conn.commit()
        self.carregar_registros()

    def editar_transacao(self, transacao_original, novos_dados):
        nova_data_obj = transacao_original.validar_data(novos_dados['data'])
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE transacoes SET tipo = ?, descricao = ?, valor = ?, data = ?
                WHERE id = ?
            """, (
                novos_dados['tipo'], novos_dados['descricao'], novos_dados['valor'],
                nova_data_obj.isoformat(), transacao_original.id
            ))
            conn.commit()
        self.carregar_registros()
        
    def saldo(self):
        return sum(t.valor if t.tipo == "ganho" else -t.valor for t in self.usuario.transacoes)

    def get_resumo_mensal(self):
        resumo = defaultdict(lambda: {'ganhos': 0, 'gastos': 0})
        for t in self.usuario.transacoes:
            chave_mes = t.data.strftime("%Y-%m")
            if t.tipo == "ganho":
                resumo[chave_mes]['ganhos'] += t.valor
            else:
                resumo[chave_mes]['gastos'] += t.valor
                
        resumo_ordenado = dict(sorted(resumo.items()))
        return resumo_ordenado

    def get_resumo_diario_por_mes(self,  ano, mes):
        resumo = defaultdict(lambda: {'ganhos' : 0,  'gastos': 0})
        transacoes_filtradas = [
            t for t in self.usuario.transacoes
            if t.data.year == ano and t.data.month == mes
        ]
        for t in transacoes_filtradas:
            chave_dia = t.data.strftime("%d")
            if t.tipo == "ganho":
                resumo[chave_dia]['ganhos'] += t.valor
            else:
                resumo[chave_dia]['gastos'] += t.valor
                
        resumo_ordenado = dict(sorted(resumo.items()))
        return resumo_ordenado

    def gerar_relatorio_texto(self):
        soma_ganhos = sum(t.valor for t in self.usuario.transacoes if t.tipo == "ganho")
        soma_gastos = sum(t.valor for t in self.usuario.transacoes if t.tipo == "gasto")
        
        resumo_mensal = self.get_resumo_mensal()
        
        media_ganhos = 0
        if any(v['ganhos'] > 0 for v in resumo_mensal.values()):
            soma_media = sum(v['ganhos'] for v in resumo_mensal.values())
            media_ganhos = soma_media / len(resumo_mensal)
            
        relatorio = f"RELATÓRIO FINANCEIRO - {self.usuario.nome.upper()}\n"
        relatorio += "=" * 40 + "\n\n"
        
        relatorio += "RESUMO MENSAL DETALHADO:\n"
        for mes, valores in resumo_mensal.items():
            relatorio += (
                f"Mês {mes}:\n"
                f"  - Ganhos: R$ {valores['ganhos']:.2f}\n"
                f"  - Gastos: R$ {valores['gastos']:.2f}\n\n"
            )
            
        relatorio += "=" * 40 + "\n\n"
        relatorio += "HISTÓRICO COMPLETO DE TRANSAÇÕES:\n"
        
        transacoes_ordenadas = sorted(self.usuario.transacoes, key=lambda t: t.data)
        for t in transacoes_ordenadas:
            relatorio += f"- {t}\n"
            
        relatorio += "\n" + "=" * 40 + "\n\n"
        relatorio += "RESUMO GERAL:\n"
        relatorio += f"- Total de Ganhos: R$ {soma_ganhos:.2f}\n"
        relatorio += f"- Total de Gastos: R$ {soma_gastos:.2f}\n"
        relatorio += f"- Saldo Final: R$ {self.saldo():.2f}\n"
        relatorio += f"- Média Mensal de Ganhos: R$ {media_ganhos:.2f}\n"
        
        return relatorio