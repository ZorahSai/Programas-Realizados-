import pdfplumber
import re
import datetime as dt

def extrair_transacoes_pdf(caminho_pdf):
    transacoes_lidas = []
    ganhos_totais = 0.0
    gastos_totais = 0.0
    
    # Dicionário para converter o nome do mês para número
    meses = {
        "janeiro": "01", "fevereiro": "02", "março": "03", "marco": "03",
        "abril": "04", "maio": "05", "junho": "06", "julho": "07",
        "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
    }
    
    # Se o PDF não tiver data, usamos a de hoje como garantia
    data_atual = dt.date.today().strftime('%d/%m/%Y')

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if not texto:
                continue
                
            linhas = texto.split('\n')
            for linha in linhas:
                # 1 TENTA ACHAR UMA DATA NA LINHA (Ex: "20 de agosto 2026")
                # A Regex busca um número, a palavra "de", um mês e um ano.
                match_data = re.search(r'(\d{1,2})\s+de\s+([a-zA-ZçÇ]+)\s*(?:de\s*)?(\d{4})', linha, re.IGNORECASE)
                if match_data:
                    dia = match_data.group(1).zfill(2) # Garante que "1" vire "01"
                    mes_nome = match_data.group(2).lower()
                    ano = match_data.group(3)
                    
                    mes = meses.get(mes_nome, "01")
                    data_atual = f"{dia}/{mes}/{ano}"
                    # Achamos uma data, vamos para a próxima linha
                    continue 

                # 2 PROCURA OS VALORES (agora incluindo os traços especiais do PDF: -, –, −)
                match = re.search(r'([+\-–−])\s*(?:R\$)?\s*([\d\.\s]+,\d{2})', linha)
                
                if match:
                    sinal = match.group(1)
                    valor_bruto = match.group(2) # Ex: " 18,00" ou "51,99"
                    
                    
                    valor_limpo = valor_bruto.replace(' ', '') # 1. Remove qualquer espaço
                    valor_limpo = valor_limpo.replace('.', '') # 2. Remove pontos (se houver)
                    valor_limpo = valor_limpo.replace(',', '.') # 3. Troca a vírgula por ponto
                    
                    try:
                        valor = float(valor_limpo)
                    except ValueError:
                        print(f"ERRO DE CONVERSÃO! Não foi possível converter: {valor_limpo}")
                        continue
                        
                    
                    print(f"Linha lida: {linha.strip()}")
                    print(f" -> Capturado: '{valor_bruto}' | Convertido: {valor}")
                    print("-" * 30)

                    # 3 DEFINE SE É GANHO OU GASTO
                    if sinal == '+':
                        tipo = "ganho"
                        ganhos_totais += valor
                    else:
                        tipo = "gasto"
                        gastos_totais += valor
                        
                    # 4 LIMPA A DESCRIÇÃO
                    descricao = linha.replace(match.group(0), '').strip()
                    
                   
                    descricao = re.sub(r'^\d{2}:\d{2}\s+', '', descricao).strip()
                    
                    # 5 SALVA A TRANSAÇÃO COM A DATA CORRETA
                    transacoes_lidas.append({
                        "tipo": tipo, 
                        "descricao": descricao, 
                        "valor": valor,
                        "data": data_atual 
                    })
                    
    return transacoes_lidas, ganhos_totais, gastos_totais
