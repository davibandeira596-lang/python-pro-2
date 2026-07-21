import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input("digite o numero de caracteres da sua senha\n"))
senha = ""

condicao = input("vc gostaria que algum caractere não possa ser utilizado\n").lower()
if condicao == "sim":
    verif = True
    bloq = input("quais caracteres vc gostaria de bloquear (sem espaço entre eles)\n")
else:
    verif = False
    bloq = ""

while len(senha) < tamanho:
    digito = random.choice(caracteres)
    if verif and digito in bloq:
        continue
    senha += digito

print(senha)
