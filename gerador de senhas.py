import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input("digite o numero de caracteres da sua senha\n"))
senha = ""
condicao = input("vc gostaria que algum caractere não possa ser utilizado\n").lower
if condicao == "sim":
    verif = True
    bloq = input("qual caractere vc gostaria de bloquear\n")
else:
    verif = False

for i in range(tamanho):
    digito = random.choice(caracteres)
    if verif == True and digito == bloq:
        tamanho + 1
        continue
    else:
        senha += digito

print(senha)
