import random as rd
from utils import obter_saudacao

import random as rd
from utils import obter_saudacao

# Função auxiliar interna para montar a "estrutura" da mensagem
def _montar_esqueleto(saudacao_tempo, tratamento, nome, referencia_veiculo, placa):
    
    # 1. Aberturas (Variações de saudação)
    aberturas = [
        f"{saudacao_tempo}, {tratamento}{nome}.",
        f"Prezado(a) {tratamento}{nome}, {saudacao_tempo.lower()}.",
        f"Olá, {tratamento}{nome}. Esperamos que esteja bem.",
        f"{saudacao_tempo}, {tratamento}{nome}. Tudo bem?",
        f"Estimado(a) {tratamento}{nome},",
    ]

    # 2. O Anúncio (O que aconteceu?)
    anuncios = [
        f"Informamos que o documento referente ao veículo ({placa}) {referencia_veiculo} já se encontra pronto.",
        f"Temos a satisfação de comunicar que o documento do veículo de placa {placa} ({referencia_veiculo.replace('do ', '').replace('da ', '')}) foi emitido com sucesso.",
        f"O processo do veículo ({placa}) foi concluído e o documento {referencia_veiculo} já está disponível para retirada.",
        f"Entramos em contato para avisar que o documento {referencia_veiculo} (Placa: {placa}) está pronto.",
        f"Notificamos que o licenciamento do veículo ({placa}) foi finalizado e o documento está em mãos.",
    ]

    # 3. A Instrução (O que fazer?)
    instrucoes = [
        "O mesmo encontra-se disponível para retirada em nosso escritório.",
        "Você já pode passar aqui no escritório para retirar a versão impressa.",
        "Aguardamos sua visita para a retirada do documento original.",
        "O documento físico está separado e pronto para ser retirado no balcão.",
        "Pode retirar o documento impresso diretamente conosco.",
    ]

    # 4. Informações de Horário (Fixo, mas com variações de texto)
    horarios = [
        "Nosso horário de atendimento é de segunda a sexta, das 8h às 17h.",
        "Estamos à disposição de segunda a sexta-feira, das 08:00 às 17:00.",
        "Atendemos nos dias úteis, das 8h às 17h.",
        "Funcionamos de segunda a sexta, das 8h às 17h.",
    ]

    # 5. Opção Digital (PDF)
    digitais = [
        "Caso prefira agilidade, podemos enviar a versão em PDF por aqui.",
        "Se for mais conveniente, solicite o envio do arquivo digital (PDF).",
        "Também disponibilizamos o envio do documento em formato PDF, se desejar.",
        "Havendo interesse, podemos encaminhar a cópia digital (PDF) para impressão.",
        "Se preferir não vir buscar agora, posso adiantar o arquivo em PDF.",
    ]

    # 6. Despedida Formal
    despedidas = [
        "Atenciosamente,\nMarcello e equipe do\n*DESPACHANTE LIDER*",
        "Cordialmente,\nMarcello e equipe\n*DESPACHANTE LIDER*",
        "Agradecemos a confiança.\nEquipe *DESPACHANTE LIDER*",
        "Qualquer dúvida, estamos à disposição.\n*DESPACHANTE LIDER*",
        "Conte sempre conosco!\nMarcello - *DESPACHANTE LIDER*",
    ]

    # Montagem da frase final com quebras de linha
    mensagem = (
        f"{rd.choice(aberturas)}\n\n"
        f"{rd.choice(anuncios)} "
        f"{rd.choice(instrucoes)}\n\n"
        f"{rd.choice(horarios)}\n"
        f"{rd.choice(digitais)}\n\n"
        f"{rd.choice(despedidas)}"
    )
    
    return mensagem


def gerar_frase_proprietario(nameOwner, sexo, placa, tratamento):
    """
    Gera mensagem quando o contato É o dono do carro.
    """
    saudacao = obter_saudacao()
    # Referência direta: "do seu veículo"
    referencia = "do seu veículo" 
    
    return _montar_esqueleto(saudacao, tratamento, nameOwner, referencia, placa)


def gerar_frase_terceiro(contatName, tratamento_contato, nameOwner, tratamento_prop, placa):
    """
    Gera mensagem quando o contato NÃO é o dono (falando com parente/amigo/secretária).
    """
    saudacao = obter_saudacao()
    # Referência indireta: "do veículo do Sr. João"
    referencia = f"pertencente a {tratamento_prop}{nameOwner}"
    
    return _montar_esqueleto(saudacao, tratamento_contato, contatName, referencia, placa)
       
       
     
