clientes_cadastrados = []

for i in range(3):
    print(f'\ncadastro {i+1}')
    cadastro = {}

    cadastro['nome'] = input('Informe o seu nome completo: ')
    cadastro['telefone'] = input('Informe seu telefone: ')
    cadastro['e-mail'] = (input('Informe o seu e-mail: '))

    clientes_cadastrados.append(cadastro)

    
#print(clientes_cadastrados) #Imprime a lista completa de clientes cadastrados

for elemento in clientes_cadastrados:
    print(f'\nNome: {elemento["nome"]}') #Imprime o nome dos clientes cadastrados
    print(f'Telefone: {elemento["telefone"]}') #Imprime o telefone dos clientes cadastrados
    print(f'E-mail: {elemento["e-mail"]}') #Imprime o e-mail dos clientes cadastrados
