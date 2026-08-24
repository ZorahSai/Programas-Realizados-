
#Função para calcular o comissão
def comissao_final(tipo,quantidade):
    if tipo=="8k":
        if quantidade>=10:
            return 550*quantidade
        elif quantidade<=10:
            return 350*quantidade
    elif tipo=="4k":
        if quantidade>=10:
            return 420*quantidade
        elif quantidade<=10:
            return 250*quantidade
    else:
        return 0
#Função para calcular o salário
def salario_liquido_final(salario_inicial):
    inss=salario_inicial*0.08
    salario_liquido=salario_inicial-inss
    if salario_liquido>950:
        imposto=salario_liquido*0.05
        salario_liquido-=imposto
    return salario_liquido
#Variáveis
salario_ao_todo=0
comissao_ao_todo=0
quantidade_de_funcionarios=0
big_comissao=float('-inf')
smal_comissao=float('inf')
while True:
    tipo= input("DIGITE O TIPO DA TV(4k ou 8K) ou DIGITE 'finalizar' PARA TERMINAR DE USAR O PROGAMA:").upper()
    if tipo =="FINALIZAR":
        break
    quantidade=int(input("INSIRA A QUANTIDADE DE TVs VENDIDA: "))
    salario_atual=float(input("INSIRA O SALÁRIO ATUAL DO FUNCIONARIO: "))
    #Comissão
    c=comissao_final(tipo,quantidade)
    salario_ao_todo=salario_atual+c
    salario_liquido=salario_liquido_final(salario_ao_todo)
    #Atualização dos valores
    salario_ao_todo+=salario_liquido
    comissao_ao_todo+=c
    quantidade_de_funcionarios+=1
    if c>big_comissao:
        big_comissao=c
    elif c<smal_comissao:
        smal_comissao=c
    print(f"SALARIO LÍQUIDO: R$ {salario_liquido:.2f}")
#Prints Finais
print("[RESULTADOS FINAIS:]")
print(f"QUANTIDADE DE FUNCIONÁRIOS: {quantidade_de_funcionarios}")
print(f"TOTAL DE SALÁRIOS PAGOS: R${salario_ao_todo:.2f}")
print(f"MÉDIA DAS COMISSÕES: R${comissao_ao_todo/quantidade_de_funcionarios:.2f}")
print(f"MAIOR COMISSÃO: R${big_comissao:.2f}")
print(f"MENOR COMISSÃO: R${smal_comissao:.2f}")
