define menu_entries = {
    "ant": {
        "name" : "Ant",
        "image": "characters/Ant/ant.png",
        "traits": [
            "Hard to get",
            "Secretly loves you",
            "Latino and gay"
        ],
        "voice": [
            "characters/Ant/maidline1.mp3",
            "characters/Ant/maidline2.mp3",
            "characters/Ant/maidline3.mp3",
            "characters/Ant/maidline4.mp3",
            "characters/Ant/maidline5.mp3",
            "characters/Ant/maidline6.mp3",
            "characters/Ant/maidline7.mp3",
            "characters/Ant/maidline8.mp3",
            "characters/Ant/maidline9.mp3",
        ],
    },
    "charley": {
        "name": "Charley",
        "image": "characters/Charley/charley maid.png",
        "traits": [
            "Strong",
            "Dragon of Dojima",
            "Stoic",
        ],
        "voice": "characters/Charley/anthonybirthday.mp3"
    },
    "parker": {
        "name": "Parker",
        "image": "characters/Parker/parker peace.png",
        "traits": [
            "Jamaican",
            "Swagtasic",
            "Intellectual"
        ],
        "voice": "characters/Parker/ALI G MP3 BOOYAHKASHA.mp3"
    },
    "abot": {
        "name": "ABot",
        "image": "characters/ABot/abot chibi.png",
        "traits": [
            "Nervous",
            "Chill",
            "Gambling Addict",
        ],
        "voice": [
            "characters/ABot/ABotLine1.wav",
            "characters/ABot/ABotLine2.wav",
            "characters/ABot/ABotLine3.wav",
            "characters/ABot/ABotLine3alt.wav",
            "characters/ABot/ABotLine4.wav",
            "characters/ABot/ABotLine5.wav",
        ],
    },
    "sebastian": {
        "name": "Sebastian",
        "image": "characters/Sebastian/sebastian.png",
        "traits": [
            "Tired",
            "Enigmatic",
            "Easy Going",
        ],
        "voice": "characters/Sebastian/Recording 2.wav",
    },
    "jayden": {
        "name": "Jayden",
        "image": "characters/Jayden",
        "traits": [
            "",
            "",
            "",
        ],
        "voice": "characters/Jayden",
    },
    "sofia": {
        "name": "Sofia",
        "image": "characters/Sofia",
        "traits": [
            "",
            "",
            "",
        ],
        "voice": "characters/Sofia",
    },
}

define menu_pages = [
    ["abot", "ant", "charley", "jayden"],
    ["parker", "sebastian", "sofia"],
]

default persistent.menu_removed = []

screen menu():

    tag menu
    modal True

    default page = 0

    # Notebook background
    add "images/bg menu.jpg":
        xysize(1920, 1080)
        fit("cover")

    # Notebook title
    text "MAID CAFE MENU":
        xalign 0.5
        ypos 40
        size 45
        color "#3b3028"

    # Display entries for the current page
    grid 2 2:
        xpos 150
        ypos 150
        xspacing 100
        yspacing 40

        for name in menu_pages[page]:

            if name not in persistent.menu_removed:
                # Retrieve entry from dictionary
                $ entry = menu_entries[name]

                # Entire entry is clickable
                button:
                    background None
                    hover_background "#00000022"
                    xsize 750
                    ysize 200

                    action [
                        Return(name)
                    ]

                    hbox:
                        spacing 20

                        # Entry image
                        add entry["image"]:
                            xysize (180, 180)
                            fit "contain"

                        # Three bullet points
                        vbox:
                            spacing 10
                            yalign 0.5

                            text entry["name"]:
                                size 28
                                color "#3b3028"

                            for point in entry["traits"]:
                                text "• [point]":
                                    size 18
                                    color "#3b3028"
                                    xmaximum 450

    # Previous page button
    textbutton "Previous":
        xpos 150
        ypos 650
        action SetScreenVariable("page", page - 1)
        sensitive page > 0

    # Next page button
    textbutton "Next":
        xpos 1050
        ypos 650
        action SetScreenVariable("page", page + 1)
        sensitive page < len(menu_pages) - 1

    # Page counter
    text "[page + 1] / [len(menu_pages)]":
        xalign 0.5
        ypos 660
        color "#3b3028"
        size 22