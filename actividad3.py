precio_orignial= float( input("Ingrese su precio original:"))
descuento= int(input("Ingrese su descuento:"))
precio_final= precio_orignial-(precio_orignial*descuento/100)
print("El precio final es:", precio_final)