# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg dream:
    "prologue/bgDream.jpg"
    xysize (1920, 1080)
image bg roomCastle:
    "prologue/bgRoomCastle.jpg"
    xysize (1920, 1080)
image bg hallwayCastle:
    "prologue/bgHallwayCastle.jpg"
    xysize (1920, 1080)
image bg hallCastle:
    "prologue/bgHallCastle.png"
    xysize (1920, 1080)
image bg dungeonCastle:
    "prologue/bgDungeonCastle.png"
    xysize (1920, 1080)

#image lieutenant idle2
    #zoom 0.5
    #xycenter (0.0, 0.0)
#image monarch idle:
    #xysize (300, 600)

#image lieutenant idle

transform move_right:
    linear 2.0 xalign 1.0

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
