import os


def limpiar_screem():
    os.system("cls")


def entrada_datos():
    base = float(input("Ingrese la base del tringulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    return base, altura


def Calcular_area():
    base, altura = entrada_datos()
    Area = (base*altura)/2
    print(f'El area del triangulo es: {Area}')


def tipo_tringangulo():
    print("Para conocer el tipo de triangulo ingresar informacion adicional")
    print("Ingre la medida de los lados del triangulo")
    lado_a = float(input("Ingrese medida del primer lado: "))
    lado_b = float(input("Ingrese mediad del segundo lado: "))
    lado_c = float(input("Ingrese medidad del tercer lado: "))
    if(lado_a == lado_b == lado_c):
        print("El tringulo es equilatero")
    else:
        if((lado_a == lado_b) != lado_c or (lado_a == lado_c) != lado_b or (lado_b == lado_c) != lado_a):
            print("El triangulo es isoceles")
        else:
            if(lado_b != lado_a and lado_b != lado_c and lado_a != lado_c):
                print(" el tringulo es Escaleno")
            else:
                print("No es un triangulo")


def main():
    b = True
    while(b == True):
        Calcular_area()
        print("Desea conocer el tipo de triangulo Y/N")
        dato = str(input("Ingrese el su respuesta: "))
        if (dato == "Y"):
            tipo_tringangulo()
            input("Enter para continar")
            limpiar_screem()
            print("Desea realizar una nueva consulta Y/N")
            dato = str(input("Ingrese el su respuesta: "))
            if(dato == "Y"):
                limpiar_screem()
                continue
            else:
                b = False
        elif(dato == "N"):
            print("Gracias por usar este programa")
            b = False
        else:
            print("El datos ingreado no es correcto")


if __name__ == '__main__':
    main()
