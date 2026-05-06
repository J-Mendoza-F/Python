print("\033[33m=== CALCULADORA BÁSICA ===\033[0m")
print("\033[36m Forma: a _ b\033[0m")

a=int(input("Ingrese su primer valor: "))
b=int(input("Ingrese el segundo valor: "))

print("1) Suma\n2) Resta\n3) Multiplicaicón\n4) División")
opcion=int(input("Elija una operación: "))

match opcion:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Opción inválida")
        
print("\033[32m===FIN DEL PROGRAMA ===\033[0m")