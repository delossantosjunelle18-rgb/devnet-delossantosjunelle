
import requests
import random

# List of at least five Pokemon
pokemon_list = [
    "pikachu",
    "charizard",
    "bulbasaur",
    "squirtle",
    "gengar"
]

# Function to get Pokemon data from PokeAPI
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url, timeout=10)

    # Check if the request was successful
    response.raise_for_status()

    # Convert the response into Python data
    data = response.json()

    # Extract the required information
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }


def main():
    try:
        # Randomly select a Pokemon
        selected = random.choice(pokemon_list)

        # Retrieve its information from the API
        pokemon = get_pokemon(selected)

        print("=== WHO'S THAT POKEMON? ===")
        print("Guess the Pokemon using its measurements!")
        print(f"Height: {pokemon['height'] / 10} meters")
        print(f"Weight: {pokemon['weight'] / 10} kilograms")

        # Give the player three attempts
        for attempt in range(1, 4):
            guess = input(
                f"Attempt {attempt}/3 - Your guess: "
            ).strip().lower()

            if guess not in pokemon_list:
                print("That Pokemon is not in the list.")
                continue

            if guess == pokemon["name"]:
                print("Correct! You guessed the Pokemon!")
                break
            else:
                print("Wrong guess. Try again!")

        else:
            print(f"Game over! The Pokemon was {pokemon['name']}.")

    except requests.exceptions.RequestException:
        print("Network error or Pokemon data could not be retrieved.")


if __name__ == "__main__":
    main()
