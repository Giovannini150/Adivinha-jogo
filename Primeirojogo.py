import random

print("Jogo de adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 e 100.")
print("Você tem sete tentativas para acerta o número secreto.")

numero_secreto = random.randint(1, 100)
contador = 7
acertou = False 
while contador > 0:
    tentativa = int(input("Digite o seu palpite:"))

    if tentativa == numero_secreto:
         print("Parabéns! Você acertou!")
         acertou = True
         break
    elif tentativa < numero_secreto:
         print("Você errou! O número secreto é maior que o seu palpite")
    else:
         print("Você errou! O número secreto é menor que o seu palpite")
    contador -= 1

if not acertou:
    print("O número secreto era", numero_secreto)
    print("Você perdeu! O número secreto era", numero_secreto)

