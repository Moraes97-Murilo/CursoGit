git remote add origin https://github.com/Moraes97-Murilo/CursoGit.gii

op = input("Você gostaria de somar, subtrair, multiplicar ou dividir? ")
    if op == "somar":
        a = float (input ("Digite o primeiro valor: ")) 
        b = float (input ("Digite o segundo valor: ")) 
        return a+b
    if op == "subtrair":
        a = float (input ("Digite o primeiro valor: ")) 
        b = float (input ("Digite o segundo valor: ")) 
        return a-b
    if op == "multiplicar":
        a = float (input ("Digite o primeiro valor: ")) 
        b = float (input ("Digite o segundo valor: ")) 
        return a*b
    if op == "dividir":
        a = float (input ("Digite o primeiro valor: ")) 
        b = float (input ("Digite o segundo valor: ")) 
        return a/b
    else:
        print("Operação desconhecida.")
    
