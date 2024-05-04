import random

# basic rooms to start
rooms = {
    'start': 'You are in the starting room. There are exits to the north, east, and west.',
    'room_a': 'You are in Room A.',
    'room_b': 'You are in Room B.',
    'room_c': 'You are in Room C.',
    'room_d': 'You are in Room D.',
    'suspect_room': 'where the answer goes',
}

# clues that could go around the room
room_clues = {
    'room_a': 'Clue for RSA',
    'room_b': 'Clue for XOR',
    'room_c': 'Clue for Vigenere',
    'room_d': 'Clue for xxx',
}

# final answer to complete the game
suspect_details = {
    'name': 'Mrs. Green',
    'weapon': 'rope',
    'final_clue': 'No idea what to put here yet'
}

# movement for the game
def handle_input(current_room, directions):
    while True:
        action = input("\nWhat would you like to do? ").strip().lower()
        if action == 'quit':
            print("Thanks for playing!")
            return 'quit'
        elif action in ['north', 'south', 'east', 'west']:
            if action in directions[current_room]:
                return action
            else:
                print("You can't go that way!")
        else:
            print("Invalid input. Please enter north, south, east, west, or quit.")



def main():
    current_room = 'start'

    # make the room random order
    room_list = list(rooms.keys())
    random.shuffle(room_list)

    # define where the person can go at each room/point
    directions = {
        'start': ['north', 'east', 'west'],
        'room_a': ['north', 'east'],
        'room_b': ['south', 'west'],
        'room_c': ['north', 'west'],
        'room_d': ['south', 'east'],
        'suspect_room': ['south']
    }

    print("Welcome to the text adventure game!\n")
    
    # Game loop
    while True:
        print(rooms[current_room])

        if current_room == 'suspect_room':
            name = input("What is the suspect's name? ").strip().lower()
            weapon = input("What weapon did they use? ").strip().lower()
            final_clue = input("What is the final clue? ").strip().lower()

            if name == suspect_details['name'] and weapon == suspect_details['weapon'] and final_clue == suspect_details['final_clue']:
                print("Congratulations! You get 40000 points")
            else:
                print("Womp")
            break

        action = handle_input(current_room, directions)

        if action == 'quit':
            break
        else:
            current_room = room_list.pop()


if __name__ == "__main__":
    main()
