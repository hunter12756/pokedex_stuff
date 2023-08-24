from app import app
from app.models import db, Pokemon, Item
from random import randint
#15 pokemon
with app.app_context():
  pokemons = [
    {
        'number': 1,
        'image_url': '/images/pokemon_snaps/1.svg',
        'name': 'Bulbasaur',
        'attack': 49,
        'defense': 49,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip'
        ],
        'captured': True
    },
    {
        'number': 2,
        'image_url': '/images/pokemon_snaps/2.svg',
        'name': 'Ivysaur',
        'attack': 62,
        'defense': 63,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        'captured': True
    },
    {
        'number': 3,
        'image_url': '/images/pokemon_snaps/3.svg',
        'name': 'Venusaur',
        'attack': 82,
        'defense': 83,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        'captured': True
    },
    {
        'number': 4,
        'image_url': '/images/pokemon_snaps/4.svg',
        'name': 'Charmander',
        'attack': 52,
        'defense': 43,
        'type': 'fire',
        'moves': [
          'scratch',
          'ember',
          'metal claw'
        ],
        'captured': True
    },
    {
        'number': 5,
        'image_url': '/images/pokemon_snaps/5.svg',
        'name': 'Charmeleon',
        'attack': 64,
        'defense': 58,
        'type': 'fire',
        'moves': [
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ],
        'captured': True
      },
      {
        'number': 6,
        'image_url': '/images/pokemon_snaps/6.svg',
        'name': 'Charizard',
        'attack': 84,
        'defense': 78,
        'type': 'fire',
        'moves': [
          'flamethrower',
          'wing attack',
          'slash',
          'metal claw'
        ],
        'captured': True
      },
      {
        'number': 7,
        'image_url': '/images/pokemon_snaps/7.svg',
        'name': 'Squirtle',
        'attack': 48,
        'defense': 65,
        'type': 'water',
        'moves': [
          'tackle',
          'bubble',
          'water gun'
        ],
        'captured': True
      },
      {
        'number': 8,
        'image_url': '/images/pokemon_snaps/8.svg',
        'name': 'Wartortle',
        'attack': 63,
        'defense': 80,
        'type': 'water',
        'moves': [
          'tackle',
          'bubble',
          'water gun',
          'bite'
        ],
        'captured': False
      },
      {
        'number': 9,
        'image_url': '/images/pokemon_snaps/9.svg',
        'name': 'Blastoise',
        'attack': 83,
        'defense': 100,
        'type': 'water',
        'moves': [
          'hydro pump',
          'bubble',
          'water gun',
          'bite'
        ],
        'captured': False
      },
      {
        'number': 10,
        'image_url': '/images/pokemon_snaps/10.svg',
        'name': 'Caterpie',
        'attack': 30,
        'defense': 35,
        'type': 'bug',
        'moves': [
          'tackle'
        ],
        'captured': False
      },
      {
        'number': 11,
        'image_url': '/images/pokemon_snaps/12.svg',
        'name': 'Butterfree',
        'attack': 45,
        'defense': 50,
        'type': 'bug',
        'moves': [
          'confusion',
          'gust',
          'psybeam',
          'silver wind'
        ],
        'captured': False
      },
      {
        'number': 12,
        'image_url': '/images/pokemon_snaps/13.svg',
        'name': 'Weedle',
        'attack': 35,
        'defense': 30,
        'type': 'bug',
        'moves': [
          'poison sting'
        ],
        'captured': False
      },
      {
        'number': 13,
        'image_url': '/images/pokemon_snaps/16.svg',
        'name': 'Pidgey',
        'attack': 45,
        'defense': 40,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust'
        ],
        'captured': False
      },
      {
        'number': 14,
        'image_url': '/images/pokemon_snaps/17.svg',
        'name': 'Pidgeotto',
        'attack': 60,
        'defense': 55,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust',
          'wing attack'
        ],
        'captured': False
      },
      {
        'number': 15,
        'image_url': '/images/pokemon_snaps/18.svg',
        'name': 'Pidgeot',
        'attack': 80,
        'defense': 75,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust',
          'wing attack'
        ],
        'captured': False
      },
]
#10 items
  items = [

  ]
  def randomImg():
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    index = randint(0,3)
    return images[index]

  def randomName():
    names= [
        'potion','berry','egg','super potion'
    ]
    index= randint(0,3)
    return names[index]

  for i in range(1,11):
    item_data = {
        'pokemon_id': i,
        'name':randomName(),
        'price':randint(1,100),
        'happiness':randint(1,100),
        'image_url':randomImg(),
    }
    items.append(item_data)

  [db.session.add(Pokemon(**pokemon)) for pokemon in pokemons]
  db.session.commit()
  [db.session.add(Item(**item)) for item in items]

  db.session.commit()
