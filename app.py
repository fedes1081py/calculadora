class ImprimirMixin:

    @classmethod
    def mostrar_info(cls,message,resultado):
        resultado = round(resultado,2)
        print(f"El resultado de la {message} fue {resultado}" )

class ObtencionNumeroMixin:
    #vamos a validar el numero pedido
    @classmethod
    def pedir_numero(cls,operacion):
        numeros = []
        i = 1
        while i<3:
            try:
                num = float(input(f"Decime el numero {i}:"))
                if i == 2 and num == 0 and operacion == 'division':
                    raise ZeroDivisionError
                numeros.append(num)
                i+=1
            except ValueError:
                print("Dato invalido")
            except ZeroDivisionError:
                print("No se puede dividir por cero ingresa otro numero")
        return numeros


class ValidarOperacionMixin:
    @classmethod
    def validar(cls,valores,menu,mensaje):
        while True:
            try:
                print(menu)
                op = input(mensaje)
                if not op.strip() in valores.values():
                    raise ValueError
                return op
            except ValueError:
                print("Dato equivocado")

class Calculadora:
    def __init__(self):
        self.operaciones = {
            "1":"suma",
            '2': "resta",
            '3': 'multiplicacion',
            '4': 'division',
            '5': 'salir'
        }
        self.operadores = {
            "suma":  "+",
            "resta" : "-",
            "multiplicacion" : "*",
            "division" : "/"
        }
    
    def operacion(self):
        opcion_operacion = self.pedir_operacion()
        if opcion_operacion == 'salir':
            return [],[],[]
        num1 , num2 = self.pedir_numeros(opcion_operacion)
        return opcion_operacion,num1,num2
    
    def pedir_operacion(self):
        opcion = self.validar_operacion()
        return opcion
    
    def validar_operacion(self):
        menu = self.mostrar_menu()
        mensaje = "Decime la opcion escrita: "
        op = ValidarOperacionMixin.validar(self.operaciones,menu,mensaje)
        return op

    def mostrar_menu(self):
        mensaje = ""
        for key,values in self.operaciones.items():
           mensaje += f"{key}) {values}\n"
        return mensaje
        
    def pedir_numeros(self,opcion_operacion):
        num1,num2 = ObtencionNumeroMixin.pedir_numero(opcion_operacion)
        if num2 == 0 and opcion_operacion == 'division':
            print("No se puede dividir por 0")
            return False
        return [num1,num2]
    
    def resolver(self,operacion,num1,num2):
        resultado = 0
        if operacion == 'suma':
            resultado = self.sumar(num1,num2)
        elif operacion == 'resta':
            resultado = self.restar(num1,num2)
        elif operacion == 'division':
            resultado = self.division(num1,num2)
        elif operacion == 'multiplicacion':
            resultado = self.multiplicacion(num1,num2)
        return resultado

        
    def sumar(self,num1,num2):
        return num1+num2
    def restar(self,num1,num2):
        return num1-num2
    def division(self,num1,num2):
        return num1/num2
    def multiplicacion(self,num1,num2):
        return num1*num2
calcu = Calculadora()
resultado = 0
while True:
    operacion, num1, num2 = calcu.operacion()
    if operacion == []:
        print("Adios")
        break
    resultado = calcu.resolver(operacion,num1,num2)
    ImprimirMixin.mostrar_info(operacion,resultado)




