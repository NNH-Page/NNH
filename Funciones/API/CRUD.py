import requests
import json
from pprint import pprint


url = "https://6654000b1c6af63f46761430.mockapi.io/index/UserPj"

def GetApiGlobal():
    Get= requests.get(url)
    pprint(json.loads(Get.text)) 
    
def GetApiGlobalEspecifica():
    Get= requests.get(f"{url}/{id}")
    pprint(json.loads(Get.text)) 
    

def PostApi(Nombre, Clan , Aldea , Rango):
 
    Info =  {
  "Nombre": Nombre ,
  "Clan": Clan,
  "Aldea": Aldea,
  "Rango": Rango}
    
    Post= requests.post(url,data=Info)
    pprint(Post.text)
        

def delete(id):
    endpoint = f"{url}/{id}"
    Del = requests.delete(endpoint)
    print(Del.text)


def Put(id,Nombre, Clan , Aldea , Rango):
    endpoint = f"{url}/{id}"
    Info =  {
    "Nombre": Nombre ,
    "Clan": Clan,
    "Aldea": Aldea,
    "Rango": Rango}
    put = requests.put(endpoint,data=Info)
    print(put.text)

