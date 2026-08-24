'''Escreva um programa que simula o jogo conhecido como “Pedra, Papel e Tesoura”
de um jogador A contra um jogador B. O programa deve ler a escolha do jogador A e
a escolha do jogador B. Por ﬁm, o programa deve indicar quem foi o vencedor.'''

A = str(input("Escolha entre Pedra, Papel ou Tesoura: "))
B = str(input("Escolha entre Pedra, Papel ou Tesoura: "))

if (A == "Papel" and B == "Tesoura") or (A == "Pedra" and B == "Papel") or (A == "Tesoura" and B == "Pedra"):
    print("O Jogador B ganhou!!!")
elif (B == "Papel" and A == "Tesoura") or (B == "Pedra" and A == "Papel") or (B == "Tesoura" and A == "Pedra"):
    print("O Jogador A ganhou !!!!")
elif (A == "Papel" and B == "Papel") or (A == "Pedra" and B == "Pedra") or (A == "Tesoura" and B == "Tesoura"):
    print("O jogo deu empate!!")
else:
    print("Reinicie o programa e escolha entre Papel, Pedra ou Tesoura!!!")