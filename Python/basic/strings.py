# corte string, dessa forma ele irá acessa o índice como se fosse um array
mensagem = "Super Mario"
print(mensagem[0])  # Primeiro caractere
print(mensagem[10])  # último caractere
print(mensagem[-1])  # último caractere
print(mensagem[0:5])  # pegando a palavra super
##
idade = 20
print('idade igual a {}'.format(idade))
# dentro das chaves, ele entende que ali terá um valor numérico
numero = 4 * 4
print('A resposta é {}, e o dobro é {}'.format(numero, numero * 2))
# também podemos fazer dessa forma, onde o f indica que vamos trabalhar comformat:
print(f'A respostar é {numero}, e o dobro é {numero * 2}')
# conseguimos também verificar o tamanho de um string, assim:
palavra = "suporte"
print(len(palavra))
