#!/usr/bin/python3

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
from rooms import rooms

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  """Display intial gameplay instructions."""

  #print a main menu and the commands
  print('''
It's a dark and stormy night. You're sitting in your room, trying to see some dank memes when the power goes out! Now you must navigate the dangers of this home and restart the generator in your backyard
========
Commands:
  go [direction]
  get [item]
  "I'm scared of the dark!" press q
''')
showInstructions()

def showStatus(currentRoom, inventory):
  """Print player's current status, including room, room description, inventory, possible directions """
  #print the player's current roon
  print('---------------------------')
  print('You are in the ' + currentRoom)
  # print this rooms description
  print(rooms[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print list of possible directions 
  print(f"Possible directions: {list(rooms[currentRoom]['directions'].keys())}")
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

def move_rooms(move, currentRoom, inventory):
    """Function allows players to move from room to room: 
          > checks for specific items if required to move into or out of rooms
          > checks for rooms containing monsters and if required items are present
          > alerts player if they cannot go a certain way or if required item is not present
    """

    #check that they are allowed wherever they want to go
    new_room = currentRoom

    if move[1] in rooms[currentRoom]['directions']:
      # represents the next room the player would move into
      interim_room = rooms[currentRoom]['directions'][move[1]]
      room_item = rooms[interim_room].get('required item') #required item for entering next room
      
      # checks if player has required item in inventory and if room requires an item
      if room_item != None and room_item not in inventory :
        print("You can't go that way without the proper items.") 
      
      # conditional for first monster room
      elif 'Mushu the Great Dragon'  == rooms[interim_room].get('monster') and 'worm' in inventory:
        print("---------------------------")
        print(f"You've quenched {rooms[interim_room]['monster']} hunger")
        new_room = rooms[currentRoom]['directions'][move[1]]
      
      # conditional for final boss
      elif 'Poly the Bird' == rooms[interim_room].get('monster') and 'cracker' in inventory:
        print("---------------------------")
        print(f"The great beast {rooms[interim_room]['monster']} is satisfied... for now. Leave quickly!")
        new_room = rooms[currentRoom]['directions'][move[1]]

      else:
        #set the current room to the new room
        new_room = rooms[currentRoom]['directions'][move[1]]
        kitchen_check(currentRoom, inventory)
    #there is no door (link) to the new room
    else:
      print("---------------------------")
      print('You can\'t go that way!')

    return new_room

def get_item(move, currentRoom, inventory):
    """ Allows players to 'pick up' items. Additionally calls kitchen_check function for special cracker recipe """
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']

      # check if player is in kitchen to make a cracker
      kitchen_check(currentRoom, inventory)

    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

def kitchen_check(currentRoom, inventory):
  """ Determines whether player can create a 'cracker'. Checks current room and if the required items are in the inventory"""

    # conditional for special actions in kitchen 
  if currentRoom == "Kitchen":
    cracker_recipe = ['water', 'salt', 'flour', 'oven']
    # checks if all required items to make a cracker are in the inventory and removes them
    if 'water' in inventory and 'salt' in inventory and 'flour' in inventory and 'oven' in inventory:
      print("---------------------------")
      print('You have all the items to make a cracker. Let\'s get cracking')
      print("---------------------------")
      # loop over ingredients in recipe and removes them from inventory then add cracker to inventory
      for ingredient in cracker_recipe:
        if ingredient in inventory:
          inventory.remove(ingredient)
      inventory.append('cracker')

def is_game_over_check(currentRoom, inventory):
  """ Conditionally checks for win/lose conditions """

  is_game_over = False

  ## Define how a player can win (by exiting to the backyard)
  if currentRoom == 'Backyard' and 'backyard key' in inventory:
    print('You made it to the backyard!')
    is_game_over = True

  ## If a player enters a room with a monster
  elif 'Poly the Bird' == rooms[currentRoom].get('monster') and 'cracker' not in inventory:
    print(f"Like thousands before you... you have fallen prey to {rooms[currentRoom]['monster']}'s horrors. GAME OVER!")
    is_game_over = True

  elif 'Mushu the Great Dragon' == rooms[currentRoom].get('monster') and 'worm' not in inventory:
    print(f"{rooms[currentRoom]['monster']} has got you... FREAKING LOSEEERRR!")
    is_game_over = True
  
  return is_game_over

def main():
  #an inventory, which is initially empty
  inventory = ['water', 'flour', 'salt', 'flashlight', 'worm']

  #start the player in Your Bedroom
  currentRoom = 'Your Bedroom'

  #loop forever
  while True:
    # show game status at each iteration
    showStatus(currentRoom, inventory)

    #get the player's next 'move'
    move = ''
    while move == '':
      move = input('> ')

    # split allows an item to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    # quit game
    if move[0] == 'q' :
      print('COWARD!')
      break

    #if they type 'go' first
    if move[0] == 'go':
      currentRoom = move_rooms(move, currentRoom, inventory)

    #if they type 'get' first
    if move[0] == 'get' :
      get_item(move, currentRoom, inventory)
    
    # check if game is over -> if true break from loop
    if is_game_over_check(currentRoom, inventory):
      break

if __name__ == '__main__':
  main()