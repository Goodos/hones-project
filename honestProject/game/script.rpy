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

label start:

    jump prologue #prologue wrap

    jump chapterOne #chapter one wrap

    jump chapterTwo #chapter two wrap

    

    return # This ends the game.
