qtd = int(input("Digite o número de pessoas: "))
# x x=1 é o mesmo que: x = x+1
# x -=10 é o mesmo que: x = x-10
while qtd > 0:
    print("Bom dia")
    qtd -= 1
    if qtd == 2:
        print("Mal dia para você")
    qtd -= 1
# podemos ir aninhando também, como foi feito em cima, acrescentando ifs...
