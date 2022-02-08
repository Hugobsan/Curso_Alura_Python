print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

print("Você digito:", chute)

print("Você acertou!" if numero_secreto == chute else "Você errou")