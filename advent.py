
def game_root():
    cave()


def cave():
    print("You are in warm comfortable cave dwelling. There is is a small fire \n" +
    "burning in the center of the room. On the floor is your bison skin bed. There \n" +
    "are cave paintings on the wall. There is a spear here. There is an exit to the east.\n")

    print("1. Leave Cave")
    print("2. Sleep")

    choice = input()

    if choice == "1":
        outside_cave()
    if choice == "2":
        you_sleep()
    else:
        print("I don't know that option")


def outside_cave():
    print("You are ouside the cave. There is a fierce bear here!")

    print("1. Fight Bear")
    print("2. Run back to cave")

    choice = input()

    if choice == "1":
        print("You killed the bear! You murderer! You lose.")
    if choice == "2":
        cave()
    else:
        print("I don't know that option")


def you_sleep():
    print("You awaken and it is morning. It seems like a good time to go hunting.")

    print("1. Go hunting")
    print("2. Sleep some more")

    choice = input()

    if choice == "1":
        print("You were able to hunt down a large buffalo. You are happy. The end.")
    if choice == "2":
        you_sleep()
    else:
        print("I don't know that option")


game_root()
