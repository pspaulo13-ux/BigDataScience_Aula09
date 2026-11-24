produto1 = {} #Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'marca': 'Lenovo'
}    #Chaves | Valores

#print(type(produto))    Saber o tipo de dado que tem dentro do dicionário.
print(produto) #Imprime o dicionário completo (chaves e valores)

print(produto['nome']) #Imprime o valor da chave 'nome'
print(produto['preco']) #Imprime o valor da chave 'preco'

#Alterando valores

produto['marca'] = 'Positivo' #Alterando o valor da chave 'marca'
print(produto) #Imprime o dicionário completo (chaves e valores)

# Adicionando Chaves
produto['tela'] = '18"' #Adicionando a chave 'tela' com o valor '15 polegadas'
print(produto) #Imprime o dicionário completo (chaves e valores)

#Deletando uma chave
del produto['marca'] #Deletando a chave 'marca'
print(produto) #Imprime o dicionário completo (chaves e valores)

print(produto.keys()) #Imprime todas as chaves do dicionário
print(produto.values()) #Imprime todos os valores do dicionário
print(produto.items()) #Imprime todas as chaves e valores do dicionário
