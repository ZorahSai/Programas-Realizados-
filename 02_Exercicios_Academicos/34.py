import math
def resolver_eq(a,b,c):
    if a ==0:
        raise ValueError("O valor de 'a' não pode ser zero!!")
    discrimiante = b**2 - 4*a*c
    if discrimiante > 0:
        r1 = (-b + math.sqrt(discrimiante)) / (2 * a)
        r2 = (-b - math.sqrt(discrimiante)) / (2 * a)
        return 2, r1, r2
    elif discrimiante == 0:
        r = -b / (2 * a)
        return 1, r
    else:
        return 0
def main():
    try:
       a=float(input("INSIRA O VALOR DE A: "))
       b=float(input("INSIRA O VALOR DE B: "))
       c=float(input("INSIRA O VALOR DE C: "))
       result = resolver_eq(a, b, c)
       q_raizes = result[0]
       if q_raizes ==2:
            r1,r2=result[1], result[2]
            print(f"As raízes da equação são: {r1:.2f} e {r2:.2f}.")
       elif q_raizes ==1:
            r=result[1]
            print(f"A raís da equação é: {r:.2f}.")
       elif q_raizes==0:
            print("Não existem raízes reais na equação")
    except ValueError as e: 
        print(f"ERRO: {e}")
if __name__ == "__main__":
    main()

