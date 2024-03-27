label chapterOne:

    scene bg ch1MonasteryArrival with fade
    
    $ GetTextLine(1)

    $ GetTextLine(2)

    show lieutenant idle
    with dissolve

    $ GetTextLine(3)
    
    $ GetTextLine(4)
    
    $ GetTextLine(5)
    
    $ GetTextLine(6)

    $ chs = GetTextLine(7)
    $ renpy.display_menu([(chs[0], "ch1D1Ans1"), (chs[1], "ch1D1Ans1"), (chs[2], "ch1D1Ans1")])
    
    label ch1D1Ans1:

        $ GetTextLine(8)

        $ GetTextLine(9)

        $ GetTextLine(10)

        $ GetTextLine(11)

        $ GetTextLine(12)

    $ chs = GetTextLine(13)
    $ renpy.display_menu([(chs[0], "ch1D2Ans1"), (chs[1], "ch1D2Ans1"), (chs[2], "ch1D2Ans1")])
    
    label ch1D2Ans1:

        $ GetTextLine(14)

        $ GetTextLine(15)

    $ GetTextLine(16)

    $ GetTextLine(17)

    $ GetTextLine(18)

    $ GetTextLine(19)

    jump chapterTwo        