pergunta1 = str(input("Telefonou para a v�tima? "))
pergunta1 = pergunta1.upper()

pergunta2 = str(input("Esteve no local do crime? "))
pergunta2 = pergunta2.upper()

pergunta3 = str(input("Mora perto da v�tima? "))
pergunta3 = pergunta3.upper()

pergunta4 = str(input("Devia para a v�tima? "))
pergunta4 = pergunta4.upper()

pergunta5 = str(input("J� trabalhou com a v�tima? "))
pergunta5 = pergunta5.upper()

respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

afirmacoes = 0
for resp in respostas:
  if resp == "SIM":
    afirmacoes+=1

if afirmacoes == 2:
  print("Suspeito")

elif afirmacoes>=3 and afirmacoes <=4:
  print("Cumplice")

elif afirmacoes == 5:
  print("Assasino")

else:
  print("Inocente")
