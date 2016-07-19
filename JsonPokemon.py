##list = []
##for i in range(10):
##    x = {'numbers':i, 'strings':i+1, 'x':i+2, 'y':i+3}
##    list.append(x)
##
##data= list
##import json
##with open("pokemon.json", "w") as outfile:
##    json.dump(data, outfile, indent=4)

class JsonPokemon:
    def __init__(self,listdata,filename="default"):
        self.data = listdata
        self.filename = str(filename)
        import json
        with open('generation'+self.filename+'.json', "w") as outfile:
            json.dump(self.data, outfile, indent=4)
        
    
