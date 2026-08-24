#14. Construa  um  programa  que  calcule  e  mostre  a  soma  dos  30  primeiros  termos  da 
#série: (450/10) + (445/11)+ (440/12) +(435/13)...

num_termos = 10
soma = float(sum((450 - 5 * i) / (10 + i) for i in range(num_termos)))
print(f"A soma dos primeiros {num_termos} termos da série é: {soma:.2f}")
