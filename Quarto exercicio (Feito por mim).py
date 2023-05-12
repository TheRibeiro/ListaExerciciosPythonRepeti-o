
import random

resultado = random.randint(1, 10)
palpite = int(input("Adivinhe o numero que o computador está pensando:"))
soma = 0

while palpite != resultado:
    soma = soma + 1 
    print('Esse não foi o numero pensado pelo computador tente novamente!!')
    palpite = int(input("Adivinhe o numero que o computador está pensando:"))

print(f'Parabens!!!,você acertou o numero em {soma + 1} tentativas')

#Adivinhar numero que maquina está pensando e anotar quantas tentativas foram feitas para chegar nele
