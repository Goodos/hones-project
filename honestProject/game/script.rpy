# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Tomboy")
define me = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/ye.mp3" fadeout 1.0 fadein 1.0

    scene bg dream with fade:
        blur 10
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Сквозь пелену сна к тебе тянется чья-то рука. Кончики пальцев
    нежно касаются твоей щеки. Пальцы обжигают твою щёку могильным
    холодом, словно весенняя капель пробирающаяся сквозь последние
    сугробы. Просто прикосновение. Не больше, не меньше. Ты не
    можешь вспомнить чьи это руки. Как не можешь вспомнить когда
    оно произошло. Но почему-то ты уверен полностью, что это
    прощальное прикосновение."

    scene bg room
    with fade

    show tomboy idle at right
    with dissolve

    e "Учитель!"

    hide tomboy
    with dissolve

    "Громкий стук в дверь возвращает тебя в реальный мир. Видимо,
    случилось что-то срочное, раз твой помощник пришёл лично будить
    тебя. Хорошо потянувшись, ты запрыгиваешь в тапочки и,
    почёсывая бок направляешься к двери."

    show tomboy idle at left with dissolve

    e "Учитель, доброе утро!"

    me "Доброе" with vpunch
    
    e "Вас срочно вызывают на аудиенцию к Монарху."

    "В столь ранний час?"

    menu:

        "оки доки":
            jump good

        "послать нахуй":
            jump evil

    label good:
    
        me "Хорошо, передай что я буду в Тронном зале через двадцать минут."

        jump toHall

    label evil:        

        me "Пошел нахуй"

        jump toHall

    label toHall:

        "Иду в зал"


    # This ends the game.

    return
