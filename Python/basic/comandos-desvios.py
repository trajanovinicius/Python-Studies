# Comando IF:

cargo = input('Insira seu cargo: ')

# O bloco de código em python, não utiliza chaves, é tudo pela identação.
# A identação no python é extremamante importante, sem ela, além de feio o código,
# estará errado.
# Se quiser inserir os () não tem problema.
if cargo == cargo:
    print('Acesso liberado')
else:
    print('Acesso Negado')
print('Final')

# caso tenha um cenário no qual o if terá múltiplas condições, poderá ser feito assim:
idade = int(input('Insira sua idade: '))
if idade > 65:
    print('Acesso prioritário')
elif idade < 18:
    print('Acesso negado')
else:
    print('Acesso Liberado')
print('Final')
# utiliza-se elif, ao invés de else if, para fazer o que chamamos de if aninhado.
