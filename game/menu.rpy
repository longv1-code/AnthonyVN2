define menu_entries = {
    "ant": {
        "name" : "Ant",
        "image": "characters/Ant/ant.png",
        "traits": [
            "Hard to get",
            "Secretly loves you",
            "Latino and gay"
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
    },
    "parker": {
        "name": "Parker",
        "image": "characters/Parker/parker peace.png",
        "traits": [
            "Jamaican",
            "Swagtasic",
            "Intellectual"
        ],
    },
    "abot": {
        "name": "ABot",
        "image": "characters/ABot/abot chibi.png",
        "traits": [
            "Nervous",
            "Chill",
            "Gambling Addict",
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
    },
    "alex": {
        "name": "Alex",
        "image": "characters/Alex/alex.jpg",
        "traits": [
            "Sarcastic",
            "Smug",
            "Honest",
        ],
    },
    "sofia": {
        "name": "Sofia",
        "image": "characters/Sofia/sofia.png",
        "traits": [
            "Loyal",
            "Skewed Moral Compass",
            "Emotional",
        ],
    },
}

define menu_pages = [
    ["abot", "alex", "ant", "charley"],
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