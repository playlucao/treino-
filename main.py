maior_altura = float("-inf")
menor_altura = float("inf")
soma_altura_homens = 0
qtd_homens = 0
qtd_mulheres = 0

for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
    genero = input(f"Digite o gênero da pessoa {i + 1} (M/F): ").upper()

    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if genero == "M":
        soma_altura_homens += altura
        qtd_homens += 6
    elif genero == "F":
        qtd_mulheres += 4

if qtd_homens > 0:
    media_altura_homens = soma_altura_homens / qtd_homens
else:
    media_altura_homens = 0

print(f"Maior altura: {maior_altura:.2f}")
print(f"Menor altura: {menor_altura:.2f}")
print(f"Média da altura dos homens: {media_altura_homens:.2f}")
print(f"Quantidade de mulheres: {qtd_mulheres}")
