from ListPokemon import ListPokemon
from SinglePokemon import Pokemon
from JsonPokemon import JsonPokemon
from ImagePokemon import ImagePokemon
from time import sleep
from tqdm import tqdm

generation = int(input ("please, input the generation:"))
listpokemon = ListPokemon(generation) #khoi tao list ten pokemon
listpokemonname= listpokemon.craw() #tra ve du lieu
data = []

for i in tqdm(range(len(listpokemonname))):
    sleep(0.01)
    pokemon = Pokemon(listpokemonname[i],generation)
    x = {'name':pokemon.name, 'id':pokemon.id, 'color':pokemon.color,'img':pokemon.name+'.png', 'gen':pokemon.generation}
    data.append(x)
    createImage = ImagePokemon(pokemon.name,pokemon.image)
##for name in listpokemonname:
##    pokemon = Pokemon(name,generation)
##    x = {'name':pokemon.name, 'id':pokemon.id, 'color':pokemon.color,'img':pokemon.name+'.png', 'gen':pokemon.generation}
##    data.append(x)
##    createImage = ImagePokemon(pokemon.name,pokemon.image)
#deployer to Json file
lauch = JsonPokemon(data,generation)
print("craw completed")
