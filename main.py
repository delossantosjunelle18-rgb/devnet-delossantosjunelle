import requests
import random
pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/charmeleon")
poke_name= [{pokemon1.cotent}, {pokemon2.content}, {pokemon3.content}]

random.shuffle(poke_name)
random_pokemon = list[:1]

print(pokemon1)
 
# def get_random_pokemon():
#     random_pokemon = random.choice(poke_name)
 
 
# response = requests.get(f"{url}/"{random_pokemon}")
#                        return response.json()
                        
#                     print()