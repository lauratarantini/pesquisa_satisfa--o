
excelente = 0
bom = 0
ruim = 0

#Entrada
for i in range(50):
    print(f"\nEntrevistado {i+1}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

#Processamento
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

#Saída
    print("\nResultado até agora:")
    print("EXCELENTE:", excelente)
    print("BOM:", bom)
    print("RUIM:", ruim)

print("\nRESULTADO FINAL:")
print("EXCELENTE:", excelente)
print("BOM:", bom)
print("RUIM:", ruim)