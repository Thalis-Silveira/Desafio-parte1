idades = []
for i in range(3):
  idade = int(input(f"Forneça a idade {i+1}º: \n"))
  while(idade <  5 or idade > 100):
    print("Idade inválida, são aceitas somente idades entre 5 a 100")
    idade = int(input(f"Forneça a idade {i+1}º: \n"))
  idades.append(idade)

idades.sort()

print(idades[1])