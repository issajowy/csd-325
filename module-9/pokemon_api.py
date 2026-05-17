import requests

url = "https://pokeapi.co/api/v2/generation/1/"
response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    species = data["pokemon_species"]

    # Extract (dex_number, name) pairs
    pokemon = []
    for p in species:
        # URL looks like: https://pokeapi.co/api/v2/pokemon-species/25/
        dex_number = int(p["url"].rstrip("/").split("/")[-1])
        pokemon.append((dex_number, p["name"]))

    # Sort by Pokédex number
    pokemon.sort(key=lambda x: x[0])

    print("Gen 1 Pokémon in Pokédex Order:")
    for dex, name in pokemon:
        print(f"{dex}: {name}")

else:
    print("Failed to retrieve data.")

