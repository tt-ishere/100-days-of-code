print("Welcome to the game of choices")
print("Your mission is to find the treasure island\n")

go = input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if go == "left":
    #Game will continue
    island = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n').lower()
    if island == "wait":
        #Game will continue
        door = input('You arive on the island unharmed. There is a house with 3 doors. One red, yellow and blue. which color do you choose?\n').lower()
        if door ==  "yellow":
           print("You found the room with the treasure \nYou won!!!")
        elif door == "red":
             print("You entered a room full of fire. Game over!")
        else:
            print("You entered a room full of beasts. Game over!")
    else:
        print("You drowned and died. Game over!")
else:
    print("You fell into a deep man hole and broke you neck. Game over!")
    