import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Toplevel
import os
import csv
import re
from utils import (
    capitalizar_name, formatar_tratamento, 
    copiar_para_clipboard, salvar_historico, 
    salvar_contato_csv, listar_contatos_csv, excluir_contato_csv, 
    atualizar_contato_csv, importar_arquivo_csv, tema_ativo
)
from random_frase import gerar_frase_proprietario, gerar_frase_terceiro

class DespachanteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Despachante Líder")
        self.root.geometry("800x650") # Aumentei a largura para acomodar o menu
        self.root.configure(bg="#f0f0f0")

        # --- Configuração do Layout Principal ---
        # Menu Lateral (Esquerda)
        self.sidebar = tk.Frame(root, bg="#2c3e50", width=200)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False) # Impede que o frame encolha

        # Área de Conteúdo (Direita)
        self.content_area = tk.Frame(root, bg="#f0f0f0")
        self.content_area.pack(side="right", fill="both", expand=True)

        # Configuração das Telas (Frames)
        # Vamos empilhar todos os frames na content_area e alternar a visibilidade
        self.frames = {}

        for F in (FrameGerador, FrameContatos, FrameHistorico):
            page_name = F.__name__
            frame = F(parent=self.content_area, controller=self)
            self.frames[page_name] = frame
            # Coloca todos no mesmo lugar (grid 0,0) para sobrepor
            frame.grid(row=0, column=0, sticky="nsew")

        # Configurar peso do grid da área de conteúdo para expandir
        self.content_area.grid_rowconfigure(0, weight=1)
        self.content_area.grid_columnconfigure(0, weight=1)

        # --- Criar Botões do Menu ---
        self.criar_menu_lateral()

        # Iniciar na tela do Gerador
        self.mostrar_tela("FrameGerador")

    def criar_menu_lateral(self):
        # Título / Logo no Menu
        lbl_title = tk.Label(self.sidebar, text="DESPACHANTE\nLÍDER", bg="#2c3e50", fg="white", font=("Arial", 12, "bold"), pady=20)
        lbl_title.pack(fill="x")

        # Botões de Navegação
        # Dica: Usamos lambda para passar o nome da tela
        self.btn_nav(self.sidebar, "📝 Gerar Mensagem", "FrameGerador")
        self.btn_nav(self.sidebar, "👥 Contatos", "FrameContatos")
        self.btn_nav(self.sidebar, "📜 Histórico", "FrameHistorico")
        
        # Espaçador
        tk.Label(self.sidebar, bg="#2c3e50").pack(fill="both", expand=True)
        
        # Botão Sair
        btn_sair = tk.Button(self.sidebar, text="Sair", bg="#c0392b", fg="white", font=("Arial", 10), bd=0, padx=20, pady=10, command=self.root.quit)
        btn_sair.pack(fill="x", side="bottom", pady=10, padx=10)

    def btn_nav(self, parent, text, frame_name):
        btn = tk.Button(parent, text=text, bg="#34495e", fg="white", font=("Arial", 10), bd=0, padx=20, pady=15, anchor="w",
                        command=lambda: self.mostrar_tela(frame_name))
        btn.pack(fill="x", pady=1)
        
        # Efeito simples de hover
        btn.bind("<Enter>", lambda e: btn.configure(bg="#2980b9"))
        btn.bind("<Leave>", lambda e: btn.configure(bg="#34495e"))

    def mostrar_tela(self, page_name):
        """Traz o frame escolhido para o topo da pilha"""
        frame = self.frames[page_name]
        frame.tkraise()
        
        # Se for tela de contatos ou histórico, atualiza a lista automaticamente ao abrir
        if hasattr(frame, 'atualizar_dados'):
            frame.atualizar_dados()


# =============================================================================
# TELA 1: GERADOR DE MENSAGENS
# =============================================================================
class FrameGerador(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller
        
        # Título da Página
        tk.Label(self, text="Gerador de Mensagens", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)

        self.container_inputs = tk.Frame(self, bg="#f0f0f0")
        self.container_inputs.pack(fill='x', padx=20)
        paddy = 2
        
        # === DADOS DO CONTATO ===
        self.lbl_frame_contato = tk.LabelFrame(self.container_inputs, text="Dados do Contato", bg="#f0f0f0")
        self.lbl_frame_contato.pack(fill="x", pady=5)

        tk.Label(self.lbl_frame_contato, text="Nome:", bg="#f0f0f0").pack(anchor="w", padx=5)
        self.entry_contato = tk.Entry(self.lbl_frame_contato)
        self.entry_contato.pack(fill="x", padx=5, pady=paddy)

        # Telefone e Botão Salvar
        frame_tel = tk.Frame(self.lbl_frame_contato, bg="#f0f0f0")
        frame_tel.pack(fill="x", padx=5, pady=paddy)

        tk.Label(frame_tel, text="Telefone / WhatsApp:", bg="#f0f0f0").pack(anchor="w")
        self.entry_telefone = tk.Entry(frame_tel)
        self.entry_telefone.pack(side="left", fill="x", expand=True)
        
        tk.Button(frame_tel, text="💾 Salvar", font=("Arial", 8), command=self.acao_salvar_contato).pack(side="left", padx=5)

        # Gênero
        tk.Label(self.lbl_frame_contato, text="Gênero:", bg="#f0f0f0").pack(anchor="w", padx=5)
        self.sexo_contato_var = tk.StringVar(value="M")
        frame_radio = tk.Frame(self.lbl_frame_contato, bg="#f0f0f0")
        frame_radio.pack(anchor="w", padx=5, pady=paddy)
        tk.Radiobutton(frame_radio, text="Masculino", variable=self.sexo_contato_var, value="M", bg="#f0f0f0").pack(side="left")
        tk.Radiobutton(frame_radio, text="Feminino", variable=self.sexo_contato_var, value="F", bg="#f0f0f0").pack(side="left")

        # === DADOS DO VEÍCULO ===
        self.lbl_frame_veiculo = tk.LabelFrame(self.container_inputs, text="Dados do Veículo", bg="#f0f0f0")
        self.lbl_frame_veiculo.pack(fill="x", pady=5)

        tk.Label(self.lbl_frame_veiculo, text="Placa:", font=("Arial", 9, "bold"), bg="#f0f0f0").pack(anchor="w", padx=5)
        self.entry_placa = tk.Entry(self.lbl_frame_veiculo, width=20)
        self.entry_placa.pack(anchor="w", padx=5, pady=paddy)

        self.e_proprietario_var = tk.BooleanVar(value=True)
        self.chk_proprietario = tk.Checkbutton(self.container_inputs, text="O contato É o proprietário?", 
                                               variable=self.e_proprietario_var, command=self.toggle_proprietario, bg="#f0f0f0")
        self.chk_proprietario.pack(pady=5)

        # === DADOS PROPRIETÁRIO (TERCEIRO) ===
        self.frame_dados_prop = tk.LabelFrame(self.container_inputs, text="Proprietário Real", bg="#f0f0f0")
        
        tk.Label(self.frame_dados_prop, text="Nome:", bg="#f0f0f0").pack(anchor="w", padx=5)
        self.entry_proprietario = tk.Entry(self.frame_dados_prop)
        self.entry_proprietario.pack(fill="x", padx=5, pady=paddy)

        tk.Label(self.frame_dados_prop, text="Gênero:", bg="#f0f0f0").pack(anchor="w", padx=5)
        self.sexo_prop_var = tk.StringVar(value="M")
        frame_radio_prop = tk.Frame(self.frame_dados_prop, bg="#f0f0f0")
        frame_radio_prop.pack(anchor="w", padx=5, pady=paddy)
        tk.Radiobutton(frame_radio_prop, text="Masculino", variable=self.sexo_prop_var, value="M", bg="#f0f0f0").pack(side="left")
        tk.Radiobutton(frame_radio_prop, text="Feminino", variable=self.sexo_prop_var, value="F", bg="#f0f0f0").pack(side="left")

        # === AÇÕES ===
        btn_gerar = tk.Button(self, text="GERAR MENSAGEM", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.gerar_mensagem)
        btn_gerar.pack(pady=10)

        self.txt_resultado = tk.Text(self, height=8, width=60)
        self.txt_resultado.pack(pady=5, padx=20)

        frame_botoes = tk.Frame(self, bg="#f0f0f0")
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Copiar Texto", command=self.copiar_texto).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Limpar Tudo", command=self.limpar_campos).pack(side="left", padx=5)

    def toggle_proprietario(self):
        if not self.e_proprietario_var.get():
            self.frame_dados_prop.pack(pady=5, padx=5, fill="x")
        else:
            self.frame_dados_prop.pack_forget()

    def validar_placa(self, placa):
        padrao = re.compile(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$')
        placa_limpa = placa.replace("-", "").replace(" ", "").upper()
        if padrao.match(placa_limpa):
            return placa_limpa
        return None

    def gerar_mensagem(self):
        contato = capitalizar_name(self.entry_contato.get())
        placa_raw = self.entry_placa.get()
        placa = self.validar_placa(placa_raw)

        if not contato or not placa:
            messagebox.showerror("Erro", "Preencha o Nome e uma Placa válida.")
            return

        sexo_contato = self.sexo_contato_var.get()
        tratamento_contato = formatar_tratamento(sexo_contato)
        
        mensagem = ""
        nome_prop_log = ""
        tipo_msg = ""

        if self.e_proprietario_var.get():
            tipo_msg = "Proprietário"
            nome_prop_log = contato
            mensagem = gerar_frase_proprietario(contato, sexo_contato, placa, tratamento_contato)
        else:
            tipo_msg = "Terceiro"
            nome_prop = capitalizar_name(self.entry_proprietario.get())
            if not nome_prop:
                messagebox.showerror("Erro", "Preencha o nome do Proprietário.")
                return
            nome_prop_log = nome_prop
            sexo_prop = self.sexo_prop_var.get()
            tratamento_prop = formatar_tratamento(sexo_prop, tipo="proprietario")
            mensagem = gerar_frase_terceiro(contato, tratamento_contato, nome_prop, tratamento_prop, placa)

        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(tk.END, mensagem)
        
        salvar_historico(contato, nome_prop_log, placa, tipo_msg)

    def copiar_texto(self):
        texto = self.txt_resultado.get("1.0", tk.END).strip()
        if texto:
            copiar_para_clipboard(texto)
            messagebox.showinfo("Sucesso", "Mensagem copiada!")

    def limpar_campos(self):
        self.entry_contato.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_placa.delete(0, tk.END)
        self.entry_proprietario.delete(0, tk.END)
        self.txt_resultado.delete("1.0", tk.END)
        self.e_proprietario_var.set(True)
        self.toggle_proprietario()

    def acao_salvar_contato(self):
        nome = capitalizar_name(self.entry_contato.get())
        tel = self.entry_telefone.get().strip()
        sexo = self.sexo_contato_var.get()

        if not nome:
            messagebox.showwarning("Atenção", "Digite pelo menos o nome para salvar.")
            return

        if salvar_contato_csv(nome, tel, sexo):
            messagebox.showinfo("Sucesso", f"Contato '{nome}' salvo!")
        else:
            messagebox.showerror("Erro", "Erro ao salvar.")

    def preencher_com_contato(self, nome, tel, sexo):
        """Método chamado pela tela de contatos"""
        self.limpar_campos()
        self.entry_contato.insert(0, nome)
        self.entry_telefone.insert(0, tel)
        self.sexo_contato_var.set(sexo)


# =============================================================================
# TELA 2: LISTA DE CONTATOS
# =============================================================================
class FrameContatos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller
        
        tk.Label(self, text="Contatos Salvos", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)

        # Treeview com Scrollbar
        frame_lista = tk.Frame(self)
        frame_lista.pack(fill='both', expand=True, padx=20, pady=5)

        colunas = ("Nome", "Telefone", "Sexo")
        self.tree = ttk.Treeview(frame_lista, columns=colunas, show='headings', selectmode="browse")
        
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.column("Nome", width=200)
        self.tree.column("Telefone", width=150)
        self.tree.column("Sexo", width=50, anchor="center")
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill='both', expand=True)
        scrollbar.pack(side="right", fill='y')

        self.tree.bind("<Double-1>", self.acao_editar_popup)

        # Botões
        frame_btns = tk.Frame(self, bg="#f0f0f0")
        frame_btns.pack(pady=15)

        tk.Button(frame_btns, text="✏️ Editar", bg="#f1c40f", command=self.acao_editar_popup).pack(side="left", padx=5)
        tk.Button(frame_btns, text="🗑️ Excluir", bg="#e74c3c", fg="white", command=self.acao_excluir).pack(side="left", padx=5)
        ttk.Separator(frame_btns, orient="vertical").pack(side="left", fill="y", padx=10)
        tk.Button(frame_btns, text="📝 Usar no Gerador", bg="#3498db", fg="white", command=self.usar_contato).pack(side="left", padx=5)
        ttk.Separator(frame_btns, orient="vertical").pack(side="left", fill="y", padx=10)
        tk.Button(frame_btns, text="📥 Importar CSV", command=self.acao_importar).pack(side="left", padx=5)
        tk.Button(frame_btns, text="🔄 Atualizar", command=self.atualizar_dados).pack(side="left", padx=5)

    def atualizar_dados(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        contatos = listar_contatos_csv()
        for c in contatos:
            self.tree.insert("", "end", values=c)

    def usar_contato(self):
        selecionado = self.tree.selection()
        if not selecionado:
            return
        
        dados = self.tree.item(selecionado[0])['values'] # [Nome, Tel, Sexo]
        
        # Chama a função lá no FrameGerador para preencher
        frame_gen = self.controller.frames["FrameGerador"]
        frame_gen.preencher_com_contato(dados[0], str(dados[1]), dados[2])
        
        # Muda a tela
        self.controller.mostrar_tela("FrameGerador")

    def acao_excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione para excluir.")
            return
        
        nome = self.tree.item(selecionado[0])['values'][0]
        if messagebox.askyesno("Confirmar", f"Excluir '{nome}'?"):
            excluir_contato_csv(nome)
            self.atualizar_dados()

    def acao_importar(self):
        caminho = filedialog.askopenfilename(filetypes=[("CSV", "*.csv"), ("Tudo", "*.*")])
        if caminho:
            qtd = importar_arquivo_csv(caminho)
            if qtd >= 0:
                messagebox.showinfo("Sucesso", f"{qtd} importados.")
                self.atualizar_dados()
            else:
                messagebox.showerror("Erro", "Falha ao ler arquivo.")

    def acao_editar_popup(self, event=None):
        selecionado = self.tree.selection()
        if not selecionado:
            return

        dados = self.tree.item(selecionado[0])['values']
        nome_orig = dados[0]

        popup = Toplevel(self)
        popup.title("Editar Contato")
        popup.geometry("300x250")
        
        tk.Label(popup, text="Nome:").pack(anchor="w", padx=10)
        entry_nome = tk.Entry(popup, width=30)
        entry_nome.insert(0, dados[0])
        entry_nome.pack(padx=10)

        tk.Label(popup, text="Telefone:").pack(anchor="w", padx=10)
        entry_tel = tk.Entry(popup, width=30)
        entry_tel.insert(0, str(dados[1]))
        entry_tel.pack(padx=10)

        tk.Label(popup, text="Gênero:").pack(anchor="w", padx=10)
        var_sexo = tk.StringVar(value=dados[2])
        tk.Radiobutton(popup, text="Masculino", variable=var_sexo, value="M").pack()
        tk.Radiobutton(popup, text="Feminino", variable=var_sexo, value="F").pack()

        def salvar():
            if atualizar_contato_csv(nome_orig, entry_nome.get(), entry_tel.get(), var_sexo.get()):
                self.atualizar_dados()
                popup.destroy()
            else:
                messagebox.showerror("Erro", "Falha ao atualizar.")

        tk.Button(popup, text="Salvar", bg="#2ecc71", command=salvar).pack(pady=15)


# =============================================================================
# TELA 3: HISTÓRICO
# =============================================================================
class FrameHistorico(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller

        tk.Label(self, text="Histórico de Mensagens", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)

        frame_lista = tk.Frame(self)
        frame_lista.pack(fill='both', expand=True, padx=20, pady=5)

        colunas = ("Data", "Contato", "Proprietario", "Placa", "Tipo")
        self.tree = ttk.Treeview(frame_lista, columns=colunas, show='headings')
        
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.column("Data", width=130)
        self.tree.column("Placa", width=80)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill='both', expand=True)
        scrollbar.pack(side="right", fill='y')

        btn = tk.Button(self, text="🗑️ Limpar Histórico", bg="#e74c3c", fg="white", command=self.limpar_hist)
        btn.pack(pady=15)

    def atualizar_dados(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        arquivo = 'historico_mensagns.csv'
        if os.path.isfile(arquivo):
            try:
                with open(arquivo, newline='', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=';')
                    next(reader, None)
                    for row in reversed(list(reader)):
                        self.tree.insert("", "end", values=row) 
            except Exception:
                pass

    def limpar_hist(self):
        if messagebox.askyesno("Confirmar", "Apagar tudo?"):
            with open('historico_mensagns.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Data/Hora', 'Contato', 'Proprietario', 'Placa', 'Tipo'])
            self.atualizar_dados()

if __name__ == "__main__":
    root = tk.Tk()
    app = DespachanteApp(root)
    root.mainloop()



    