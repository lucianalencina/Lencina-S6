class Chatbot:
    def  __init__(self):
        self.options ={
            "inicio": {
                "mensaje": "Bienvenidos al chatbot ¿En qué te puedo ayudar?"
                "opiciones":[
                    "1. Productos",
                    "2. Contactos",
                    "3. FAQ"
                ]
            },


            "Productos":{
                "1. Shatter Me, Tahereh Mafi",
                "2. Harry potter, J.K. Rowling",
                "3. Percy Jackson, Rick Riordan",
                "4. Maze runner, James Dashner",
                "5. El inventor de juegos, Pablo de Santis"
                "6. Still with you, Lily del Pilar"
            },


            "Harry potter, J.K. Rowling":{
                "1. Ingles"
                "2. Español"
                "3. Aleman"
                "4. Frances"
            },
               "Percy Jackson, Rick Riordan":{
                "1. Ingles"
                "2. Español"
                "3. Aleman"
                "4. Frances"
            },
             "Maze runner, James Dashner":{
                "1. Ingles"
                "2. Español"
                "3. Aleman"
                "4. Frances"
            },
             "El inventor de juegos, Pablo de Santis":{
                "1. Ingles"
                "2. Español"
                "3. Aleman"
                "4. Frances"
            },
             "Still with you, Lily del Pilar":{
                "1. Ingles"
                "2. Español"
                "3. Aleman"
                "4. Frances"
             }
        }
        
        self.respuesta = {
            "producto_Shatter Me" : "$16",
              "producto_Harry potter" : "$10", 
              "producto_Percy Jackson" : "$13",
              "producto_Maze runner" : "$15",
              "producto_El inventor de juegos" : "$8",
              "producto_Still with you" : "$20"
        }

         if self.estado_actual == "inicio":
                if opcion == 1:
                    self.estado_actual = "productos"
                elif opcion == 2:
                    print("\n📞 Información de Contacto:")
                    print(self.respuestas["contacto"])
                elif opcion == 3:
                    print("\n FAQ:")
                    print(self.respuestas["faq"])
                

            #RESPUESTAS SECCIONES

            elif self.estado_actual == "secciones":
                if opcion == 1:
                    self.estado_actual = "kinder"
                elif opcion == 2:
                    self.estado_actual = "primary"
                elif opcion == 3:
                    self.estado_actual = "middle"
                elif opcion == 4:
                    self.estado_actual = "senior"
                elif opcion == 5:
                    self.estado_actual = "inicio"
     
            #RESPUESTAS POR AREAS
                    
            elif self.estado_actual in ["kinder", "primary", "middle", "senior"]:
                if opcion == 1:  # Jornada
                    print(f"\n🕒 Jornada {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_jornada"])
                elif opcion == 2:  # Edades/Actividades/Electivas
                    if self.estado_actual == "kinder":
                        print("\n👶 Edades:")
                        print(self.respuestas["kinder_edades"])
                    elif self.estado_actual == "senior":
                        print("\n📚 Electivas y Orientativas:")
                        print(self.respuestas["senior_electivas"])
                    else:
                        print(f"\n📋 Actividades {self.estado_actual.capitalize()}:")
                        print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 3:  # Actividades
                    print(f"\n🎯 Actividades {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 4:  # Volver a secciones
                    self.estado_actual = "secciones"
                elif opcion == 5:  # Volver al inicio
                    self.estado_actual = "inicio"
                    
        except Exception as e:
            print(f"\n❌ Error procesando la opción: {e}")
            print("Por favor, intenta nuevamente.")

    def ejecutar(self):
        print("\n¡Bienvenido al ChatBot del Day School! 🎓")
        
        while True:
            self.mostrar_menu()
            opcion = input("\n➤ Ingresa el número de la opción deseada: ").strip()
            
            if opcion.lower() == 'q':
                print("\n¡Gracias por usar nuestro ChatBot! ¡Hasta pronto! 👋")
                break
                
            self.procesar_entrada(opcion)
