import requests
import random

pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar"]

pokemon_name = random.choice(pokemon_list)

try:
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    name = data["name"]
    height = data["height"] 
    weight = data["weight"] 

    print(" WHO'S THAT POKEMON? ")
    print(f"Choices:", ", ".join(pokemon_list))
    print(f"Height:", height)
    print(f"Weight:", weight)

    for attempt in range(3):
        guess = input("Guess the Pokemon: ").strip().lower()

        if guess not in pokemon_list:
            print("Pokemon is not in the list!")
        elif guess == name:
            print("Correct! You guessed the Pokemon!")
            break
        else:
            print("Wrong guess! Try again.")

    else:
        print(f"Game over! The Pokemon was", name)

except requests.exceptions.RequestException:
    print("Error! Please check your internet connection.")

