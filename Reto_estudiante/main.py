from figuras import Rectangulo, Circulo, probar_figura

def main():
 
 while True:
        print("Opciones: \n 1 - Rectángulo \n 2 - Circulo \n 4 - Salir")
        num = int(input("Ingrese un número: ")) 
        
        if num == 1:
            print("Usted eligió la opción Rectángulo\n")
            base = int(input("Ingrese la base del rectángulo:" ))
            altura = int(input("Ingrese la altura del rectángulo:" ))
            r = Rectangulo(base, altura)
            probar_figura(r)
            

        elif num == 2:
            print("Usted eligió la opción Circulo\n")
            radio = input("Ingrese el radio del rectángulo:" )
            c = Circulo(radio)  
            probar_figura(c)

        elif num == 4:
            print("Terminó el programa")
            break

        else:
            print("Número inválido") 






if __name__ == '__main__':
    main()