git remote add origin https://github.com/Moraes97-Murilo/CursoGit.gii

op = input("Você gostaria de somar, subtrair, multiplicar ou dividir? ")
if op == "somar":
    a = float (input ("Digite o primeiro valor: ")) 
    b = float (input ("Digite o segundo valor: ")) 
    print (a+b)
    
elif op == "subtrair":
    a = float (input ("Digite o primeiro valor: ")) 
    b = float (input ("Digite o segundo valor: ")) 
    print (a-b)
    
elif op == "multiplicar":
    a = float (input ("Digite o primeiro valor: ")) 
    b = float (input ("Digite o segundo valor: ")) 
    print (a*b)
    
elif op == "dividir":
    a = float (input ("Digite o primeiro valor: ")) 
    b = float (input ("Digite o segundo valor: ")) 
    print (a/b)
    
else:
    print("Operação desconhecida.")
