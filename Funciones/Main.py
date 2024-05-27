from API import GetApiGlobal, PostApi, delete, Put , GetApiGlobalEspecifica
from pprint import pprint



while True:
    Op = int(input("Opciones:\n1-Cargar Gennin Usuario\n2-Busacar Gennin por ID\n3-Modificar Gennin\n4-Borrar gennin\n\n5-Mostrar lista global\n6-Cerrar\n ¿Que desea hacer?:"))
    
    if Op == 1:
        print("Cargar Gennin \n")
        Nombre=input("Nombre:")
        Clan=input("Clan:")
        Aldea=input("Aldea:")
        Rango=input("Rango:")
        Generacion = input("Generacion:")
        
        PostApi(Nombre,Clan,Aldea,Rango,Generacion)
    
    if Op == 2:
        Dato=input("Ingrese ID: ")
        print()
        GetApiGlobalEspecifica(Dato)
        print()
        
            
    if Op == 3:
        Dato=int(input("Ingrese Code:"))
        Nombre = input("Nombre: ")
        Clan = input("Clan: ")
        Aldea = input("Aldea: ")
        Rango = input("Rango: ")
        Generacion= input("Generacion: ")

        Put(Dato,Nombre,Clan,Aldea,Rango,Generacion)
            
    if Op == 4:
        Dato=int(input("Ingrese Code:"))
        delete(Dato)
        
    
    