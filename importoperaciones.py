import operaciones as o

a=float(input('Introduce un número para a:'))
b=float(input('Introduce un número para b:'))

def main():

    suma=o.suma(a,b)
    print('El resultado de la suma a+b es:',suma)
    resta=o.resta(a,b)
    print('El resultado de la resta a-b es:',resta)
    multiplicacion=o.multiplicar(a,b)
    print('El resultado de la multiplicación a*b es:',multiplicacion)
    division=o.dividir(a,b)
    print('El resultado de la division a/b es:',division)

main()