# corte string, dessa forma ele irá acessa o índice como se fosse um array
mensagem = "Super Mario"
print(mensagem[0])  # Primeiro caractere
print(mensagem[10])  # último caractere
print(mensagem[-1])  # último caractere

print(mensagem[0:5])  # pegando a palavra super
print(mensagem[:5])  # o mesmo de cima, indíce "default" pode ser omitido
print(mensagem[6:])  # pegando a palavra mario

print(mensagem[::2]) # somente os indices pares
print(mensagem[1::2]) # somente os indices impáres
print(mensagem[::-1]) # inverte a string
##
idade = 20
print('idade igual a {}'.format(idade))
# dentro das chaves, ele entende que ali terá um valor numérico
numero = 4 * 4
print('A resposta é {}, e o dobro é {}'.format(numero, numero * 2))
# também podemos fazer dessa forma, onde o f indica que vamos trabalhar com format:
print(f'A respostar é {numero}, e o dobro é {numero * 2}') # só disponível do python 3.6 em diante
# conseguimos também verificar o tamanho de um string, assim:
palavra = "suporte"
print(len(palavra))
