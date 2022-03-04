# defining Class
class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.__str__()

    def enter_room(self):
        print('You are entering Room: ' + self.description)
        return self

    def print_description(self):
        print('You are in Room: ' + self.description)


def main():
    room1 = Room('Bedroom 2')
    room2 = Room('Family Room')
    room3 = Room('Storage Room')
    room4 = Room('Bathroom')
    room5 = Room('Courtyard')
    room6 = Room('Dinning Room')
    room7 = Room('Bedroom 1')
    room8 = Room('Living Room')
    room9 = Room('Kitchen')
    room0 = Room('Entrance')

    room_list = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9]
    print(room_list)
# entrance
    room0.north = room8
# Bedroom 1
    room1.east = room2
    room1.south = room4
# Bedroom 2
    room2.east = room3
    room2.south = room5
    room2.west = room1
# Storage Room
    room3.south = room6
    room3.west = room2
# Bathroom
    room4.north = room1
    room4.east = room5
    room4.south = room7
# CourtYard
    room5.north = room2
    room5.east = room6
    room5.south = room8
    room5.west = room4
# Dining Room
    room6.north = room3
    room6.south = room9
    room6.west = room5
# Bedroom 1
    room7.north = room4
    room7.east = room8
# Living Room
    room8.north = room5
    room8.east = room9
    room8.south = room0
    room8.west = room7
# Kitchen
    room9.north = room6
    room9.west = room8

    current_room = room0

    # current_room = current_room.north.enter_room()
    # print(current_room)
    # current_room = current_room.south.enter_room()
    # print(current_room)
    # current_room = current_room.north.enter_room()
    # print(current_room)
    # current_room = current_room.west.enter_room()
    # print(current_room)
    #
    # current_room.print_description()

# Direction movement
    game_active = True

    valid_commands = ['north', 'n', 'east', 'e', 'south', 's', 'west', 'w', 'up', 'u', 'down', 'd', 'left', 'l',
                      'right', 'r', 'exit']
    while game_active:
        current_room.print_description()
        key = input('What would you like to do')
        key = key.lower()
        print(key)
        if key in valid_commands:
            if key in ['exit']:
                print('Alright... you will be exited!, See you Sucker!')
                game_active = False
            elif key in ['north', 'n', 'up', 'u'] and current_room.north is not None:
                current_room = current_room.north.enter_room()
            elif key in ['east', 'e', 'right', 'r'] and current_room.east is not None:
                current_room = current_room.east.enter_room()
            elif key in ['south', 's', 'down', 'd'] and current_room.south is not None:
                current_room = current_room.south.enter_room()
            elif key in ['west', 'w', 'left', 'l'] and current_room.west is not None:
                current_room = current_room.west.enter_room()
            else:
                print('Sorry, You hit a wall! I hope you head hurts!')
        else:
            print('You sucker, I don\'t know what you mean! Check your spelling moron!')


main()
