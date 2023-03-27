def multiplo(num1 , num2):
    if num1%num2 == 0:
        return True
    else:
        return False
    
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))

multiplicar = multiplo(num1=num1,num2=num2)

print(multiplicar)

