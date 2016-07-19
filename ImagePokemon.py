pokemon_name = "Ivysaur"
##import requests
##link = "http://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png"
##response = requests.get(link)
##if response.status_code == 200:
##    f = open("sample.jpg", 'wb')
##    f.write(response.content)
##    f.close()

import requests
import os
class ImagePokemon:
    def __init__(self,name,url):
        if not os.path.exists('images'):
            os.makedirs('images')
        self.name = name
        self.url = url
        response = requests.get(url)
        if response.status_code == 200:
            f = open("images/"+self.name+".png", 'wb')
            f.write(response.content)
            f.close()
        


ivy = ImagePokemon("Ivysaur","http://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png")

        
