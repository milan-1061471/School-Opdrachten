# Opdracht 1
populaire_games = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018", "Fortnite Battle Royale 39 Million 2017", "Apex Legends 50 Million (1 Month) 2019", "Leauge of Legends (LOL) 27 Million 2009", "Counter Strike; Global Offensive 32 Million 2014", "Heartstone 29 Million 20120", "Minecraft 91 Million 2011", "DOTA 2 5 million 2015", "The Division 2 N/A 2019", "The Splatoon 2"]

print(f"5] {populaire_games[4]}")

lengte_game = populaire_games[7]
characters_in_name = len[lengte_game]
print(f"De game DOTA heeft {characters_in_name} characters")

number_of_games = len(populaire_games)
print(f"Er zitten {number_of_games} games in de lijst.")

populaire_games.insert(1, "Snake")
print(populaire_games)

index_of_splatoon = populaire_games.index("The Splatoon 2")
splatoon = populaire_games.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}.")

index_of_heartstone = populaire_games.index("Heartstone 29 Million 20120")
populaire_games[index_of_heartstone] = "Heartstone 29 Million 2012"
print(populaire_games)

# Opdracht 2
computers = ("Apple", "Asus", "Dell", "Lenovo", "Acer", "Samsung", "MSI", "Hewlett-Packard (HP)", "Toshiba", "Microsoft", "Chuwi", "Sony")

aantal_computers = len(computers)
print(f"De tuple bevat {aantal_computers} computer leveranciers.")

computer = computers[7]
characters_in_name = len(computer)
print(f"De naam van {computer} bestaat uit {characters_in_name} karakters.")

print(f"10] {computers[9]}")

# Opdracht 3
telefoon_nummers = {"The Simpsons": "636-555-3226", "Vegas Vacation": "555-0100", "Ghostbusters": "555-23678", "Billy Madison": "555-0840",  "Swingers": "213-555-4679", "Bruce Almighty": "555-0123", "Seinfeld": "555-FILK", "Arrested Development": "555-0113", "Die Hard With a Vengeance": "555-0001", "The A-Team": "555-6162"}

print(f"Het telefoonnummer van Bruce Almighty is {telefoon_nummers['Bruce Almighty']}.")
print(telefoon_nummers)

telefoon_nummers["Harry Potter"] = "605-475-6961"
print(telefoon_nummers)

oud_nummer = telefoon_nummers["Ghostbusters"]
nieuw_nummer = "555-2368"
telefoon_nummers["Ghostbusters"] = nieuw_nummer
print(f"Het telefoonnummr {oud_nummer} van de Ghostbusters is gewijzigd naar {nieuw_nummer}.")

telefoon_nummers = telefoon_nummers.pop("Seinfeld")
print(f"Telefoonnummer {telefoon_nummers} van Sienfeld is verwijderd.")

hoeveelheid_telefoon_nummers = len(telefoon_nummers)
print(f"In de dictionary zitten {hoeveelheid_telefoon_nummers} telefoonnummers.")