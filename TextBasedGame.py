# Marcel Vicente Garza

def objective():
    print()
    print('Vampire Text Adventure Game')
    print()
    print("You happen to be inside a mansion and there is a vampire hosting a meal in the dining room waiting")
    print("for a real estate agent to come by. To defeat him, you need to gather several items. You will need")
    print("garlic from the kitchen to repel the vampire, a stake from the living room, a crossbow in the bedroom, ")
    print("dead man’s blood in the attic, which is basically poison to him, flash grenade in the ballroom to blind")
    print("him for a moment, and a scroll in the library explaining how to defeat him. ")

def show_instructions():
    # Prints a main menu and the commands
    print()
    print('Collect the 6 items to win the game or be bitten by the vampire')
    print('Move commands: North, East, South, West')
    print('Add to Inventory: get \'item name\'')

def main():
    # A dictionary for the vampire text game
    # The dictionary links a room to other rooms as well as item
    rooms = {
        'Entrance Hall': {'Room': 'Entrance Hall', 'East': 'Living Room', 'item': []},
        'Living Room': {'Room': 'Living Room', 'West': 'Entrance Hall', 'North': 'Ballroom', 'East': 'Bedroom', 'South': 'Kitchen', 'item': ['stake']},
        'Ballroom': {'Room': 'Ballroom', 'East': 'Library', 'South': 'Living Room', 'item': ['flash grenade']},
        'Library': {'Room': 'Library', 'West': 'Ballroom', 'item': ['scroll']},
        'Bedroom': {'Room': 'Bedroom', 'West': 'Living Room', 'North': 'Attic', 'item': ['crossbow']},
        'Attic': {'Room': 'Attic', 'South': 'Bedroom', 'item': ['dead man\'s blood']},
        'Kitchen': {'Room': 'Kitchen', 'North': 'Living Room', 'East': 'Dining Room', 'item': ['garlic']},
        'Dining Room': {'Room': 'Dining Room', 'West': 'Kitchen', 'item': ['vampire']}  # Villain
    }

    directions = ['North', 'East', 'South', 'West']

    # Start the player in the hall
    current_room = rooms['Entrance Hall']

    inventory = []

    def moving_and_collecting():
        nonlocal current_room
        while True:
            # Displays current location
            print('You are in the {}.'.format(current_room['Room']))
            print('Inventory: {}'.format(inventory))
            # Displays different possible commands
            print('Enter either North, East, South, West, or get \'item\'')
            # Displays item
            if current_room['item']:
                print('In the room is the: {}'.format(', '.join(current_room['item'])))
            # Prompts user for command
            user_input = input('Enter a command.').capitalize()
            print()
            # Allows player to move to another room
            if user_input in directions:
                if user_input in current_room:
                    current_room = rooms[current_room[user_input]]
                    # Losing function
                    if current_room == rooms['Dining Room']:
                        print('You have encountered the vampire before gathering the items needed.')
                        print('This Sucks!...Game Over!')
                        quit()
                else:
                    # Bad Movement
                    print('Can\'t go that way')
            # Allows player to gather items
            elif user_input.lower().split()[0] == 'get':
                if len(user_input.split()) == 2:
                    item = user_input.lower().split()[1]
                    if item in current_room['item']:
                        current_room['item'].remove(item)
                        inventory.append(item)
                        print('You have obtained the {}.'.format(item))
                    else:
                        print("I don't see that here.")
                elif len(user_input.split()) == 3:
                    item = 'flash grenade'
                    if item in current_room['item']:
                        current_room['item'].remove(item)
                        inventory.append(item)
                        print('You have obtained the {}.'.format(item))
                    else:
                        print("I don't see that here.")
                elif len(user_input.split()) == 4:
                    item = 'dead man\'s blood'
                    if item in current_room['item']:
                        current_room['item'].remove(item)
                        inventory.append(item)
                        print('You have obtained the {}.'.format(item))
                    else:
                        print("I don't see that here.")
                # Bad command
                else:
                    print("I don't understand that command.")
            # Bad command
            else:
                print("I don't understand that command")
            # Winning function
            if len(inventory) == 6:
                print('Congratulations! You have gathered all the items needed and defeated the vampire.')
                print('The real estate agent is safe.')
                print('Thanks for playing!')
                quit()
    moving_and_collecting()
objective()
show_instructions()
main()



