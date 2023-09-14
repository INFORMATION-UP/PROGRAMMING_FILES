#▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▶EJERCICIO #1◀▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
#Realizar un programa que muestre el promedio aprobado o reprobado de un estudiante.
#▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰

#CÓDIGO:
class estudiante: #se define la clase y su nombre 
    def __init__(self): #metodo constructor
        self.nombre = input("Ingrese su nombre: ")  
        self.curso = input("Ingrese su curso: ")
        self.nota1 = float (input("Ingrese su primera nota: "))
        self.nota2= float (input("Ingrese segunda nota: "))
        self.asistencia = float(input("Ingrese porcentaje de asistencia: "))
        
    def Promedio(self): #metodo de calculo del promedio
        media = float((self.nota1 + self.nota2)/2)  #atributo de metodo
        suma = self.nota1 + self.nota2 
        print ("Su promedio es: ", media)
        if media>=7 and self.asistencia >= 70:
            print(self.nombre + ", Usted ha aprobado") 
        else:
            print("Lo sentimos " + self.nombre + ", usted a reprobado la materia por faltas")
        print("Por no alcanzar el minimo de asistencia: ", self.asistencia)    

    def supletorio(self):
        pass      
              
alumno = estudiante() #gestionar la clase mediante una variable
print(alumno.Promedio()) #llamar al metodo de calculo mediante la varibale declarada