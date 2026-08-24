''' 13. A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os 
demais são dados pela soma dos dois anteriores.  Faça um programa que imprima os 
“n” primeiros termos da série, sendo “n” dado pelo usuário. '''

# primeiros numero fibo
def fibonacci(n):
    termos = [1, 1]

    while len(termos) < n:
        novo_termo = termos[-1] + termos[-2]
        termos.append(novo_termo)

    return termos
n = int(input("Digite o número de termos da série de Fibonacci (n): "))

#chama a função 
serie_fibonacci = fibonacci(n)
print(f"Os {n} primeiros termos da série de Fibonacci são: {serie_fibonacci}")
