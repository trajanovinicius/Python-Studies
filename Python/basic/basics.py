# comando print, mostra na saída uma informação pedida:
print("Hello World")
# dentro do input passamos como parâmetro a mensagem que queremos exibir e o valor,
# que esperamos receber.
# obs: o input sempre irá trabalhar com strings.
nome = input("Digite o seu nome: ")
print('Bem vindo', nome)
# Quando surgir a necessidade de usar números no input, temos que converter para inteiro,
# Dessa forma:
numero = int(input("Insira um número: "))
print(numero * 2)
# Basicamente a função int vai tranformar uma string em inteiro,
# o que é  necessário caso queira trabalhar com número dentro do input
# uma vez que o input trabalha somente com strings.
