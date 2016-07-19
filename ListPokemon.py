import requests
from bs4 import BeautifulSoup
class ListPokemon:
    def __init__ (self, generation):
        self.generation = generation
        
    def craw(self):
        response = requests.get("http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id = "mw-content-text")
        tables=content.find_all("table")
        gen = tables[self.generation]
        table_rows= gen.find_all("td",{})
        list = []
        for single_row in table_rows:
        # truy tim ten
            try:
                name = single_row.a.img.get('alt')
            except AttributeError:
                continue
            else:    
                if  name:
                    #print(name)
                    list.append(name)
        return list
