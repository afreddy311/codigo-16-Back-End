# from camelcase import CamelCase
# instancia  = CamelCase()
# texto = "hola ..."
# print(instancia.hump(texto))

def ejercicios(num2,num1=10):
    if (num1+num2)%2==0:
        print(f'{(num1+num2)/2}')
    else:
        print(f'{num1+num2}')

ejercicios(15)


def Notas(*args):
    if args>10:
        print("aprobado")
    else:
        print("desaprobado")

    
    
