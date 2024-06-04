
#!pip install pytelegrambotapi
#!pip install transformers
#!pip install requests

import telebot
import requests
import re
from transformers import pipeline

# This is cursed sorry.
allPokemons = [
	"Bulbasaur",
	"Ivysaur",
	"Venusaur",
	"Charmander",
	"Charmeleon",
	"Charizard",
	"Squirtle",
	"Wartortle",
	"Blastoise",
	"Caterpie",
	"Metapod",
	"Butterfree",
	"Weedle",
	"Kakuna",
	"Beedrill",
	"Pidgey",
	"Pidgeotto",
	"Pidgeot",
	"Rattata",
	"Raticate",
	"Spearow",
	"Fearow",
	"Ekans",
	"Arbok",
	"Pikachu",
	"Raichu",
	"Sandshrew",
	"Sandslash",
	"Nidoran♀",
	"Nidorina",
	"Nidoqueen",
	"Nidoran♂",
	"Nidorino",
	"Nidoking",
	"Clefairy",
	"Clefable",
	"Vulpix",
	"Ninetales",
	"Jigglypuff",
	"Wigglytuff",
	"Zubat",
	"Golbat",
	"Oddish",
	"Gloom",
	"Vileplume",
	"Paras",
	"Parasect",
	"Venonat",
	"Venomoth",
	"Diglett",
	"Dugtrio",
	"Meowth",
	"Persian",
	"Psyduck",
	"Golduck",
	"Mankey",
	"Primeape",
	"Growlithe",
	"Arcanine",
	"Poliwag",
	"Poliwhirl",
	"Poliwrath",
	"Abra",
	"Kadabra",
	"Alakazam",
	"Machop",
	"Machoke",
	"Machamp",
	"Bellsprout",
	"Weepinbell",
	"Victreebel",
	"Tentacool",
	"Tentacruel",
	"Geodude",
	"Graveler",
	"Golem",
	"Ponyta",
	"Rapidash",
	"Slowpoke",
	"Slowbro",
	"Magnemite",
	"Magneton",
	"Farfetch'd",
	"Doduo",
	"Dodrio",
	"Seel",
	"Dewgong",
	"Grimer",
	"Muk",
	"Shellder",
	"Cloyster",
	"Gastly",
	"Haunter",
	"Gengar",
	"Onix",
	"Drowzee",
	"Hypno",
	"Krabby",
	"Kingler",
	"Voltorb",
	"Electrode",
	"Exeggcute",
	"Exeggutor",
	"Cubone",
	"Marowak",
	"Hitmonlee",
	"Hitmonchan",
	"Lickitung",
	"Koffing",
	"Weezing",
	"Rhyhorn",
	"Rhydon",
	"Chansey",
	"Tangela",
	"Kangaskhan",
	"Horsea",
	"Seadra",
	"Goldeen",
	"Seaking",
	"Staryu",
	"Starmie",
	"Mr. Mime",
	"Scyther",
	"Jynx",
	"Electabuzz",
	"Magmar",
	"Pinsir",
	"Tauros",
	"Magikarp",
	"Gyarados",
	"Lapras",
	"Ditto",
	"Eevee",
	"Vaporeon",
	"Jolteon",
	"Flareon",
	"Porygon",
	"Omanyte",
	"Omastar",
	"Kabuto",
	"Kabutops",
	"Aerodactyl",
	"Snorlax",
	"Articuno",
	"Zapdos",
	"Moltres",
	"Dratini",
	"Dragonair",
	"Dragonite",
	"Mewtwo",
	"Mew",
	"Chikorita",
	"Bayleef",
	"Meganium",
	"Cyndaquil",
	"Quilava",
	"Typhlosion",
	"Totodile",
	"Croconaw",
	"Feraligatr",
	"Sentret",
	"Furret",
	"Hoothoot",
	"Noctowl",
	"Ledyba",
	"Ledian",
	"Spinarak",
	"Ariados",
	"Crobat",
	"Chinchou",
	"Lanturn",
	"Pichu",
	"Cleffa",
	"Igglybuff",
	"Togepi",
	"Togetic",
	"Natu",
	"Xatu",
	"Mareep",
	"Flaaffy",
	"Ampharos",
	"Bellossom",
	"Marill",
	"Azumarill",
	"Sudowoodo",
	"Politoed",
	"Hoppip",
	"Skiploom",
	"Jumpluff",
	"Aipom",
	"Sunkern",
	"Sunflora",
	"Yanma",
	"Wooper",
	"Quagsire",
	"Espeon",
	"Umbreon",
	"Murkrow",
	"Slowking",
	"Misdreavus",
	"Unown",
	"Wobbuffet",
	"Girafarig",
	"Pineco",
	"Forretress",
	"Dunsparce",
	"Gligar",
	"Steelix",
	"Snubbull",
	"Granbull",
	"Qwilfish",
	"Scizor",
	"Shuckle",
	"Heracross",
	"Sneasel",
	"Teddiursa",
	"Ursaring",
	"Slugma",
	"Magcargo",
	"Swinub",
	"Piloswine",
	"Corsola",
	"Remoraid",
	"Octillery",
	"Delibird",
	"Mantine",
	"Skarmory",
	"Houndour",
	"Houndoom",
	"Kingdra",
	"Phanpy",
	"Donphan",
	"Porygon2",
	"Stantler",
	"Smeargle",
	"Tyrogue",
	"Hitmontop",
	"Smoochum",
	"Elekid",
	"Magby",
	"Miltank",
	"Blissey",
	"Raikou",
	"Entei",
	"Suicune",
	"Larvitar",
	"Pupitar",
	"Tyranitar",
	"Lugia",
	"Ho-Oh",
	"Celebi",
	"Treecko",
	"Grovyle",
	"Sceptile",
	"Torchic",
	"Combusken",
	"Blaziken",
	"Mudkip",
	"Marshtomp",
	"Swampert",
	"Poochyena",
	"Mightyena",
	"Zigzagoon",
	"Linoone",
	"Wurmple",
	"Silcoon",
	"Beautifly",
	"Cascoon",
	"Dustox",
	"Lotad",
	"Lombre",
	"Ludicolo",
	"Seedot",
	"Nuzleaf",
	"Shiftry",
	"Taillow",
	"Swellow",
	"Wingull",
	"Pelipper",
	"Ralts",
	"Kirlia",
	"Gardevoir",
	"Surskit",
	"Masquerain",
	"Shroomish",
	"Breloom",
	"Slakoth",
	"Vigoroth",
	"Slaking",
	"Nincada",
	"Ninjask",
	"Shedinja",
	"Whismur",
	"Loudred",
	"Exploud",
	"Makuhita",
	"Hariyama",
	"Azurill",
	"Nosepass",
	"Skitty",
	"Delcatty",
	"Sableye",
	"Mawile",
	"Aron",
	"Lairon",
	"Aggron",
	"Meditite",
	"Medicham",
	"Electrike",
	"Manectric",
	"Plusle",
	"Minun",
	"Volbeat",
	"Illumise",
	"Roselia",
	"Gulpin",
	"Swalot",
	"Carvanha",
	"Sharpedo",
	"Wailmer",
	"Wailord",
	"Numel",
	"Camerupt",
	"Torkoal",
	"Spoink",
	"Grumpig",
	"Spinda",
	"Trapinch",
	"Vibrava",
	"Flygon",
	"Cacnea",
	"Cacturne",
	"Swablu",
	"Altaria",
	"Zangoose",
	"Seviper",
	"Lunatone",
	"Solrock",
	"Barboach",
	"Whiscash",
	"Corphish",
	"Crawdaunt",
	"Baltoy",
	"Claydol",
	"Lileep",
	"Cradily",
	"Anorith",
	"Armaldo",
	"Feebas",
	"Milotic",
	"Castform",
	"Kecleon",
	"Shuppet",
	"Banette",
	"Duskull",
	"Dusclops",
	"Tropius",
	"Chimecho",
	"Absol",
	"Wynaut",
	"Snorunt",
	"Glalie",
	"Spheal",
	"Sealeo",
	"Walrein",
	"Clamperl",
	"Huntail",
	"Gorebyss",
	"Relicanth",
	"Luvdisc",
	"Bagon",
	"Shelgon",
	"Salamence",
	"Beldum",
	"Metang",
	"Metagross",
	"Regirock",
	"Regice",
	"Registeel",
	"Latias",
	"Latios",
	"Kyogre",
	"Groudon",
	"Rayquaza",
	"Jirachi",
	"Deoxys",
	"Turtwig",
	"Grotle",
	"Torterra",
	"Chimchar",
	"Monferno",
	"Infernape",
	"Piplup",
	"Prinplup",
	"Empoleon",
	"Starly",
	"Staravia",
	"Staraptor",
	"Bidoof",
	"Bibarel",
	"Kricketot",
	"Kricketune",
	"Shinx",
	"Luxio",
	"Luxray",
	"Budew",
	"Roserade",
	"Cranidos",
	"Rampardos",
	"Shieldon",
	"Bastiodon",
	"Burmy",
	"Wormadam",
	"Mothim",
	"Combee",
	"Vespiquen",
	"Pachirisu",
	"Buizel",
	"Floatzel",
	"Cherubi",
	"Cherrim",
	"Shellos",
	"Gastrodon",
	"Ambipom",
	"Drifloon",
	"Drifblim",
	"Buneary",
	"Lopunny",
	"Mismagius",
	"Honchkrow",
	"Glameow",
	"Purugly",
	"Chingling",
	"Stunky",
	"Skuntank",
	"Bronzor",
	"Bronzong",
	"Bonsly",
	"Mime Jr.",
	"Happiny",
	"Chatot",
	"Spiritomb",
	"Gible",
	"Gabite",
	"Garchomp",
	"Munchlax",
	"Riolu",
	"Lucario",
	"Hippopotas",
	"Hippowdon",
	"Skorupi",
	"Drapion",
	"Croagunk",
	"Toxicroak",
	"Carnivine",
	"Finneon",
	"Lumineon",
	"Mantyke",
	"Snover",
	"Abomasnow",
	"Weavile",
	"Magnezone",
	"Lickilicky",
	"Rhyperior",
	"Tangrowth",
	"Electivire",
	"Magmortar",
	"Togekiss",
	"Yanmega",
	"Leafeon",
	"Glaceon",
	"Gliscor",
	"Mamoswine",
	"Porygon-Z",
	"Gallade",
	"Probopass",
	"Dusknoir",
	"Froslass",
	"Rotom",
	"Uxie",
	"Mesprit",
	"Azelf",
	"Dialga",
	"Palkia",
	"Heatran",
	"Regigigas",
	"Giratina",
	"Cresselia",
	"Phione",
	"Manaphy",
	"Darkrai",
	"Shaymin",
	"Arceus",
	"Victini",
	"Snivy",
	"Servine",
	"Serperior",
	"Tepig",
	"Pignite",
	"Emboar",
	"Oshawott",
	"Dewott",
	"Samurott",
	"Patrat",
	"Watchog",
	"Lillipup",
	"Herdier",
	"Stoutland",
	"Purrloin",
	"Liepard",
	"Pansage",
	"Simisage",
	"Pansear",
	"Simisear",
	"Panpour",
	"Simipour",
	"Munna",
	"Musharna",
	"Pidove",
	"Tranquill",
	"Unfezant",
	"Blitzle",
	"Zebstrika",
	"Roggenrola",
	"Boldore",
	"Gigalith",
	"Woobat",
	"Swoobat",
	"Drilbur",
	"Excadrill",
	"Audino",
	"Timburr",
	"Gurdurr",
	"Conkeldurr",
	"Tympole",
	"Palpitoad",
	"Seismitoad",
	"Throh",
	"Sawk",
	"Sewaddle",
	"Swadloon",
	"Leavanny",
	"Venipede",
	"Whirlipede",
	"Scolipede",
	"Cottonee",
	"Whimsicott",
	"Petilil",
	"Lilligant",
	"Basculin",
	"Sandile",
	"Krokorok",
	"Krookodile",
	"Darumaka",
	"Darmanitan",
	"Maractus",
	"Dwebble",
	"Crustle",
	"Scraggy",
	"Scrafty",
	"Sigilyph",
	"Yamask",
	"Cofagrigus",
	"Tirtouga",
	"Carracosta",
	"Archen",
	"Archeops",
	"Trubbish",
	"Garbodor",
	"Zorua",
	"Zoroark",
	"Minccino",
	"Cinccino",
	"Gothita",
	"Gothorita",
	"Gothitelle",
	"Solosis",
	"Duosion",
	"Reuniclus",
	"Ducklett",
	"Swanna",
	"Vanillite",
	"Vanillish",
	"Vanilluxe",
	"Deerling",
	"Sawsbuck",
	"Emolga",
	"Karrablast",
	"Escavalier",
	"Foongus",
	"Amoonguss",
	"Frillish",
	"Jellicent",
	"Alomomola",
	"Joltik",
	"Galvantula",
	"Ferroseed",
	"Ferrothorn",
	"Klink",
	"Klang",
	"Klinklang",
	"Tynamo",
	"Eelektrik",
	"Eelektross",
	"Elgyem",
	"Beheeyem",
	"Litwick",
	"Lampent",
	"Chandelure",
	"Axew",
	"Fraxure",
	"Haxorus",
	"Cubchoo",
	"Beartic",
	"Cryogonal",
	"Shelmet",
	"Accelgor",
	"Stunfisk",
	"Mienfoo",
	"Mienshao",
	"Druddigon",
	"Golett",
	"Golurk",
	"Pawniard",
	"Bisharp",
	"Bouffalant",
	"Rufflet",
	"Braviary",
	"Vullaby",
	"Mandibuzz",
	"Heatmor",
	"Durant",
	"Deino",
	"Zweilous",
	"Hydreigon",
	"Larvesta",
	"Volcarona",
	"Cobalion",
	"Terrakion",
	"Virizion",
	"Tornadus",
	"Thundurus",
	"Reshiram",
	"Zekrom",
	"Landorus",
	"Kyurem",
	"Keldeo",
	"Meloetta",
	"Genesect",
	"Chespin",
	"Quilladin",
	"Chesnaught",
	"Fennekin",
	"Braixen",
	"Delphox",
	"Froakie",
	"Frogadier",
	"Greninja",
	"Bunnelby",
	"Diggersby",
	"Fletchling",
	"Fletchinder",
	"Talonflame",
	"Scatterbug",
	"Spewpa",
	"Vivillon",
	"Litleo",
	"Pyroar",
	"Flabébé",
	"Floette",
	"Florges",
	"Skiddo",
	"Gogoat",
	"Pancham",
	"Pangoro",
	"Furfrou",
	"Espurr",
	"Meowstic",
	"Honedge",
	"Doublade",
	"Aegislash",
	"Spritzee",
	"Aromatisse",
	"Swirlix",
	"Slurpuff",
	"Inkay",
	"Malamar",
	"Binacle",
	"Barbaracle",
	"Skrelp",
	"Dragalge",
	"Clauncher",
	"Clawitzer",
	"Helioptile",
	"Heliolisk",
	"Tyrunt",
	"Tyrantrum",
	"Amaura",
	"Aurorus",
	"Sylveon",
	"Hawlucha",
	"Dedenne",
	"Carbink",
	"Goomy",
	"Sliggoo",
	"Goodra",
	"Klefki",
	"Phantump",
	"Trevenant",
	"Pumpkaboo",
	"Gourgeist",
	"Bergmite",
	"Avalugg",
	"Noibat",
	"Noivern",
	"Xerneas",
	"Yveltal",
	"Zygarde",
	"Diancie",
	"Hoopa",
	"Volcanion",
	"Rowlet",
	"Dartrix",
	"Decidueye",
	"Litten",
	"Torracat",
	"Incineroar",
	"Popplio",
	"Brionne",
	"Primarina",
	"Pikipek",
	"Trumbeak",
	"Toucannon",
	"Yungoos",
	"Gumshoos",
	"Grubbin",
	"Charjabug",
	"Vikavolt",
	"Crabrawler",
	"Crabominable",
	"Oricorio",
	"Cutiefly",
	"Ribombee",
	"Rockruff",
	"Lycanroc",
	"Wishiwashi",
	"Mareanie",
	"Toxapex",
	"Mudbray",
	"Mudsdale",
	"Dewpider",
	"Araquanid",
	"Fomantis",
	"Lurantis",
	"Morelull",
	"Shiinotic",
	"Salandit",
	"Salazzle",
	"Stufful",
	"Bewear",
	"Bounsweet",
	"Steenee",
	"Tsareena",
	"Comfey",
	"Oranguru",
	"Passimian",
	"Wimpod",
	"Golisopod",
	"Sandygast",
	"Palossand",
	"Pyukumuku",
	"Type: Null",
	"Silvally",
	"Minior",
	"Komala",
	"Turtonator",
	"Togedemaru",
	"Mimikyu",
	"Bruxish",
	"Drampa",
	"Dhelmise",
	"Jangmo-o",
	"Hakamo-o",
	"Kommo-o",
	"Tapu Koko",
	"Tapu Lele",
	"Tapu Bulu",
	"Tapu Fini",
	"Cosmog",
	"Cosmoem",
	"Solgaleo",
	"Lunala",
	"Nihilego",
	"Buzzwole",
	"Pheromosa",
	"Xurkitree",
	"Celesteela",
	"Kartana",
	"Guzzlord",
	"Necrozma",
	"Magearna",
	"Marshadow",
	"Poipole",
	"Naganadel",
	"Stakataka",
	"Blacephalon",
	"Zeraora",
	"Meltan",
	"Melmetal",
	"Grookey",
	"Thwackey",
	"Rillaboom",
	"Scorbunny",
	"Raboot",
	"Cinderace",
	"Sobble",
	"Drizzile",
	"Inteleon",
	"Skwovet",
	"Greedent",
	"Rookidee",
	"Corvisquire",
	"Corviknight",
	"Blipbug",
	"Dottler",
	"Orbeetle",
	"Nickit",
	"Thievul",
	"Gossifleur",
	"Eldegoss",
	"Wooloo",
	"Dubwool",
	"Chewtle",
	"Drednaw",
	"Yamper",
	"Boltund",
	"Rolycoly",
	"Carkol",
	"Coalossal",
	"Applin",
	"Flapple",
	"Appletun",
	"Silicobra",
	"Sandaconda",
	"Cramorant",
	"Arrokuda",
	"Barraskewda",
	"Toxel",
	"Toxtricity",
	"Sizzlipede",
	"Centiskorch",
	"Clobbopus",
	"Grapploct",
	"Sinistea",
	"Polteageist",
	"Hatenna",
	"Hattrem",
	"Hatterene",
	"Impidimp",
	"Morgrem",
	"Grimmsnarl",
	"Obstagoon",
	"Perrserker",
	"Cursola",
	"Sirfetch'd",
	"Mr. Rime",
	"Runerigus",
	"Milcery",
	"Alcremie",
	"Falinks",
	"Pincurchin",
	"Snom",
	"Frosmoth",
	"Stonjourner",
	"Eiscue",
	"Indeedee",
	"Morpeko",
	"Cufant",
	"Copperajah",
	"Dracozolt",
	"Arctozolt",
	"Dracovish",
	"Arctovish",
	"Duraludon",
	"Dreepy",
	"Drakloak",
	"Dragapult",
	"Zacian",
	"Zamazenta",
	"Eternatus",
	"Kubfu",
	"Urshifu",
	"Zarude",
	"Regieleki",
	"Regidrago",
	"Glastrier",
	"Spectrier",
	"Calyrex",
	"Wyrdeer",
	"Kleavor",
	"Ursaluna",
	"Basculegion",
	"Sneasler",
	"Overqwil",
	"Enamorus",
	"Sprigatito",
	"Floragato",
	"Meowscarada",
	"Fuecoco",
	"Crocalor",
	"Skeledirge",
	"Quaxly",
	"Quaxwell",
	"Quaquaval",
	"Lechonk",
	"Oinkologne",
	"Tarountula",
	"Spidops",
	"Nymble",
	"Lokix",
	"Pawmi",
	"Pawmo",
	"Pawmot",
	"Tandemaus",
	"Maushold",
	"Fidough",
	"Dachsbun",
	"Smoliv",
	"Dolliv",
	"Arboliva",
	"Squawkabilly",
	"Nacli",
	"Naclstack",
	"Garganacl",
	"Charcadet",
	"Armarouge",
	"Ceruledge",
	"Tadbulb",
	"Bellibolt",
	"Wattrel",
	"Kilowattrel",
	"Maschiff",
	"Mabosstiff",
	"Shroodle",
	"Grafaiai",
	"Bramblin",
	"Brambleghast",
	"Toedscool",
	"Toedscruel",
	"Klawf",
	"Capsakid",
	"Scovillain",
	"Rellor",
	"Rabsca",
	"Flittle",
	"Espathra",
	"Tinkatink",
	"Tinkatuff",
	"Tinkaton",
	"Wiglett",
	"Wugtrio",
	"Bombirdier",
	"Finizen",
	"Palafin",
	"Varoom",
	"Revavroom",
	"Cyclizar",
	"Orthworm",
	"Glimmet",
	"Glimmora",
	"Greavard",
	"Houndstone",
	"Flamigo",
	"Cetoddle",
	"Cetitan",
	"Veluza",
	"Dondozo",
	"Tatsugiri",
	"Annihilape",
	"Clodsire",
	"Farigiraf",
	"Dudunsparce",
	"Kingambit",
	"Great Tusk",
	"Scream Tail",
	"Brute Bonnet",
	"Flutter Mane",
	"Slither Wing",
	"Sandy Shocks",
	"Iron Treads",
	"Iron Bundle",
	"Iron Hands",
	"Iron Jugulis",
	"Iron Moth",
	"Iron Thorns",
	"Frigibax",
	"Arctibax",
	"Baxcalibur",
	"Gimmighoul",
	"Gholdengo",
	"Wo-Chien",
	"Chien-Pao",
	"Ting-Lu",
	"Chi-Yu",
	"Roaring Moon",
	"Iron Valiant",
	"Koraidon",
	"Miraidon",
	"Walking Wake",
	"Iron Leaves",
	"Dipplin",
	"Poltchageist",
	"Sinistcha",
	"Okidogi",
	"Mankidori",
	"Fezandipiti",
	"Ogerpon",
	"Archaludon",
	"Hydrapple",
	"Gouging Fire",
	"Raging Bolt",
	"Iron Boulder",
	"Iron Crown",
	"Terapagos",
	"Pecharunt"
]

def getPoke(poke):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
def getPokeHabitat(poke):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke}')
    if response.status_code == 200:
        return response.json().get('habitat').get('name')
    else:
        return None
def getPokeColor(poke):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke}')
    if response.status_code == 200:
        return response.json().get('color').get('name')
    else:
        return None


TOKEN = ''

bot = telebot.TeleBot(TOKEN)


classifier = pipeline("zero-shot-classification")
pr = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2", tokenizer="timpal0l/mdeberta-v3-base-squad2")

intentions = ["search for stats in a pokemon","search for pokemon abilities", "wants to know pokemon place of living", "wants to know pokemon color"]

state = 1

@bot.message_handler(func=lambda message: True)
def reply(message):
    global state
    global saved_info
    global allPokemons

    user_msg = message.text

    if (state == 1):
        bot.reply_to(message, "Hello i am a bot, i can help you with some information about Pokemons like stats, abilities, habitat and color just type in the name and what you want ")
        state = 2
    if (state == 2):
        reply = pr(context=user_msg, question=intent)

         intent = classifier(user_msg, intentions)["labels"][0]
         print(intent)
        if (intent == "search for stats in a pokemon"):
            words = (re.sub(r"'s", '', user_msg))
            print(words)
            words = (re.sub(r'[^A-Za-z0-9 ]+', '',words)).split()
            print(words)
            for word in words:
                if word.capitalize() in allPokemons:
                    poke_data = getPoke(word.lower())
                    stats = poke_data["stats"]
                    stat_string = f"Stats for {word.capitalize()}:\n"
                    for stat in stats:
                        stat_name = stat['stat']['name'].capitalize()
                        base_stat = stat['base_stat']
                        stat_string += f"{stat_name}: {base_stat}\n"
                    if poke_data is not None:
                        bot.reply_to(message, stat_string)
                        break
                    else:
                        bot.reply_to(message,"Sorry, i couldn't find that pokemon")
                else:
                  bot.reply_to(message,"Sorry, i couldn't find that pokemon")
        elif (intent == "wants to know pokemon color"): 
            words = (re.sub(r"'s", '', user_msg))
            print(words)
            words = (re.sub(r'[^A-Za-z0-9 ]+', '',words)).split()
            print(words)
            for word in words:
                if word.capitalize() in allPokemons:
                    poke_data = getPokeColor(word.lower())
                    if poke_data is not None:
                        bot.reply_to(message, f"The color of {word.capitalize()} is {poke_data.capitalize()}")
                        break
                    else:
                        bot.reply_to(message,"Sorry, i couldn't find that pokemon")
                else:
                  bot.reply_to(message,"Sorry, i couldn't find that pokemon")
        elif(intent == "search for pokemon abilities"):
            words = (re.sub(r"'s", '', user_msg))
            print(words)
            words = (re.sub(r'[^A-Za-z0-9 ]+', '',words)).split()
            print(words)
            for word in words:
              if word.capitalize() in allPokemons:
                poke_data = getPoke(word.lower())
                abilities = poke_data['abilities']
                abilities_string = f"Abilities for {word.capitalize()}:\n"
                for ability in abilities:
                    ability_name = ability['ability']['name'].capitalize()
                    abilities_string += f"{ability_name}\n"
                if poke_data is not None:
                  bot.reply_to(message, abilities_string)
              else:
                bot.reply_to(message,"Sorry, i couldn't find that pokemon")
        elif(intent == "wants to know pokemon place of living"):
            words = (re.sub(r"'s", '', user_msg))
            print(words)
            words = (re.sub(r'[^A-Za-z0-9 ]+', '',words)).split()
            print(words)
            for word in words:
                if word.capitalize() in allPokemons:
                    poke_data = getPokeHabitat(word.lower())
                    if poke_data is not None:
                        bot.reply_to(message, f"The habitat of {word.capitalize()} is {poke_data.capitalize()}")
                        break
                    else:
                        bot.reply_to(message,"Sorry, i couldn't find that pokemon")
                else:
                     bot.reply_to(message,"Sorry, i couldn't find that pokemon")
bot.polling()