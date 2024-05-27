from sqlalchemy import Column , Integer , String 
from Database import Cursor , Base

class UsserShinobi(Base):
    __tablename__ = "ShinobiUsuario"

    Code = Column("Code",Integer, autoincrement= True , unique= True , primary_key= True)
    Nombre = Column ("Nombre", String)
    Clan = Column("Clan" , String)
    Rango = Column("Rango" , String)
    Aldea = Column("Aldea" , String)
    

    def __init__(self, 
                 Rango = None,
                 Nombre = None , 
                 Aldea = None,
                 Clan = None):
        
        self.Nombre = Nombre
        self.Rango = Rango
        self.Aldea = Aldea
        self.Clan = Clan

    def Cargar(self, Nombre , Clan, Rango , Aldea):
        self.Nombre = Nombre.lower()
        self.Clan = Clan.lower()
        self.Rango = Rango.lower()
        self.Aldea = Aldea.lower()
        

    def save(self):
        Cursor.add(self)
        Cursor.commit()
        Cursor.flush()

