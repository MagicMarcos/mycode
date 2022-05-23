#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
It's a dark and stormy night. You're sitting in your room, trying to see some dank memes when the power goes out! Now you must navigate the dangers of this home and restart the generator in your backyard
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print(rooms[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))

  print(f"Possible directions: {list(rooms[currentRoom]['directions'].keys())}")
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = ['water', 'flour', 'salt', 'cracker', 'oven']

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
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
                'item' : 'Master Bedroom Key', # opens master bedroom
                'monster' : 'Mushu the Great Dragon', # needs worm from front yard
                'description' : 'A strange skunky smell is coming from this room... '
            },
            'Small Bedroom' : {
              'north' : 'Main Hall',
              'item' : 'Backyard Key', # necessary to win the game and exit
              'description' : 'A child\'s bedroom. Toys are scattered everywhere. Someone\'s going to get grounded...'
            }, 
            'Bathroom' : {
              'north' : 'Main Hall', 
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
              'required item' : 'Master Bedroom Key',
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
              'required item' : 'Backyard Key', 
              'description' : 'The promised land! FINALLY, I CAN GO BACK TO LOOKING AT DANK MEMES!'
            }
         }

#start the player in the Hall
currentRoom = 'Your Bedroom'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  # quit game
  if move[0] == 'q' :
    print('COWARD!')
    break

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
  
    if move[1] in rooms[currentRoom]['directions']:
      interim_room = rooms[currentRoom]['directions'][move[1]]
      room_item = rooms[interim_room].get('required item') 

      if room_item != None and room_item not in inventory :
        print("You can't go that way without the proper items.") 

      elif 'Mushu the Great Dragon'  == rooms[interim_room].get('monster') and 'worm' in inventory:
        print(f"You've quenched {rooms[interim_room]['monster']} hunger")
        currentRoom = rooms[currentRoom]['directions'][move[1]]

      elif 'Poly the Bird' == rooms[interim_room].get('monster') and 'cracker' in inventory:
        print(f"The great beast {rooms[interim_room]['monster']} is satisfied... for now. Leave quickly!")
        currentRoom = rooms[currentRoom]['directions'][move[1]]

      else:
        #set the current room to the new room
        currentRoom = rooms[currentRoom]['directions'][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  if currentRoom == "Kitchen":
    if 'water' in inventory and 'salt' in inventory and 'flour' in inventory and 'oven' in inventory:
      print('You have all the items to make a cracker. Let\'s get cracking')
      inventory.remove('water')
      inventory.remove('salt')
      inventory.remove('flour')
      inventory.remove('oven')
      inventory.append('cracker')
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Backyard' and 'key' in inventory:
    print('You made it to the backyard!')
    break

  ## If a player enters a room with a monster
  elif 'Poly the Bird' == rooms[currentRoom].get('monster') and 'cracker' not in inventory:
    print(f"Like thousands before you... you have fallen prey to {rooms[currentRoom]['monster']}'s horrors. GAME OVER!")
    break
  elif 'Mushu the Great Dragon' == rooms[currentRoom].get('monster') and 'worm' not in inventory:
    print(f"{rooms[currentRoom]['monster']} has got you... FREAKING LOSEEERRR!")
    break