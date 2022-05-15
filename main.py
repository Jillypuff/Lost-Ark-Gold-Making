import json

data = open('mats.json', )
data = json.load(data)

wild_flower = data['Wild Flower'] / 100
shy_wild_flower = data['Shy Wild Flower'] / 10
bright_wild_flower = data['Bright Wild Flower'] / 10
crude_mushroom = data['Crude Mushroom'] / 100
fresh_mushroom = data['Fresh Mushroom'] / 10
exquisite_mushroom = data['Exquisite Mushroom'] / 10
timber = data['Timber'] / 100
tender_timber = data['Tender Timber'] / 10
sturdy_timber = data['Sturdy Timber'] / 10
iron_ore = data['Iron Ore'] / 100
heavy_iron_ore = data['Heavy Iron Ore'] / 10
strong_iron_ore = data['Strong Iron Ore'] / 10
thick_raw_meat = data['Thick Raw Meat'] / 100
tough_leather = data['Tough Leather'] / 10
treated_meat = data['Treated Meat'] / 10
caldarr_thick_raw_meat = data['Caldarr Thick Raw Meat'] / 10
oreha_thick_meat = data['Oreha Thick Meat'] / 10
hunting_crystal = data['Hunting Crystal'] / 10
fish = data['Fish'] / 100
redflesh_fish = data['Redflesh Fish'] / 10
natural_pearl = data['Natural Pearl'] / 10
caldarr_solar_carp = data['Caldarr Solar Carp'] / 10
oreha_solar_carp = data['Oreha Solar Carp'] / 10
fishing_crystal = data['Fishing Crystal'] / 10
ancient_relic = data['Ancient Relic'] / 100
rare_relic = data['Rare Relic'] / 10
caldarr_relic = data['Caldarr Relic'] / 10
oreha_relic = data['Oreha Relic'] / 10
excavating_crystal = data['Excavating Crystal'] / 10

print('Heavy Iron Ore -> Iron Ore: ', iron_ore * 50 - heavy_iron_ore * 25)
print('Strong Iron Ore -> Iron Ore: ', iron_ore * 50 - strong_iron_ore * 5)
print('Tender Timber -> Timber: ', timber * 50 - tender_timber * 25)
print('Sturdy Timber -> Timber: ', timber * 50 - sturdy_timber * 5, '\n')

if iron_ore * 50 - heavy_iron_ore * 25 == iron_ore * 50 - strong_iron_ore * 5 and iron_ore * 50 - heavy_iron_ore > 0:
    print(
        f'Trading Heavy Iron Ore for {heavy_iron_ore * 10} or Strong Iron Ore for {strong_iron_ore * 10} is equally '
        f'worth.')
    iron_ore = heavy_iron_ore * 2
elif iron_ore * 50 - heavy_iron_ore * 25 > 0 or iron_ore * 50 - strong_iron_ore * 5 > 0:
    if iron_ore * 50 - heavy_iron_ore * 25 > iron_ore * 50 - strong_iron_ore * 5:
        iron_ore = heavy_iron_ore * 2
        print(f'Trade Heavy Iron Ore for {heavy_iron_ore * 10} to Iron Ores.')
    else:
        iron_ore = strong_iron_ore * 10
        print(f'Trade Strong Iron Ore for {strong_iron_ore * 10} to Iron Ores. ')

if timber * 50 - tender_timber * 25 == timber * 50 - sturdy_timber * 5 and timber * 50 - tender_timber > 0:
    print(f'Trading Tender Timber for {tender_timber * 10} or Sturdy Timber {sturdy_timber * 10} is equally worth.')
    timber = tender_timber * 2
elif timber * 50 - tender_timber * 25 > 0 or timber * 50 - sturdy_timber * 5 > 0:
    if timber * 50 - tender_timber * 25 > timber * 50 - sturdy_timber * 5:
        timber = tender_timber * 2
        print(f'Trade Tender Timber for {tender_timber * 10} to Timber')
    else:
        timber = sturdy_timber * 10
        print(f'Trade Study Timber for {sturdy_timber * 10} to Timber')

# POWDERS
# GATHERING POWDER
if wild_flower * 100 < shy_wild_flower * 50 and wild_flower * 100 < crude_mushroom * 100 and wild_flower * 100 < \
        fresh_mushroom * 50:
    gathering_powder = ['Wild Flower', wild_flower * 1.25]
elif shy_wild_flower * 50 < crude_mushroom * 100 and shy_wild_flower * 50 < fresh_mushroom * 50:
    gathering_powder = ['Shy Wild Flower', shy_wild_flower * 0.625]
elif crude_mushroom * 100 < fresh_mushroom * 50:
    gathering_powder = ['Crude Mushroom', crude_mushroom * 1.25]
else:
    gathering_powder = ['Fresh Mushroom', fresh_mushroom * 0.625]

# Logging Powder
if timber * 100 < tender_timber:
    logging_powder = ['Timber', timber * 1.25]
else:
    logging_powder = ['Tender Timber', tender_timber * 0.625]

# MINING POWDER
if iron_ore * 100 < heavy_iron_ore * 50:
    mining_powder = ['Iron Ore', iron_ore * 1.25]
else:
    mining_powder = ['Heavy Iron Ore', heavy_iron_ore * 0.625]

# HUNTING POWDER
if thick_raw_meat * 100 < treated_meat * 50 and thick_raw_meat * 100 < tough_leather * 50:
    hunting_powder = ['Thick Raw Meat', thick_raw_meat * 1.25]
elif treated_meat * 50 < tough_leather * 50:
    hunting_powder = ['Treated Meat', treated_meat * 0.625]
else:
    hunting_powder = ['Tough Leather', tough_leather * 0.625]

# FISHING POWDER
if fish * 100 < redflesh_fish * 50 and fish * 100 < natural_pearl * 50:
    fishing_powder = ['Fish', fish * 1.25]
elif redflesh_fish * 50 < natural_pearl * 50:
    fishing_powder = ['Redflesh Fish', redflesh_fish * 0.625]
else:
    fishing_powder = ['Natural Pearl', natural_pearl * 0.625]

# EXCAVATING POWDER

if ancient_relic * 100 < rare_relic * 50:
    excavating_powder = ['Ancient Relic', ancient_relic * 1.25]
else:
    excavating_powder = ['Rare Relic', rare_relic * 0.625]
# EXCHANGE RATES
# GATHERING EXCHANGE
if gathering_powder[1] * 100 < shy_wild_flower * 50:
    print(f'- Shy Wild Flower: AH {shy_wild_flower} - Exchange {gathering_powder[1] * 2}')
    shy_wild_flower = gathering_powder[1] * 2
if gathering_powder[1] * 100 < bright_wild_flower * 10:
    print(f'- Bright Wild Flower: AH {bright_wild_flower} - Exchange {gathering_powder[1] * 10}')
    bright_wild_flower = gathering_powder[1] * 10
if gathering_powder[1] * 100 < fresh_mushroom * 50:
    print(f'- Fresh Mushroom: AH {fresh_mushroom} - Exchange {gathering_powder[1] * 2}')
    fresh_mushroom = gathering_powder[1] * 2
if gathering_powder[1] * 100 < exquisite_mushroom * 10:
    print(f'- Exquisite Mushroom: AH {exquisite_mushroom} - Exchange {gathering_powder[1] * 10}')
    exquisite_mushroom = gathering_powder[1] * 10

# LOGGING EXCHANGE
if logging_powder[1] * 100 < tender_timber * 50:
    print(f'- Tender Timber: AH {tender_timber} - Exchange {logging_powder[1] * 2}')
    tender_timber = logging_powder[1] * 2
if logging_powder[1] * 100 < sturdy_timber * 10:
    print(f'- Sturdy Timber: AH {sturdy_timber} - Exchange {logging_powder[1] * 10}')
    sturdy_timber = logging_powder[1] * 10

# MINING EXCHANGE
if mining_powder[1] * 100 < heavy_iron_ore * 50:
    print(f'- Heavy Iron Ore: AH {heavy_iron_ore} - Exchange {mining_powder[1] * 2}')
    heavy_iron_ore = mining_powder[1] * 2
if mining_powder[1] * 100 < strong_iron_ore * 10:
    print(f'- Strong Iron Ore: AH {strong_iron_ore} - Exchange {mining_powder[1] * 10}')
    strong_iron_ore = mining_powder[1] * 10

# HUNTING EXCHANGE
if hunting_powder[1] * 100 < treated_meat * 50:
    print(f'- Treated Meat: AH {treated_meat} - Exchange {hunting_powder[1] * 2}')
    treated_meat = hunting_powder[1] * 2
if hunting_powder[1] * 100 < tough_leather * 50:
    print(f'- Tough Leather: AH {tough_leather} - Exchange {tough_leather[1] * 2}')
    tough_leather = hunting_powder[1] * 2
if hunting_powder[1] * 100 < caldarr_thick_raw_meat * 10:
    print(f'- Caldarr Thick Raw Meat: AH {caldarr_thick_raw_meat} - Exchange {hunting_powder[1] * 10}')
    caldarr_thick_raw_meat = hunting_powder[1] * 10
if hunting_powder[1] * 100 < oreha_thick_meat * 10:
    print(f'- Oreha Thick Meat: AH {oreha_thick_meat} - Exchange {hunting_powder[1] * 10}')
    oreha_thick_meat = hunting_powder[1] * 10

# FISHING EXCHANGE
if fishing_powder[1] * 100 < redflesh_fish * 50:
    print(f'- Redflesh Fish: AH {redflesh_fish} - Exchange {fishing_powder[1] * 2}')
    redflesh_fish = fishing_powder[1] * 2
if fishing_powder[1] * 100 < natural_pearl * 50:
    print(f'- Natural Pearl: AH {natural_pearl} - Exchange {fishing_powder[1] * 2}')
    natural_pearl = fishing_powder[1] * 2
if fishing_powder[1] * 100 < caldarr_solar_carp * 10:
    print(f'- Caldarr Solar Carp: AH {caldarr_solar_carp} - Exchange {fishing_powder[1] * 10}')
    caldarr_solar_carp = fishing_powder[1] * 10
if fishing_powder[1] * 100 < oreha_solar_carp * 10:
    print(f'- Oreha Solar Carp: AH {oreha_solar_carp} Exchange {fishing_powder[1] * 10}')
    oreha_solar_carp = fishing_powder[1] * 10

# EXCAVATING EXCHANGE
if excavating_powder[1] * 100 < rare_relic * 50:
    print(f'- Rare Relic: AH {rare_relic} - Exchange {excavating_powder[1] * 2}')
    rare_relic = excavating_powder[1] * 2
if excavating_powder[1] * 100 < caldarr_relic * 10:
    print(f'- Caldarr Relic: AH {caldarr_relic} - Exchange {excavating_powder[1] * 10}')
    caldarr_relic = excavating_powder[1] * 10
if excavating_powder[1] * 100 < oreha_relic * 10:
    print(f'- Oreha Relic: AH {oreha_relic} - Exchange {excavating_powder[1] * 10}')
    oreha_relic = excavating_powder[1] * 10

# CHEAPEST POWDER
print(f'Cheapest Gathering Powder is {gathering_powder[0]} and costs {gathering_powder[1]} gold each.')
print(f'Cheapest Logging Powder is {logging_powder[0]} and costs {logging_powder[1]} gold each.')
print(f'Cheapest Mining Powder is {mining_powder[0]} and costs {mining_powder[1]} gold each.')
print(f'Cheapest Hunting Powder is {hunting_powder[0]} and costs {hunting_powder[1]} gold each.')
print(f'Cheapest Fishing Powder is {fishing_powder[0]} and costs {fishing_powder[1]} gold each.')
print(f'Cheapest Excavating Powder is {excavating_powder[0]} and costs {excavating_powder[1]} gold each.')

print('Flare:',
      (natural_pearl * 20 + wild_flower * 35) / 3)
print('Splendid Flare:',
      (natural_pearl * 20 + wild_flower * 35 + shy_wild_flower * 20 + 4) / 2)
print('Panacea:',
      (exquisite_mushroom * 4 + fresh_mushroom * 16 + rare_relic * 5 + crude_mushroom * 22 + 14) / 3)
print('Whirlwind Grenade:',
      (exquisite_mushroom * 3 + fresh_mushroom * 12 + tender_timber * 3 + crude_mushroom * 24 + 14) / 3)
print('HP Potion:',
      (shy_wild_flower * 5 + wild_flower * 10) / 3)
print('Elemental HP Potion:',
      (bright_wild_flower * 6 + shy_wild_flower * 24 + wild_flower * 48 + 29) / 3)
print('Awakening Potion:',
      (exquisite_mushroom * 5 + fresh_mushroom * 20 +
       sturdy_timber * 2 + rare_relic * 4 + crude_mushroom * 40 + 29) / 3)
print('Caldarr Fusion Material (Hunting):',
      (caldarr_thick_raw_meat * 9 + tough_leather * 36 + thick_raw_meat * 72 + 78) / 30)
print('Caldarr Fusion Material (Excavating):',
      (caldarr_relic * 7 + rare_relic * 28 + ancient_relic * 56 + 78) / 30)
print('Caldarr Fusion Material (Fishing):',
      (caldarr_solar_carp * 9 + natural_pearl * 36 + fish * 72 + 78) / 30)
print('Simple Oreha Fusion Material (Hunting):',
      (oreha_thick_meat * 9 + tough_leather * 36 + thick_raw_meat * 72 + 196) / 30)
print('Simple Oreha Fusion Material (Excavating):',
      (oreha_relic * 7 + rare_relic * 28 + ancient_relic * 56 + 196) / 30)
print('Simple Oreha Fusion Material (Fishing):',
      (oreha_solar_carp * 9 + natural_pearl * 36 + fish * 72 + 196) / 30)
print('Basic Oreha Fusion Material (Hunting):',
      (oreha_thick_meat * 10 + tough_leather * 40 + thick_raw_meat * 80 + 200)/30)
print('Basic Oreha Fusion Material (Excavating):',
      (oreha_relic * 8 + rare_relic * 26 + ancient_relic * 64 + 200)/30)
print('Basic Oreha Fusion Material (Fishing):',
      (oreha_solar_carp * 10 + natural_pearl * 40 + fish * 80 + 200)/30)
print('Punika Archaeological Site Map:',
      (oreha_relic * 39 + rare_relic * 195 + 39))
print('Uncommon Ship Parts Material:',
      (strong_iron_ore * 3 + sturdy_timber * 3 + heavy_iron_ore * 8 + tender_timber * 8 + 20) / 15)
print('Tool Crafting Part:',
      (strong_iron_ore * 22 + sturdy_timber * 22 + heavy_iron_ore * 88 + tender_timber * 88 + 19) / 30)
