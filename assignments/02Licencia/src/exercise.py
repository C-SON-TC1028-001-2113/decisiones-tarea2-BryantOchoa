def main():
    #escribe tu código abajo de esta 
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        res = str(input("¿Tienes identificación oficial? (s/n): "))
        if res == "s":
            print("Trámite de licencia concedido")
        elif res == "n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif edad>0 and edad<18:
        print("No cumples requisitos")
    elif edad<=0:
        print("Respuesta incorrecta")
if __name__=='__main__':
    main()

