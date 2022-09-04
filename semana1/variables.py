# texto = ("jjsdjsdj"
# "jjjsjksdjk"
# "iueueu"
# )

# nombre="Freddy"
# apellido="yo"

# print(f"{nombre} {apellido}")


# numbera=int(input("ingrese un numero"))
# numberb=int(input("ingrese otro numero"))

# print(f'la suma de {numbera}+{numberb}= {numbera+numberb}' )
# # print(f'la Multiplicacion de {numbera}*{numberb}= {numbera*numberb}' )
# # print(f'la Division de {numbera}/{numberb}= {numbera/numberb}' )

# personas=["alan" , "andres" , "freddy", "etc"]

# # personas.pop(3)
# # print(f'pop->{personas}')

# # personas.append("Luis")
# # print(f'append -> {personas}')

# for index,value in enumerate(personas):
#     print(index,value)


# igual, aux = 0, 0
# texto = input("Ingrese la palabra que desea evaluar: ")
# for ind in reversed(range(0, len(texto))):
#   if texto[ind].lower() == texto[aux].lower():
#     igual += 1
#   aux += 1
# if len(texto) == igual:
#   print("El texto es palindromo!")
# else:
#   print("El texto no es palindromo!")


from datetime import date


year=int(input("ingrese su year de nacimiento: "))
for i in range(year,2022):
    print(f'"en el a;o"{i} "tenia" {i-year}')