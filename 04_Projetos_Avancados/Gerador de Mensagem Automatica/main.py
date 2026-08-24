from random_frase import gerar_frase_proprietario, gerar_frase_terceiro
from utils import (
    capitalizar_name, tema_ativo, clear_screen, typing, set_tema, 
    qual_placa, obter_genero, formatar_tratamento, copiar_para_clipboard, salvar_historico
)


def escolher_tema():
    clear_screen()
    typing("🎨 Escolha um tema:\n")
    print("1️⃣  Light Mode (padrão)")
    print("2️⃣  Dark Mode")

    while True:
        escolha = input("\n➡ Digite 1 ou 2: ").strip()
        if escolha in ["1", "2"]:
            set_tema(escolha)
            clear_screen()
            return
        print("❌ Opção inválida!")


def verificar_name(contatName):
    while True:
        resposta = input(
            f"{tema_ativo['pergunta']}É o proprietário do veículo? (S/N): {tema_ativo['reset']}"
        ).strip().upper()

        if resposta in ["S", "N"]:
            break

        print(f"{tema_ativo['erro']}❌ Por favor, digite S ou N.{tema_ativo['reset']}")

    if resposta == "S":
        return gerar_frase_proprietario(contatName)
    else:
        nameOwner = capitalizar_name(
            input(f"{tema_ativo['entrada']}Insira o nome do proprietário: {tema_ativo['reset']}")
        )
        return gerar_frase_terceiro(contatName, nameOwner)


def menu():
    escolher_tema()

    while True:
        clear_screen()

        print(f"{tema_ativo['titulo']}")
        typing("╔════════════════════════════════════╗")
        typing("║         GERADOR DE MENSAGENS       ║")
        typing("╚════════════════════════════════════╝")
        print(tema_ativo["reset"])

        print(f"{tema_ativo['opcao']}1️⃣  Gerar mensagem para um contato{tema_ativo['reset']}")
        print(f"{tema_ativo['erro']}2️⃣  Sair{tema_ativo['reset']}")

        escolha = input(f"\n{tema_ativo['pergunta']}➡ Escolha uma opção: {tema_ativo['reset']}")

        if escolha == "1":
            
            contatName = capitalizar_name(input(f"{tema_ativo['entrada']}Insira o nome do contato: {tema_ativo['reset']}"))
            sexo_contato = obter_genero(f"Qual o gênero de {contatName}? (M/F): ")
            tratamento_contato = formatar_tratamento(sexo_contato)
            
            e_proprietario = input(f"{tema_ativo['pergunta']}É o proprietário do veículo? (S/N): {tema_ativo['reset']}").strip().upper()
            
            placa = qual_placa(tema_ativo) 
            
            mensagem = ""
            tipo_msg = "" 
            nameOwner_log = "" 
            if e_proprietario == "S":
                
                mensagem = gerar_frase_proprietario(contatName, sexo_contato, placa, tratamento_contato)
            else:
                
                nameOwner = capitalizar_name(input(f"{tema_ativo['entrada']}Insira o nome do proprietário: {tema_ativo['reset']}"))
                sexo_prop = obter_genero(f"Qual o gênero do proprietário ({nameOwner})? (M/F): ")
                tratamento_prop = formatar_tratamento(sexo_prop, tipo="proprietario")
                
                mensagem = gerar_frase_terceiro(contatName, tratamento_contato, nameOwner, tratamento_prop, placa)

            
            clear_screen()
            print(f"{tema_ativo['saida']}📨 Mensagem gerada:{tema_ativo['reset']}\n")
            print("-" * 40)
            print(mensagem)
            print("-" * 40)
            
            
            salvar_historico(contatName, nameOwner_log, placa, tipo_msg)
            print(f"\n💾 {tema_ativo['titulo']}Histórico salvo com sucesso!{tema_ativo['reset']}")
            # -----------------------------

            if copiar_para_clipboard(mensagem):
                print(f"{tema_ativo['opcao']}✅ Copiado para a área de transferência!{tema_ativo['reset']}")
            else:
                print(f"{tema_ativo['erro']}(Instale 'pyperclip' para copiar automaticamente){tema_ativo['reset']}")

            input("\nPressione ENTER para voltar ao menu...")
        elif escolha == "2":
            break


if __name__ == "__main__":
    menu()