# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Main characters
define me = Character("Me")
define lieut = Character("Lieutenant")
define monarch = Character("Monarch")
define archMaster = Character("ArchMaster")

#Prologue characters
define guardian1 = Character("Guardian1")
define guardian2 = Character("Guardian2")

# The game starts here.

screen debugWin(value):
    vbox:
        text value size 40

label test1:
    "bruh"
    return

label test2:
    "hui"
    return

label start:

    #call test1

    #call test2

    jump prologue #prologue wrap

    jump chapterOne #chapter one wrap

    #call chapterTwo #chapter two wrap

    

    return # This ends the game.
