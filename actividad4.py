print("Las Victimas de la Solcho")

VictimasdeSolcho = ["Vir","Piluso","Luli","Julian"]
                    #0      #1      #2      #3
print (VictimasdeSolcho)
"Luli" in VictimasdeSolcho #Compruebo si esta Luli en la lista
VictimasdeSolcho[1]  = "Flor"
VictimasdeSolcho.append("Cocci")
VictimasdeSolcho.insert(2, "Luli")
del(VictimasdeSolcho[3])
print(VictimasdeSolcho)

edad=13
if edad <= 18:
    print("Sos la proxima victima de la Solcho")
else:
    print("Salvada!!")

numero=22
if numero >=18: 
    print("muy vieja para ser victima de la Solcho")
else: 
    print("sos la proxima victima de la Solcho, preparate")