from Core import UsserShinobi
from Database import Cursor

def CargarShinobiUsuario(Nombre, Clan , Rango , Aldea):
    Shinobi = UsserShinobi()
    Shinobi.Cargar(Nombre, Clan , Rango , Aldea)
    Shinobi.save()
    
    
    
    
def BuscarShinobisTotales():
    Lista = []
    NinjaBuscado = Cursor.query(UsserShinobi)
    for ninja in NinjaBuscado:
        Lista.append(vars(ninja))
        
    return Lista

def BuscarShinobiUsuario(Dato):
    Lista = []
    
    
    NinjaBuscado = Cursor.query(UsserShinobi).where(UsserShinobi.Nombre == Dato)
    for ninja in NinjaBuscado:
        Lista.append(vars(ninja))
        
    NinjaBuscado = Cursor.query(UsserShinobi).where(UsserShinobi.Clan == Dato )
    for ninja in NinjaBuscado:
        Lista.append(vars(ninja))
        
    NinjaBuscado = Cursor.query(UsserShinobi).where(UsserShinobi.Aldea == Dato)
    for ninja in NinjaBuscado:
        Lista.append(vars(ninja))  
    return Lista

def BuscarShinobiCode(Dato):
    NinjaBuscado = Cursor.query(UsserShinobi).where(UsserShinobi.Code == Dato)
    for Ninja in NinjaBuscado:
        
        return Ninja

def BorrarShinobi(Dato):
    Cursor.delete(Dato)
    Cursor.commit()
    Cursor.flush()
    print()
    
def UpdateShinobi(Dato, Nombre, Clan, Rango,Aldea):
    shinobi = BuscarShinobiCode(Dato)
    shinobi.Nombre = Nombre.lower()
    shinobi.Clan = Clan.lower()
    shinobi.Rango = Rango.lower()
    shinobi.Aldea = Aldea.lower()
    
    shinobi.save()
