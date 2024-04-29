class operaciones:

    def __init__(self) -> None:
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero."

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

'''
por que la funcion main?
cual es la estructura de la clase
que es git y 5 comandos
mañana tratar el codigo actual a una clase
'''
def menu():
    print("Calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("6. Todas las operaciones")



def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '5':
            print("¡Hasta luego!")
            break
       

        elif opcion in ('1', '2', '3', '4','6'):

        
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print("Resultado de la suma es:", sumar(num1, num2))
            elif opcion == '2':
                print("Resultado de la resta es:", restar(num1, num2))
            elif opcion == '3':
                print("Resultado de la multiplicacion es:", multiplicar(num1, num2))
            elif opcion == '4':
                print("Resultado de la division es:", dividir(num1, num2))
            elif opcion =='6':
                print("El resultado de todas las operaciones es ","suma", sumar(num1, num2), "resta", restar(num1, num2), "multiplicacion", multiplicar(num1, num2), "division", dividir(num1, num2))
            
            continuar = input("¿Desea realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                print("¡Hasta luego!")
                break     
       
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



if __name__ == "__main__":
    main()