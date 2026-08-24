# Mestre_Cuca
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pdfplumber  
import re
from usuario import Usuario
from gerenciador import Gerenciador
import datetime as dt
from collections import defaultdict
from processador_pdf import extrair_transacoes_pdf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuração global do tema
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")
def validar_valor(valor_str):
    try:
        valor_corrigido = valor_str.replace(',', '.', 1)
        return float(valor_corrigido)
    except (ValueError, TypeError):
        return None

class GraficoView(ctk.CTkFrame):
    def __init__(self, parent, gerenciador, callback_voltar):
        super().__init__(parent, fg_color="transparent")
        self.gerenciador = gerenciador
        self.callback_voltar = callback_voltar # Função para voltar para a tabela

        self.meses = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 
            5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 
            9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }

        # Barra superior do gráfico (Botão Voltar + Filtros)
        frame_filtros = ctk.CTkFrame(self, fg_color="transparent")
        frame_filtros.pack(fill='x', pady=(0, 10))

        # Botão de Voltar
        ctk.CTkButton(frame_filtros, text="⬅ Voltar à Tabela", width=120, 
                      command=self.callback_voltar, fg_color="#555555", 
                      hover_color="#333333").pack(side="left", padx=(0, 20))

        ctk.CTkLabel(frame_filtros, text="Ano:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        self.combo_ano = ctk.CTkComboBox(frame_filtros, state="readonly", width=100)
        self.combo_ano.pack(side="left", padx=5)

        ctk.CTkLabel(frame_filtros, text="Mês:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        self.combo_mes = ctk.CTkComboBox(frame_filtros, state="readonly", width=130)
        self.combo_mes.pack(side="left", padx=5)
        
        ctk.CTkButton(frame_filtros, text="Gerar Gráfico", command=self.gerar_grafico).pack(side="left", padx=15)

        # Área onde o desenho do gráfico vai aparecer
        self.frame_grafico = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_grafico.pack(fill="both", expand=True)
        self.canvas = None

        self.popular_filtros()

    def popular_filtros(self):
        # Transforma os anos em texto para o CTkComboBox
        anos = sorted(list(set(str(t.data.year) for t in self.gerenciador.usuario.transacoes)))
        if not anos:
            anos = [str(dt.date.today().year)]
            
        self.combo_ano.configure(values=anos)
        self.combo_ano.set(anos[-1])

        meses_nomes = list(self.meses.values())
        self.combo_mes.configure(values=meses_nomes)
        mes_atual = dt.date.today().month
        self.combo_mes.set(self.meses[mes_atual])

    def gerar_grafico(self):
        ano_str = self.combo_ano.get()
        mes_str = self.combo_mes.get()

        if not ano_str or not mes_str:
            messagebox.showerror("Erro", "Por favor, selecione um ano e um mês.")
            return

        ano = int(ano_str)
        mes_para_numero = {nome: num for num, nome in self.meses.items()}
        mes_numero = mes_para_numero[mes_str]
        
        resumo_diario = self.gerenciador.get_resumo_diario_por_mes(ano, mes_numero)
        if not resumo_diario:
            messagebox.showinfo("Sem Dados", f"Nenhuma transação encontrada para {mes_str} de {ano}.")
            return

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        dias = list(resumo_diario.keys())
        ganhos = [v['ganhos'] for v in resumo_diario.values()]
        gastos = [v['gastos'] for v in resumo_diario.values()]
        
        fig = Figure(figsize=(10, 5), dpi=100)
        ax = fig.add_subplot(111)
        x = np.arange(len(dias))
        width = 0.4
        
        rects1 = ax.bar(x - width/2, ganhos, width, label='Ganhos', color='#28a745')
        rects2 = ax.bar(x + width/2, gastos, width, label='Gastos', color='#dc3545')
        
        ax.set_ylabel('Valor (R$)')
        ax.set_title(f'Resumo Diário - {mes_str}/{ano}')
        ax.set_xticks(x)
        ax.set_xticklabels(dias)
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        ax.bar_label(rects1, padding=3, fmt='%.2f')
        ax.bar_label(rects2, padding=3, fmt='%.2f')
        fig.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Trocando ttk.Label e ttk.Entry por CTkLabel e CTkEntry
        label = ctk.CTkLabel(self, text="Bem-vindo ao Mestre Cuca!", font=ctk.CTkFont(size=24, weight="bold"))
        label.pack(pady=(60, 20))
        
        label_user = ctk.CTkLabel(self, text="Digite seu nome de usuário:", font=ctk.CTkFont(size=14))
        label_user.pack(pady=(20, 5))
        
        self.user_entry = ctk.CTkEntry(self, width=250, placeholder_text="Ex: João")
        self.user_entry.pack(pady=10)
        self.user_entry.bind("<Return>", self.on_login_press)
        
        # Trocando ttk.Button por CTkButton
        login_button = ctk.CTkButton(self, text="Entrar", command=self.login, width=150)
        login_button.pack(pady=20)

    def login(self):
        username = self.user_entry.get().strip()
        if not username: 
            messagebox.showwarning("Atenção", "O nome de usuário não pode estar em branco.")
            return
        self.user_entry.delete(0, tk.END)
        self.controller.show_app_page(username)

    def on_login_press(self, event): 
        self.login()


class MainController(ctk.CTk): # Herda de CTk ao invés de tk.Tk
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mestre Cuca Finanças")
        self.geometry("500x400")
        
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.current_app_frame = None
        self.login_frame = LoginPage(container, self)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.show_login_page()

    def show_app_page(self, username):
        self.geometry("950x600")
        usuario = Usuario(username)
        gerenciador = Gerenciador(usuario)
        self.current_app_frame = App(self.login_frame.master, self, gerenciador)
        self.current_app_frame.grid(row=0, column=0, sticky="nsew")
        self.current_app_frame.tkraise()

    def show_login_page(self):
        self.geometry("500x400")
        if self.current_app_frame: 
            self.current_app_frame.destroy()
            self.current_app_frame = None
        self.login_frame.tkraise()

class App(ctk.CTkFrame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.controller = controller
        self.gerenciador = gerenciador
        
        # Configuração do Grid Principal da tela
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ==========================================
        # 1. BARRA SUPERIOR (Apenas para o botão Menu)
        # ==========================================
        self.top_bar = ctk.CTkFrame(self, height=45, corner_radius=0)
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        self.btn_menu = ctk.CTkButton(
            self.top_bar, 
            text="☰ MENU", 
            width=60, 
            command=self.toggle_menu,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.btn_menu.pack(side="left", padx=10, pady=5)
        
        # ==========================================
        # 2. MENU LATERAL RETRÁTIL (Com barra de rolagem)
        # ==========================================
        # CTkScrollableFrame cria a rolagem automática para telas pequenas
        self.sidebar_frame = ctk.CTkScrollableFrame(self, width=200, corner_radius=0)
        self.menu_visible = False # Estado inicial: Menu oculto
        
        # Adicionando os botões na aba lateral
        ctk.CTkButton(self.sidebar_frame, text="Registrar Ganho", command=self.registrar_ganho).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="Registrar Gasto", command=self.registrar_gasto).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="Importar PDF", command=self.importar_pdf).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="Mostrar Saldo", command=self.mostrar_saldo).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="Imprimir Relatório", command=self.imprimir_relatorio).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="Mostrar Gráfico", command=self.mostrar_janela_grafico).pack(pady=10, padx=10, fill="x")
        
        # Botão de Logout com cor vermelha para destacar no final da barra
        ctk.CTkButton(self.sidebar_frame, text="Trocar Usuário", command=self.logout, fg_color="#C93B3B", hover_color="#A32A2A").pack(pady=(30, 10), padx=10, fill="x")
        
        # ==========================================
        # 3. ÁREA PRINCIPAL (Tabela Treeview)
        # ==========================================
        self.container_direito = ctk.CTkFrame(self, fg_color="transparent")
        self.container_direito.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.container_direito.grid_rowconfigure(0, weight=1)
        self.container_direito.grid_columnconfigure(0, weight=1)
        
        # A) Frame da Tabela (O que aparece por padrão)
        self.tabela_frame = ctk.CTkFrame(self.container_direito, fg_color="transparent")
        self.tabela_frame.grid_rowconfigure(0, weight=1)
        self.tabela_frame.grid_columnconfigure(0, weight=1)
        
        # B) Frame do Gráfico (Inicia vazio)
        self.grafico_frame = None 
        
        colunas = ('data', 'tipo', 'descricao', 'valor')
        self.tree = ttk.Treeview(self.tabela_frame, columns=colunas, show='headings')
        self.tree.heading('data', text='Data')
        self.tree.heading('tipo', text='Tipo')
        self.tree.heading('descricao', text='Descrição')
        self.tree.heading('valor', text='Valor (R$)')
        
        scrollbar = ttk.Scrollbar(self.tabela_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        self.tree.tag_configure('ganho', foreground='green')
        self.tree.tag_configure('gasto', foreground='red')
        
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Editar Lançamento", command=self.editar_lancamento)
        self.context_menu.add_command(label="Excluir Lançamento", command=self.excluir_lancamento)
        self.tree.bind("<Button-3>", self.mostrar_context_menu)
        
        self.atualizar_historico()
        
        # Inicia o programa mostrando a tabela
        self.mostrar_tabela()

    # ==============================================================
    # MÉTODOS DE TROCA DE TELA (SPA)
    # ==============================================================
    def mostrar_tabela(self):
        """Esconde o gráfico e volta a exibir a tabela de lançamentos"""
        if self.grafico_frame:
            self.grafico_frame.grid_forget()
        self.tabela_frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_janela_grafico(self):
        """Esconde a tabela e exibe a interface de gráficos na mesma tela"""
        if not self.gerenciador.usuario.transacoes:
            messagebox.showinfo("Gráfico", "Não há transações registradas para gerar um gráfico.")
            return
            
        # 1. Oculta a tabela
        self.tabela_frame.grid_forget()
        
        # 2. Destrói o gráfico antigo (se existir) para liberar memória
        if self.grafico_frame:
            self.grafico_frame.destroy()
            
        # 3. Cria e exibe a tela de gráfico, passando a função 'mostrar_tabela' como botão de voltar
        self.grafico_frame = GraficoView(self.container_direito, self.gerenciador, self.mostrar_tabela)
        self.grafico_frame.grid(row=0, column=0, sticky="nsew")

    def toggle_menu(self):
        """Esconde ou mostra a aba lateral de opções"""
        if self.menu_visible:
            # Oculta o frame
            self.sidebar_frame.grid_forget()
            self.menu_visible = False
        else:
            # Mostra o frame fixado na esquerda
            self.sidebar_frame.grid(row=1, column=0, sticky="ns")
            self.menu_visible = True
    def logout(self): self.controller.show_login_page()
    def atualizar_historico(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for transacao in self.gerenciador.usuario.transacoes:
            valor_formatado, data_formatada, tag_cor = f"{transacao.valor:.2f}", transacao.data.strftime('%d/%m/%Y'), transacao.tipo
            self.tree.insert('', tk.END, values=(data_formatada, transacao.tipo.upper(), transacao.descricao, valor_formatado), tags=(tag_cor,))
    def find_transacao_by_tree_item(self, item_id):
        index = self.tree.index(item_id)
        if 0 <= index < len(self.gerenciador.usuario.transacoes): return self.gerenciador.usuario.transacoes[index]
    def imprimir_relatorio(self):
        relatorio_str = self.gerenciador.gerar_relatorio_texto()
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title="Salvar Relatório", initialfile=f"relatorio_{self.gerenciador.usuario.nome}_{dt.date.today()}.txt")
        if not filepath: return
        try:
            with open(filepath, "w", encoding="utf-8") as f: f.write(relatorio_str)
            messagebox.showinfo("Sucesso", f"Relatório salvo com sucesso em:\n{filepath}")
        except Exception as e: messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar o arquivo.\nErro: {e}")
    def mostrar_context_menu(self, event):
        item_selecionado = self.tree.identify_row(event.y)
        if item_selecionado: self.tree.selection_set(item_selecionado); self.context_menu.post(event.x_root, event.y_root)
    def excluir_lancamento(self):
        selected_item = self.tree.selection()
        if not selected_item: messagebox.showwarning("Atenção", "Nenhum lançamento selecionado."); return
        transacao = self.find_transacao_by_tree_item(selected_item[0])
        if not transacao: messagebox.showerror("Erro", "Não foi possível encontrar a transação para excluir."); return
        if messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o lançamento:\n\n'{transacao.descricao} - R$ {transacao.valor:.2f}'?"):
            self.gerenciador.excluir_transacao(transacao); self.atualizar_historico(); messagebox.showinfo("Sucesso", "Lançamento excluído!")
    def editar_lancamento(self):
        selected_item = self.tree.selection();
        if not selected_item: return
        transacao = self.find_transacao_by_tree_item(selected_item[0])
        if not transacao: return
        self.abrir_janela_registro(transacao.tipo, transacao_para_editar=transacao)
    def abrir_janela_registro(self, tipo, transacao_para_editar=None):
        janela = tk.Toplevel(self); titulo = f"Editar {tipo.capitalize()}" if transacao_para_editar else f"Registrar {tipo.capitalize()}"; janela.title(titulo); janela.geometry("300x200")
        ttk.Label(janela, text="Descrição:").pack(pady=5); desc_entry = ttk.Entry(janela, width=30); desc_entry.pack()
        ttk.Label(janela, text="Valor (R$):").pack(pady=5); valor_entry = ttk.Entry(janela, width=30); valor_entry.pack()
        ttk.Label(janela, text="Data (dd/mm/aaaa) [Opcional]:").pack(pady=5); data_entry = ttk.Entry(janela, width=30); data_entry.pack()
        if transacao_para_editar: desc_entry.insert(0, transacao_para_editar.descricao); valor_entry.insert(0, str(transacao_para_editar.valor)); data_entry.insert(0, transacao_para_editar.data.strftime('%d/%m/%Y'))
        def salvar():
            descricao = desc_entry.get()
            valor = validar_valor(valor_entry.get())
            data = data_entry.get()
            
            if not descricao or valor is None: 
                messagebox.showerror("Erro", "Descrição e valor são obrigatórios.", parent=janela)
                return
                
            # Aqui adicionamos o try/except para capturar o ValueError da data
            try:
                if transacao_para_editar: 
                    self.gerenciador.editar_transacao(transacao_para_editar, {'tipo': tipo, 'descricao': descricao, 'valor': valor, 'data': data})
                else: 
                    self.gerenciador.registrar(tipo, descricao, valor, data)
                
                self.atualizar_historico()
                janela.destroy()
            except ValueError as e:
                # Exibe o erro da classe Transacao direto na tela
                messagebox.showerror("Data Inválida", str(e), parent=janela)
        ttk.Button(janela, text="Salvar", command=salvar).pack(pady=15)
    def registrar_ganho(self): self.abrir_janela_registro("ganho")
    def registrar_gasto(self): self.abrir_janela_registro("gasto")
    def mostrar_saldo(self): saldo = self.gerenciador.saldo(); messagebox.showinfo("Saldo", f"Seu saldo atual é de R$ {saldo:.2f}")
    def importar_pdf(self):
        caminho_pdf = filedialog.askopenfilename(
            title="Selecione o PDF Financeiro",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        if not caminho_pdf:
            return

        # Chama o arquivo externo que processa a regra de negócios
        try:
            transacoes, ganhos, gastos = extrair_transacoes_pdf(caminho_pdf)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível ler o PDF.\nErro: {e}")
            return

        if not transacoes:
            messagebox.showinfo("Aviso", "Nenhuma transação com sinal de + ou - foi encontrada no PDF.")
            return

        saldo = ganhos - gastos
        resultado = "LUCRO" if saldo >= 0 else "PREJUÍZO"
        
        mensagem_resumo = (
            f"Análise do PDF Concluída!\n\n"
            f"Ganhos Totais: R$ {ganhos:.2f}\n"
            f"Gastos Totais: R$ {gastos:.2f}\n"
            f"Saldo Final: R$ {saldo:.2f}\n"
            f"Resultado: {resultado}\n\n"
            f"Deseja registrar essas {len(transacoes)} transações no histórico?"
        )

        if messagebox.askyesno("Resumo do PDF", mensagem_resumo):
            for t in transacoes:
                self.gerenciador.registrar(t['tipo'], t['descricao'], t['valor'], t['data'])
            self.atualizar_historico()
            messagebox.showinfo("Sucesso", "Transações do PDF importadas com sucesso!")
class MainController(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mestre Cuca Finanças"); self.geometry("400x300")
        container = tk.Frame(self); container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1); container.grid_columnconfigure(0, weight=1)
        self.current_app_frame = None
        self.login_frame = LoginPage(container, self)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.show_login_page()
    def show_app_page(self, username):
        self.geometry("950x600")
        usuario = Usuario(username); gerenciador = Gerenciador(usuario)
        self.current_app_frame = App(self.login_frame.master, self, gerenciador)
        self.current_app_frame.grid(row=0, column=0, sticky="nsew"); self.current_app_frame.tkraise()
    def show_login_page(self):
        self.geometry("400x300")
        if self.current_app_frame: self.current_app_frame.destroy(); self.current_app_frame = None
        self.login_frame.tkraise()

if __name__ == "__main__":
    app = MainController()
    app.mainloop()