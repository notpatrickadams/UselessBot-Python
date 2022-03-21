import requests, random
from string import capwords

def get_pokemon():
    pkmn_list = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10000").json()["results"]
    rand_pkmn = random.randint(0, pkmn_list.index(pkmn_list[-1]))
    chosen_pkmn = requests.get(pkmn_list[rand_pkmn]["url"]).json()
    species_info = requests.get(chosen_pkmn["species"]["url"]).json()
    
    # Loops through genus list by language
    for entry in species_info["genera"]:
        if entry["language"]["name"] == "en":
            genus = entry["genus"]

    for entry in species_info["flavor_text_entries"]:
        if entry["language"]["name"] == "en":
            flavor_text = entry["flavor_text"]

    pkmn_types = []
    for t in chosen_pkmn["types"]:
        pkmn_types.append(capwords(t["type"]["name"]))

    name = capwords(chosen_pkmn["name"])

    # Chance for shiny
    if random.randint(1, 128) == 1:
        icon = chosen_pkmn["sprites"]["other"]["home"]["front_shiny"]
        name += " ✨"
    else:
        icon = chosen_pkmn["sprites"]["other"]["home"]["front_default"]
    
    # If there is no icon, generate a new Pokemon
    if icon == None:
        return get_pokemon()

    return {
        "name": name,
        "icon": icon,
        "types": pkmn_types,
        "dex_no": species_info["pokedex_numbers"][0]["entry_number"],
        "genus": genus,
        "flavor_text": flavor_text
    }