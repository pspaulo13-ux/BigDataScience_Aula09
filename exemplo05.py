def soma(a, b):
    r = a + b
    #print(r)
    return r # Retorna o resultado para quem chamou

#num1 = 5
#num2 = 9
#soma(num1, num2)

for i in range(3):   
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = soma(num1, num2) # Chamada da função
    print(f"A soma de {num1} e {num2} é {resultado}")