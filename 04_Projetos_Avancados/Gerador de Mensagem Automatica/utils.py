import os
import time
import re
import datetime
import csv

try:
    import pyperclip
except ImportError:
    pyperclip = None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def obter_saudacao():
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def copiar_para_clipboard(texto):
    if pyperclip:
        pyperclip.copy(texto)
        return True
    return False

def qual_placa(tema_ativo, pergunta="Qual a placa?: "):
    padrao_placa = re.compile(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$') # Valida Mercosul e Antiga
    while True:
        placa = input(f"{tema_ativo['entrada']}{pergunta}{tema_ativo['reset']}").strip().upper()
        
        placa_limpa = placa.replace("-", "").replace(" ", "")
        
        if padrao_placa.match(placa_limpa):
            
            return placa_limpa
        
        print(f"{tema_ativo['erro']}❌ Placa inválida! Use o formato ABC1234 ou ABC1D23.{tema_ativo['reset']}")


def typing(text, delay=0):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def salvar_historico(nome_contato, nome_proprietario, placa, tipo_mensagem):
    arquivo = 'historico_mensagns.csv'
    arquivo_existe = os.path.isfile(arquivo)
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')

            if not arquivo_existe:
                writer.writerow(['Data/Hora', 'Contato', 'Proprietario', 'Placa', 'Tipo' ])
            writer.writerow([data_hora, nome_contato, nome_proprietario, placa, tipo_mensagem])
    except Exception as e:
        print(f"Erro ao salvar historico: {e}")        



class Tema:
    LIGHT = {
        "reset": "\033[0m",
        "titulo": "\033[1;34m",
        "opcao": "\033[32m",
        "erro": "\033[31m",
        "pergunta": "\033[33m",
        "entrada": "\033[36m",
        "saida": "\033[35m",
    }

    DARK = {
        "reset": "\033[0m",
        "titulo": "\033[1;36m",
        "opcao": "\033[92m",
        "erro": "\033[91m",
        "pergunta": "\033[93m",
        "entrada": "\033[96m",
        "saida": "\033[95m",
    }


tema_ativo = Tema.LIGHT


def set_tema(modo):
    global tema_ativo
    if modo == "1":
        tema_ativo = Tema.LIGHT
    else:
        tema_ativo = Tema.DARK


def obter_genero(mensagem="Qual o gênero? (M/F): "):
    while True:
        sexo = input(f"{tema_ativo['entrada']}{mensagem}{tema_ativo['reset']}").strip().upper()
        if sexo in ["M", "F"]:
            return sexo

        print(f"{tema_ativo['erro']}❌ Escolha M ou F.{tema_ativo['reset']}")


def formatar_tratamento(sexo, tipo="pessoa"):
    if tipo == "proprietario":
        return "do Sr. " if sexo == "M" else "da Sra. "
    else:
        return "Sr. " if sexo == "M" else "Sra. "


def capitalizar_name(name):
    return name.strip().capitalize()


def salvar_contato_csv(nome, telefone, sexo):
    """Salva ou atualiza um contato no CSV."""
    arquivo = 'contatos.csv'
    linhas = []
    encontrado = False
    
    # Cabeçalho padrão
    header = ['Nome', 'Telefone', 'Sexo']

    # 1. Ler existentes
    if os.path.isfile(arquivo):
        try:
            with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                
                # Tenta ler o cabeçalho existente ou cria um novo
                try:
                    existente_header = next(reader)
                    linhas.append(existente_header)
                except StopIteration:
                    linhas.append(header)
                
                for row in reader:
                    if row:
                        # Se encontrar o nome (case insensitive), atualiza os dados
                        if row[0].strip().lower() == nome.strip().lower():
                            linhas.append([nome, telefone, sexo]) # Atualiza
                            encontrado = True
                        else:
                            linhas.append(row) # Mantém
        except Exception as e:
            print(f"Erro ao ler contatos: {e}")
            return False
    else:
        linhas.append(header)

    # 2. Se não encontrou, adiciona novo
    if not encontrado:
        linhas.append([nome, telefone, sexo])

    # 3. Gravar tudo de volta
    try:
        with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)
        return True
    except Exception as e:
        print(f"Erro ao salvar contato: {e}")
        return False

def listar_contatos_csv():
    """Retorna uma lista de todos os contatos."""
    arquivo = 'contatos.csv'
    lista = []
    if os.path.isfile(arquivo):
        try:
            with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader, None) # Pular cabeçalho
                for row in reader:
                    if row:
                        lista.append(row)
        except Exception:
            pass
    # Ordenar alfabeticamente pelo nome
    lista.sort(key=lambda x: x[0].lower())
    return lista

def excluir_contato_csv(nome_para_excluir):
    """Remove um contato pelo nome."""
    arquivo = 'contatos.csv'
    linhas = []
    if os.path.isfile(arquivo):
        with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            try:
                linhas.append(next(reader)) # Cabeçalho
            except StopIteration:
                pass
            
            for row in reader:
                if row and row[0].strip().lower() != nome_para_excluir.strip().lower():
                    linhas.append(row)
        
        with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(linhas)
        return True
    return False

# --- Adicione ou atualize estas funções no utils.py ---

def atualizar_contato_csv(nome_original, novo_nome, novo_telefone, novo_sexo):
    """
    Busca o contato pelo 'nome_original' e atualiza todos os dados.
    Isso permite corrigir nomes digitados errados sem duplicar o contato.
    """
    arquivo = 'contatos.csv'
    linhas = []
    atualizado = False

    if os.path.isfile(arquivo):
        try:
            with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                try:
                    linhas.append(next(reader)) # Mantém o cabeçalho
                except StopIteration:
                    pass
                
                for row in reader:
                    if row:
                        # Se achou o contato original, substitui pelos novos dados
                        if row[0].strip().lower() == nome_original.strip().lower():
                            linhas.append([novo_nome, novo_telefone, novo_sexo])
                            atualizado = True
                        else:
                            linhas.append(row)
            
            if atualizado:
                with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerows(linhas)
                return True
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False
    return False

def importar_arquivo_csv(caminho_arquivo):
    """
    Lê um CSV externo e importa os contatos.
    Espera formato: Nome;Telefone;Sexo
    """
    importados_count = 0
    try:
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as file:
            # Tenta detectar se usa ; ou ,
            sample = file.read(1024)
            file.seek(0)
            dialect = csv.Sniffer().sniff(sample)
            
            reader = csv.reader(file, dialect)
            
            # Pula cabeçalho se existir
            has_header = csv.Sniffer().has_header(sample)
            if has_header:
                next(reader, None)
            
            for row in reader:
                if len(row) >= 2: # Precisa pelo menos Nome e Telefone
                    nome = row[0].strip()
                    telefone = row[1].strip()
                    # Sexo é opcional, assume M se não tiver
                    sexo = row[2].strip().upper() if len(row) > 2 else "M" 
                    
                    # Reutiliza a função de salvar para garantir que não duplica se já existir
                    if salvar_contato_csv(nome, telefone, sexo):
                        importados_count += 1
        return importados_count
    except Exception as e:
        print(f"Erro na importação: {e}")
        return -1