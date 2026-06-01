soma = 0
quantidade = 0
entrada = ""

while entrada != "sair":
    entrada = input("Digite para entrar ou sair: ")

    if entrada == "sair":
        print("Obrigada por utilizar nossos serviços")

    else:
        nota = float(input("Digite uma nota: "))
        soma = soma + nota
        quantidade = quantidade + 1

        if quantidade == 1:
            maior = nota
            menor = nota

        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

media = soma / quantidade

print("A soma de todas as notas é:", soma)
print("A média da turma é:", media)
print("A maior nota digitada é:", maior)
print("A menor nota digitada é:", menor)()