num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print(num1)
print(num2)
print(num3)
