#!/usr/bin/python3
"""Dictionary containing all rooms in the house. To be imported by rpg.py """

rooms = {
            'Your Bedroom' : {
                  'directions' : {
                    'south' : 'Main Hall',
                  },
                  'item'  : 'flashlight', # needed to enter main hall
                  'description' : 'It\'s your bedroom, although its dark you know the layout. As usual your stupid cat darts off suddenly knocking everything off your desk.'
                },
            'Main Hall' : {
                'directions' : {
                  'north' : 'Your Bedroom',
                  'south east' : 'Bedroom',
                  'south' : 'Small Bedroom',
                  'south west': 'Bathroom',
                  'west' : 'Atrium',
                },              
                'required item' : 'flashlight', 
                'description' : 'The largest hall in the house, you have many options on where to go.'
              },
            'Bedroom' : {
              'directions' : {
                'north' : 'Main Hall', 
              },  
                'item' : 'master bedroom key', # opens master bedroom
                'monster' : 'Mushu the Great Dragon', # needs worm from front yard
                'description' : 'A strange skunky smell is coming from this room... '
            },
            'Small Bedroom' : {
              'directions' : {
                'north' : 'Main Hall',
              },
              'item' : 'backyard key', # necessary to win the game and exit
              'description' : 'A child\'s bedroom. Toys are scattered everywhere. Someone\'s going to get grounded...'
            }, 
            'Bathroom' : {
              'directions' : {
                'north' : 'Main Hall', 
              },
              'item' : 'water', # cracker ingredient
              'description' : 'You hear a leaky water faucet. When\'s that landlord gonna get his sh!t together?!'
            }, 
            'Atrium' : {
              'directions' : {
                'north' : 'Entrance',
                'east' : 'Main Hall', 
                'west' : 'Living Room',
              },            
              'description' : 'Relatively small atrium, you accidentally step on a cat. Whoops!'
            },
            'Entrance' : {
              'directions' : {
                'north' : 'Front Yard',
                'south' : 'Atrium', 
                'west' : 'Master Bedroom',
              },
              'description' : 'A small hallway leading to the front door.'
            }, 
            'Front Yard' : {
              'directions' : {
                'south' : 'Entrance', 
              },
              'item' : 'worm', # worm to feed mushu
              'description' : 'Spacious front yard. A giant chicken statue sits on a tree stump.'
            }, 
            'Master Bedroom' : {
              'directions' : {
                'east' : 'Entrance', 
              },
              'item' : 'salt', # cracker ingredient
              'required item' : 'master bedroom key',
              'description' : 'This room feels cramped with an oversized king bed in it.'
            },
            'Living Room' : {
              'directions' : {
                'east' : 'Atrium',
                'south west' : 'Kitchen',
              },
              'description' : 'Literally never used, although it\'s great spot for catching your toe on some furniture.'
            },
            'Kitchen' : {
              'directions' : {
                'north' : 'Living Room',
                'west' : 'Pantry',
                'south west' : 'Bird Room'
              }, 
              'item' :  'oven', # needs all 3 cracker ingredient to make cracker
              'description' : 'By far the nicest room in the house, recently remodeled. The smell of something yummy fills the air.'
            },
            'Pantry' : {
              'directions' : {
                'east' : 'Kitchen',
              },
              'item' : 'flour', # cracker ingredient
              'description' : 'Technically a second atrium, convered to a pantry. What sort of treasures await you?'
            }, 
            'Bird Room' : {
              'directions' : {
                'east' : 'Kitchen',
                'south west' : 'Backyard',
              },
              'monster' : 'Poly the Bird', # needs cracker
              'description' : 'Abandon all hope ye who enter here. You feel the embodiment of evil eminating from this room. From the darkness comes a loud screech and you hear \'Poly wants a cracker\''
            }, 
            'Backyard' : {
              'directions' : {
                'MEME CITY' : 'MEME CITY'
              },
              'required item' : 'backyard key', 
              'description' : 'The promised land! FINALLY, I CAN GO BACK TO LOOKING AT DANK MEMES!'
            }
         }