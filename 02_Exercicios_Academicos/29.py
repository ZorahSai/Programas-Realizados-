#fahrenheit
def FpraC(fahrenheit):
    c=5/9*(fahrenheit-32)
    return c
while True:
    try:
        f=float(input("DIGITE A TEMPERATURA EM FAHRENHEIT OU 'FINALIZAR' PARA ENCERRAR O PROGRAMA:"))
        if f == "FINALIZAR":
            break
        c=FpraC(f)
        print(f"A TEMPERATURA EM GRAUS CELSIUS É DE: {c:.2f}°C")
    except ValueError:
        print("POR FAVOR, DIGITE UMA TEMPERATURA OU 'FINALIZAR' PARA ENCERRAR O PROGAMA!")
        