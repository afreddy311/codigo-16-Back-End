from asyncore import write


# def dibujarRectangulo(ancho,alto):
#     for j in range(0,alto):
#         print("\n")
#         for i in range(0,ancho):
#                 print("*",end=""),

# dibujarRectangulo(2,2)


num = int(input("ingrese un numero :"))
while num != 1:
    if num%2==0:
        num=num/2
    else :
        num=num*3+1

    print(num,end=" <-> "),

