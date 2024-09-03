operación = input("Ingresa el tipo de operacion que desea ejecutar:(+ - * /)")
num1 = int (input("Ingrese el primer numero:"))
num2 = int (input("Ingrese el segundo numero:"))

if operación == "+":
    print(num1 + num2)
elif operación == "-":
    print(num1 - num2)
elif operación == "*":
    print(num1 * num2)
elif operación == "/":
    print(num1 / num2)
else:
    print("Operación invalida")

