#Comentrio agregado para conflicto en ramas
#Ojo

class Calculadora:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1+self.num2
        print("La suma es: ", suma)

    def restar(self):
        resta = self.num1-self.num2
        print("La resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1*self.num2
        print("La multiplicación es: ", multiplicacion)

    def dividir(self):
        divicion = self.num1/self.num2
        print("La divición es: ", divicion)


num1 = input("Primer número: ")
num2 = input("Segundo numero: ")

calculadora = Calculadora(num1, num2)
