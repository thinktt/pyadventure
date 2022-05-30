
# this is the game_root function. Our program will always come back here and then run the next
# room function. This keeps our program from filling up memory with open function calls. 
def game_root():
    print("Welcome to Little Cave Adventure!")

    # here we set the first room we will go to
    next_room = cave

    # we create a loop that will continue to get a room (as a functin name) go to that room by 
    # running that function, if we return None then that means we are ending the game, we will  
    # break out of the loop and the program will then end
    while True:
        next_room = next_room()
        if next_room == None : break

def cave():
    print()
    print("You are in warm comfortable cave dwelling. There is is a small fire \n" +
    "burning in the center of the room. On the floor is your bison skin bed. There \n" +
    "are cave paintings on the wall. There is a spear here. There is an exit to the east.")
    print("1. Leave Cave")
    print("2. Sleep")

    # here we have another loop. The loop will take a choice from the user. If the coice is one 
    # we know we will return room (a function name) to go to next. If we don not know that option
    # we will say so and and wait for the user to try again
    while True:
        choice = input()    
        if choice == "1":
            return outside_cave
        elif choice == "2":
            return you_sleep
        else:
            print("I don't know that option")

def outside_cave():
    print()
    print("You are ouside the cave. There is a fierce bear here!")
    print("1. Fight Bear")
    print("2. Run back to cave")
   
    while True:
        choice = input()    
        if choice == "1":
            print("You killed the bear! You murderer! You lose.")
            return end
        elif choice == "2":
            return cave
        else:
            print("I don't know that option")


def you_sleep():
    print()
    print("You awaken and it is morning. It seems like a good time to go hunting.")
    print("1. Go hunting")
    print("2. Sleep some more")

    while True:
        choice = input()
        if choice == "1":
            print()
            print("You were able to hunt down a large buffalo. You are happy. You win!")
            return end
        if choice == "2":
            return you_sleep
        else:
            print("I don't know that option")


def end(): 
    print("Thanks for playing Little Cave Adventure!")
    return None

game_root()
