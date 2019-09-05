# Giraudo Francesco Es31 Study Drill 2

tools = []

def main_room():
    while True:
        print("What door you open? [1/2]")

        dark_room = input("> ")

        if dark_room == "1":
            room_one()
            break
        elif dark_room == "2" and "key" in tools:
            print("This is not the correct key...\nI think you can't open this door.")
        elif dark_room == "2" and not "key" in tools:
            print("The door is closed.\nYou need a key to open it.")
            print("Wait...\nThere is something under your feet.")
            print("It's a human skull!")
            print("It has got a key in the mouth.")
            print("Do you wanna take the key? [Y/n]")
            
            take_key = input("> ").upper()

            if take_key == "Y":
                print("You got KEY.")
                tools.append("key")
            elif take_key == "N":
                print("You let the key inside the skull.")
            else:
                print("I think you want let the key inside the skull.")
        else:
            print("You stumble around the room until you starve.")
            break

def room_one():
    print("There are 7 sleeping tigers.")
    if "sword" not in tools:
        print("There is a sword on the floor.")
    print("What do you do?")
    print("1. Go back")
    print("2. Go ahead trying not to wake the tigers")
    if "sword" not in tools:
        print("3. Take the sword and fight with the tigers")

    tigers_room = input("> ")

    if int(tigers_room) <= 1:
        print("\nThe door is locked from the inside!")
        print("You can't go back!")
    
    if int(tigers_room) <= 2:
        print("The tigers are waking up...")
        print("The tigers eat you.")
    elif int(tigers_room) == 3:
        tools.append("sword")
        print("You got SWORD.")
        print("\nYou kill all the tigers while they sleep.")
        print("There is another door.")
        print("You open the door.")
        gold_room()

def gold_room():
    print("You are in the gold room.\nThere is a treasure chest closed by a padlock")
    print("You can open it only if you have the key.")
    
    if "key" in tools:
        print("You can open the chest!\nThere is gold and diamonds inside!\nYou are rich now $_$")
    else:
        print("Oh no! You haven't a key, so you can't open the chest.")

print("You are in dark room.")
print("In front of two doors.")
main_room()

print("""
 _______  _______  __   __  _______    _______  __   __  _______  ______   
|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|""")

