def dobro(a):
    r = a * 2
    #print(r)
    return r # Retorna o resultado para quem chamou

def triplo(a):
    r = a * 3
    #print(r)
    return r # Retorna o resultado para quem chamou

def quadrado(a):
    r = a ** 2
    #print(r)
    return r # Retorna o resultado para quem chamou

#num1 = 5
#num2 = 9
#soma(num1, num2)

  
numero = float(input("Digite um número: "))

resultado1 = dobro(numero) # Chamada da função
resultado2 = triplo(numero) # Chamada da função
resultado3 = quadrado(numero) # Chamada da função

print(f"O dobro de  {numero} é {resultado1}")
print(f"O triplo de  {numero} é {resultado2}")
print(f"O quadrado de  {numero} é {resultado3}")