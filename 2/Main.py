from API import GetApiGlobal, PostApi, delete, Put , GetApiGlobalEspecifica
from Controller import BuscarShinobisTotales, BuscarShinobiUsuario, CargarShinobiUsuario,UpdateShinobi, BorrarShinobi, BuscarShinobiCode
from pprint import pprint
from Database import Base , DB_ENGINE

Base.metadata.create_all(DB_ENGINE)

while True:
    Op = int(input("Opciones:\n1-Cargar Gennin Usuario\n2-Busacar Gennin por ID\n3-Modificar Gennin\n4-Borrar gennin\n\n5-Mostrar lista global\n6-Cerrar\n ¿Que desea hacer?:"))
    
    if Op == 1:
        print("Cargar Gennin \n")
        Nombre=input("Nombre:")
        Clan=input("Clan:")
        Aldea=input("Aldea:")
        Rango=input("Rango:")
        
        CargarShinobiUsuario(Nombre,Clan,Rango,Aldea)
        PostApi(Nombre,Clan,Rango,Aldea)
    
    if Op == 2:
        Dato=input("Ingrese Nombre Aldea o Clan:").lower()
        ListaNinjas=(BuscarShinobiUsuario(Dato))
        print()
        for Ninja in ListaNinjas:
            print(f"ID: {Ninja['Code']}")
            print(f"Nombre: {Ninja['Nombre']}")
            print(f"Clan: {Ninja['Clan']}")
            print(f"Aldea: {Ninja['Aldea']}")
            print(f"Rango: {Ninja['Rango']}")
            print()
            
    if Op == 3:
        Dato=int(input("Ingrese Code:"))
        Nombre = input("Nombre:")
        Clan = input("Clan:")
        Aldea = input("Aldea:")
        Rango = input("Rango:")


        UpdateShinobi(Dato,Nombre,Clan,Rango,Aldea)
        Put(Dato,Nombre,Clan,Aldea,Rango)
            
    if Op == 4:
        Dato=int(input("Ingrese Code:"))
        BorrarShinobi(BuscarShinobiCode(Dato))
        delete(Dato)
        
    
    