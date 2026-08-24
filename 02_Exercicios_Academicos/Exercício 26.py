'''Uma  empresa  está  fazendo  um  estudo  de  possibilidades  de  aumento  aos  seus 
funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à 
todos os funcionários ou seguir a seguinte tabela progressiva:  
Salário Percentual de aumento 
até R$1000,00 - 15% 
até R$2000,00 - 10% 
acima de R$2000,00 - 5% 
 
Faça  um  programa  que  leia  o  salário  de  um  número  qualquer  de  funcionários, 
imprimindo  para  cada  um  o  novo  salário  nos  dois  casos  (aumento  uniforme  ou 
aumento progressivo). Ao final, o programa deve fornecer: 
a. O total de funcionários 
b. O salário médio dos funcionários  
c. O total da folha de pagamentos atual 
d. O  total  da  folha  de  pagamentos  futura  nos  dois  casos  estudados,  indicando 
qual o caminho mais econômico para a empresa.'''

# Função para calcular o aumento de salário progressivo
# Função para calcular o aumento de salário progressivo
# Função para calcular o aumento de salário progressivo
def aumento_progressivo(salario):
    if salario <= 1000:
        return salario * 0.15
    elif salario <= 2000:
        return salario * 0.10
    else:
        return salario * 0.05

# Entrada do número de funcionários
numero_funcionarios = int(input("Digite o número de funcionários: "))

# Inicialização de variáveis
total_salarios_atual = 0
total_salarios_futuro_uniforme = 0
total_salarios_futuro_progressivo = 0

# Loop para coletar os salários dos funcionários e calcular os resultados
for _ in range(numero_funcionarios):
    salario_atual = float(input("Digite o salário do funcionário: "))
    total_salarios_atual += salario_atual
    
    # Novo salário (aumento uniforme)
    novo_salario_uniforme = salario_atual * 1.10
    total_salarios_futuro_uniforme += novo_salario_uniforme
    
    # Novo salário (aumento progressivo)
    novo_salario_progressivo = salario_atual + aumento_progressivo(salario_atual)
    total_salarios_futuro_progressivo += novo_salario_progressivo
    
    # Impressão dos resultados para o funcionário atual
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Novo salário (aumento uniforme): R$ {novo_salario_uniforme:.2f}")
    print(f"Novo salário (aumento progressivo): R$ {novo_salario_progressivo:.2f}")
    print()

# Cálculo do salário médio dos funcionários
if numero_funcionarios != 0:
    salario_medio = total_salarios_atual / numero_funcionarios
else:
    salario_medio = 0

# Impressão dos resultados finais
print("Resultados finais:")
print(f"Total de funcionários: {numero_funcionarios}")
print(f"Salário médio dos funcionários: R$ {salario_medio:.2f}")
print(f"Total da folha de pagamentos atual: R$ {total_salarios_atual:.2f}")
print(f"Total da folha de pagamentos futura (aumento uniforme): R$ {total_salarios_futuro_uniforme:.2f}")
print(f"Total da folha de pagamentos futura (aumento progressivo): R$ {total_salarios_futuro_progressivo:.2f}")

# Verificação do caminho mais econômico para a empresa
if total_salarios_futuro_uniforme < total_salarios_futuro_progressivo:
    print("O aumento uniforme de 10% é mais econômico para a empresa.")
elif total_salarios_futuro_uniforme > total_salarios_futuro_progressivo:
    print("O aumento progressivo é mais econômico para a empresa.")
else:
    print("Ambas as opções têm o mesmo custo para a empresa.")
