label prologue:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/dream.mp3" fadeout 1.0 fadein 1.0 volume 0.7

    scene bg dream with fade
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ GetTextLine(1)

    stop music fadeout 1.0

    play music "audio/ye.mp3" fadeout 1.0 fadein 1.0 volume 0.3

    scene bg roomCastle
    with fade    

    show lieutenant idle #at right
    with dissolve

    $ GetTextLine(2)
    with vpunch

    #hide lieut
    #with dissolve

    $ GetTextLine(3)

    #show lieut idle #at left with dissolve

    $ GetTextLine(4)

    $ GetTextLine(5) #with vpunch
    
    $ GetTextLine(6)

    $ GetTextLine(7)

    $ GetTextLine(8)

    hide lieut
    with dissolve

    $ GetTextLine(9)

    $ GetTextLine(10)

    $ GetTextLine(11)

    $ GetTextLine(12)

    scene bg hallwayCastle
    with fade

    $ GetTextLine(13)

    show guardian1 idle at left
    with dissolve

    show guardian2 idle at right
    with dissolve

    $ GetTextLine(14)

    $ GetTextLine(15)

    $ GetTextLine(16)

    $ chs = GetTextLine(17)
    $ renpy.display_menu([(chs[0], "toHall"), (chs[1], "toHall"), (chs[2], "toHall")])

    label toHall:
        $ GetTextLine(18)

        $ GetTextLine(19)

        $ GetTextLine(20)

    scene bg hallCastle
    with fade

    $ GetTextLine(21)

    $ GetTextLine(22)

    show monarch idle
    with dissolve

    $ GetTextLine(23)

    $ GetTextLine(24)

    $ GetTextLine(25)

    $ GetTextLine(26)

    $ GetTextLine(27)

    #возможно сделать смену лица монарха - с обычной ухмылки на озабоченное
    show monarch concern
    with dissolve

    $ GetTextLine(28)
    
    $ GetTextLine(29)

    $ GetTextLine(30)

    #смена лица - с озабоченной на обычную
    show monarch idle
    with dissolve

    $ GetTextLine(31)

    $ GetTextLine(32)

    $ GetTextLine(33)

    $ GetTextLine(34)

    $ GetTextLine(35)

    #смена лица - злое лицо
    show monarch angry
    with dissolve

    $ GetTextLine(36)

    $ GetTextLine(37)

    $ GetTextLine(38)

    $ GetTextLine(39)

    $ chs = GetTextLine(40)
    $ renpy.display_menu([(chs[0], "monarchDialogueAboutMission"), (chs[1], "monarchDialogueAboutMission"), (chs[2], "monarchDialogueAboutMission")])

    label monarchDialogueAboutMission:

        $ GetTextLine(41)

        $ GetTextLine(42)

        $ GetTextLine(43)

        $ GetTextLine(44)

        #смена лица - доброе лицо
        show monarch idle
        with dissolve

        $ GetTextLine(45)

        $ GetTextLine(46)

        $ GetTextLine(47)

        $ GetTextLine(48)

    label dungeonInCastle:
        scene bg dungeonCastle
        with fade

        $ GetTextLine(49)

        show archmaster exhausted
        with dissolve

        $ GetTextLine(50)

        $ GetTextLine(51)

        $ chs = GetTextLine(52)
        $ renpy.display_menu([(chs[0], "dungeonCastleArchMasterDialogue1"), (chs[1], "dungeonCastleArchMasterDialogue1"), (chs[2], "dungeonCastleArchMasterDialogue1")])
        
        label dungeonCastleArchMasterDialogue1:

            $ GetTextLine(53)

            $ GetTextLine(54)

            $ GetTextLine(55)

            $ chs = GetTextLine(56)
            $ renpy.display_menu([(chs[0], "dungeonCastleArchMasterDialogue2"), (chs[1], "dungeonCastleArchMasterDialogue2"), (chs[2], "dungeonCastleArchMasterDialogue2")])

            label dungeonCastleArchMasterDialogue2:

                show archmaster idle
                with dissolve

                $ GetTextLine(57)

                $ GetTextLine(58)

                $ GetTextLine(59)

                show archmaster concussion
                with dissolve

                $ GetTextLine(60)

                $ chs = GetTextLine(61)

                show archmaster concussion at move_right

                $ renpy.display_menu([(chs[0], "dungeonCastleArchMasterDialogue3"), (chs[1], "dungeonCastleArchMasterDialogue3"), (chs[2], "dungeonCastleArchMasterDialogue3")])

                label dungeonCastleArchMasterDialogue3:

                    show lieutenant idle at left
                    with dissolve

                    $ GetTextLine(62)

                    $ GetTextLine(63)

                    $ GetTextLine(64)

                    scene bg prologueEnd
                    with fade
                    
                    $ GetTextLine(65)

                    jump chapterOne


