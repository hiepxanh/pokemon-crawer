##pokemon_name = "Ivysaur"
##
##import requests
##link = "http://bulbapedia.bulbagarden.net/wiki/"+pokemon_name+"_(Pok%C3%A9mon)"
##response = requests.get(link)
###print(response)
##
##from bs4 import BeautifulSoup
##soup = BeautifulSoup(response.content, 'html.parser')
##table = soup.find("table",{"class":"roundy","width":"100%"})
##table_rows = table.find_all("tr",{})
##color = table.get("style")
##print("result 1 (NAME):", pokemon_name) # pokemon name
##print("result 2 (ID):", table_rows[0].th.big.big.a.span.get_text()) # pokemon ID
##print("result 3 (COLOR):", color.split(";")[0].split(":")[1]) # pokemon color
##print("result 4 (IMG):", table_rows[3].td.a.img.get("src")) # pokemon image

import requests
from bs4 import BeautifulSoup

class Pokemon:
    def __init__ (self,name, generation):
        self.name = name
        self.generation = generation
        link = "http://bulbapedia.bulbagarden.net/wiki/"+self.name+"_(Pok%C3%A9mon)"
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find("table",{"class":"roundy","width":"100%"})
        table_rows = table.find_all("tr",{})
        color = table.get("style")
        self.id = table_rows[0].th.big.big.a.span.get_text()
        self.color = color.split(";")[0].split(":")[1]
        self.image = table_rows[3].td.a.img.get("src")
       

##Ivysaur = pokemon("Ivysaur")
##print("result 1 (NAME):", Ivysaur.name) # pokemon name
##print("result 2 (ID):", Ivysaur.id) # pokemon ID
##print("result 3 (COLOR):", Ivysaur.color) # pokemon color
##print("result 4 (IMG):", Ivysaur.image) # pokemon image

