#Funções

def saudacao():
    print("Olá!")

def saudacao2(x): # X é um Parâmentro
    print(f'Olá, {x}!')


#____________________

nome = input('Nome: ')
saudacao2(nome) #Passagem por parâmetro
saudacao2('Antonio')
saudacao2('Pedro')  

