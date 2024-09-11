letra = input("Digite uma letra: ")
if letra == 'a' or 'i' or 'u' or 'e' or 'o':
    print("Sua letra é uma vogal!")
else:
    print("Sua letra é uma consoante!")
#Exercicio 6:
altura = float(input("Digite sua altura:"))
sexo = int(input("Digite seu sexo:(1) feminino (2) masculino: "))
if sexo == 1:
    print(f"Seu MMC ideal é {(62.1*altura)-44.7}")
else:
    print(f"Seu MMC ideal é {(72.7 * altura)-58}")

#Exercicio 5:
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
z = int(input("Digite outro numero: "))
if x>y:
    if y>z:
        print(f"{x}, {y}, {z}")
    else:
        print(f"{x}, {z}, {y}")
elif y>x:
    if z>y:
        print(f"{z}, {y}, {x}")
    else:
        print(f"{z}, {x}, {y}")
#Exercicio 8
lados = int(input("Diga a qntd de lados: "))
if lados < 3 or lados > 5:
    print("Não é um poligono!")
else:
    comprimento = (float(input("Digite o comprimento: ")))
    if lados == 3:
        perimetro = lados*comprimento
        print(f"Triangulo de perímetro {perimetro}")
    elif lados == 4:
        perimetro = lados*comprimento
        print(f"Quadrado de perimetro {perimetro}")
    elif lados == 5:
        perimetro = lados*comprimento
        print(f"Pentágono de perimetro {perimetro}")


