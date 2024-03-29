# Giraudo Francesco Es 35

from sys import exit

def gold_room():
    ''' A room with full of god. '''    
    print("This room is full of gold.  How much do you take?")

    next = input("> ")

    # this exception verify that the user typed a number
    try:
        how_much = int(next)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    ''' A room with a bear '''    
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        elif next == "open door" and not bear_moved:
            print("The bear doesn't like to be disturbed while eating honey.")
            dead("The bear chews your leg off.")
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    ''' A room with evil Cthulhu '''
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    ''' Call this when the hero dead '''
    print(why, "Good job!")
    exit(0)

def start():
    ''' Begining of the story '''
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

#   Study Drills
#   1. Draw a map of the game and how you flow through it.
#   2. Fix all of your mistakes, including spelling mistakes.
#   3. Write comments for the functions you do not understand.
#   4. Add more to the game. What can you do to both simplify and expand it?
#   5. The gold_room has a weird way of getting you to type a number. What are all the bugs in this
#   way of doing it? Can you make it better than what I’ve written? Look at how int() works for
#   clues.