
lista_catalogo = []

for i in range(2):
    print(f'\nLivro {i+1}')
    livro = {}

    livro['titulo'] = input('Informe o título do livro: ')
    livro['autor'] = input('Informe o autor do livro: ')
    livro['ano'] = int(input('Informe o ano de publicação do livro: '))
    livro['genero'] = input('Informe o gênero do livro: ')
    livro['paginas'] = float(input('Informe o número de páginas do livro: '))

    lista_catalogo.append(livro)

print(lista_catalogo) #Imprime a lista completa de livros cadastrados

for elemento in lista_catalogo:# foi usado para percorrer a lista de livros cadastrados e verificar apenas livros apartir de 2020.
        if elemento['ano'] >= 2020:
         print(elemento['titulo']) #Imprime os livros publicados a partir de 2020
         print(elemento['ano']) #Imprime o autor dos livros publicados a partir de 2020