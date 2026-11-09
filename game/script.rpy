# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ant = Character("Ant")
define charley = Character("Charley")
define parker = Character("Parker")
define abot = Character("Abot")
define seb = Character("Sebastian")
define mc = Character("Anthony")
define kevin = Character("Kevin")

define arlecchino = Character("Arlecchino")
define x = Character("?")

default retries = 0
default persistent.endingB = False

image bg city:
    "images/bg city.jpg"
    xysize (1920, 1080)
    fit "cover"

image bg animebedroom:
    "images/bg animebedroom.jpg"
    xysize (1920, 1080)
    fit "cover"

image bg bedroom:
    "images/bg bedroom.jpg"
    xysize (1920, 1080)
    fit "cover"

image bg cafe_entrance:
    "images/bg cafe_entrance.png"
    xysize (1920, 1080)
    fit "cover"
    xalign 0.5
    yalign 0.3

image bg cafe_hall:
    "images/bg cafe_hall.png"
    xysize (1920, 1080)
    fit "cover"

image bg cafe_seat:
    "images/bg cafe_seat.png"
    xysize (1920, 1080)
    fit "cover"

image bg computer:
    "images/bg computer.jpg"
    xysize (1920, 1080)
    fit "cover"
    yalign 0.6

image bg door:
    "images/bg door.jpg"
    xysize (1920, 1080)
    fit "cover"

image bg black:
    "images/bg black.jpg"
    xysize (1920, 1080)
    fit "cover"

# The game starts here.

label start:
    if persistent.endingB:
        jump realistic
    
    "Today is Novemeber 9th, 2026. A very special day for a certain someone."

    "It is your birthday. You've been looking forward this ever since you planned a whole hangout session with your friends."

    "You slowly wakes up from your slumber."

    scene bg bedroom

    mc "What time is it...?"

    "You check on your phone."

    mc "2 PM? I'm up early."

    menu:
        mc "I want to sleep more but it seems I can't. What should I do?"

        "Doomscroll":
            jump ending_doomscroll

        "Get out of bed":
            jump dream
        

label ending_doomscroll:
    scene bg black
    "You chose to doomscroll on Instagram."

    mc "One funny reel and I'll call it."

    "Couple minutes fly by."

    mc "Damn, why is my feed so ass today?"

    mc "There's gotta be one good pull, right?"

    "Hours fly by."

    mc "Bro, I've gotten more spoilers on the hit game Fire Emblem: Fortune Weave than a single funny reel. I'll continue looking."

    "Hours eventually turned into days."

    "You consumed more reels than anyone in the entire world in one session."

    "You die from starvation and dehydration after an eternity of doomscrolling."

    "You were found dead with a phone on your hand, never seeing a single funny reel."

    "Game over."

    "Ending A: Doomscrolled Too Much"

    return

label dream:
    "You chose to get out of bed."

    "You yawned as you get out of bed, putting on your slippers one at a time."

    scene bg door

    play sound knock

    "You hear a knock on your door."

    x "Honey? Are you awake?"

    "A woman's voice is coming from behind the door."

    mc "Yea, I just woke up. I'll be right there."

    "You walk up to the door to open it."

    play sound door_open

    show arlecchino:
        zoom 0.5
        xalign 0.5
        yalign 0.5
    
    arlecchino "Happy Birthday, sweetie. How was your sleep?"

    mc "Thank you, Arlecchino. It was great, thanks for asking."

    arlecchino "Did you do your dailies yet?"

    mc "I have not, I should do that soon. Thanks for reminding me."

    arlecchino "Of course, can't miss a day. I'll go grab you your medicine as well."

    hide arlecchino

    "Arlecchino leaves your bedroom to grab your daily dose of medicine..."

    "Dr. Pepper."

    scene bg computer

    mc "Time to boot up my computer and do my dailies on"

    mc "Genshin Impact"

    mc "Honkai Star Rail"

    mc "Zenless Zone Zero"

    mc "Fire Emblem Heroes"

    mc "Wuthering Waves"

    mc "Arknights"

    mc "Arknights: Endfield"

    mc "Fate/Grand Order"

    mc "Goddess of Victory: Nikke"

    mc "Reverse: 1999"

    mc "AFK Journey"

    mc "Raid: Shadow Legends"

    mc "And 50 other more gacha games"

    scene bg black

    "After a couple of hours of finishing your dailies and drinking your gallon of Dr. Pepper, it was time for you to start your day."

    scene bg bedroom

    "Your stomach growls as it only consumed only Dr. Pepper."

    mc "Boy, I am sure hungry."

    show arlecchino:
        zoom 0.5
        xalign 0.5
        yalign 0.5

    arlecchino "Don't worry, darling. I just cooked you some food."

    hide arlecchino

    scene bg black

    "Arlecchino presents you her cooking."

    show steak:
        xalign 0.5
        yalign 0.5

    "A succulent, juicy steak."

    mc "Wow, thank you so much!"

    mc "Itadakimasu!"

    hide steak

    play sound eating

    "You proceed to grab a bite of the steak."

    mc "Mmm! This taste..."

    scene bg black

    play sound death

    "You collasped all of a sudden."

    "You forgot Arlecchino cooks her steak raw."

    "Game Over."

    $ persistent.endingB = True

    "Ending B: Poisoned by your wife."

    return

label realistic:
    "You suddenly woke up, breathing heavily."

    mc "{i}I knew that was too good to be true.{/i}"

    "You looked over to your right. Your Arlecchino dakimakura is laying next to you."

    "You sighed and stood up to open up your blinds."

    scene bg animebedroom

    mc "Today is my birthday and yet..."

    mc "no one to celebrate it with."

    "Today is your day off from being a corporate slave."

    "You decided to use your yearly one day off today but didn't planned anything."

    "You pulled out your phone to doomscrolled a bit to look for something to do."

    pause(3.0)

    "You stumbled upon an ad that happened to open today near your place."

    mc "Oh, today this place just opened. It's also near me. What a coincidence."

    mc "Wouldn't mind checking it out, got nothing else to do."

    scene bg black

    "You went to get ready by showering and dressing up in your favorite Suisei shirt, favorite Ina jacket, favorite baggy black pants, and favorite tote bag."

    "You put in your shoes and went out the door."

    jump outside

label outside:
    scene bg city

    play music city volume 0.2 loop

    mc "{i}The cicadas are louder than ever.{/i}"

    mc "{i}I imagined by November, it would get colder but the fact it is still hot for cicadas to be making these noises is geniunely crazy.{/i}"

    "You walk your way to the place and see a couple of high schoolers having fun."

    "You wish a bit to have someone to hang out with."

    scene bg black

    mc "Welp, I guess this is the place."

    scene bg cafe_entrance

    if retries == 0:
        mc "Why did I even choose to go here of all places to be for my birthday?"

        mc "Oh, whatever. Better than staying at home doing dailies all day."

        "You entered the maid cafe despite your embarrassment of going in alone."

        stop music

        scene bg black

    # elif retries == 1:
        

    jump maid

label maid:
    scene bg cafe_hall

    play music cafe_bg_1 volume 0.1 fadein 1.0 loop 

    if retries == 0:
        "The moment you walked in, you immediately get blasted by the Blend S opening but something is different about it."

        "You take a couple of seconds looking around the cafe, admiring its decoration."

        mc "{i}It honestly doesn't look too bad.{/i}"

        "You don't see any customers in the cafe. You wonder if it's because of the music or that it just opened."

        x "Welcome, sir, to our finest Maid cafe establishment you will experience."

        "You hear a man's voice to your right."

        show kevin:
            zoom 0.3
            xalign 0.5
            yalign 1.5

        kevin "How many people?"

        "You look around you."

        mc "Just... one, please, Kevin."

        mc "{i}How did I know his name when he didn't say it?{/i}"

        "Kevin grabs one menu from the host table."

        kevin "Alright, follow me to your seat."

        hide kevin

        "He starts walking inside at a fast pace and you start following him, trying to match his speed."

        stop music fadeout 1.0

        # play music cafe_bg_2 volume 0.1 fadein 1.0 loop

        scene bg cafe_seat

        "You sat down at the booth area where in front of you is the stage where you assume the maids perform."
        
        show kevin:
            zoom 0.3
            xalign 0.5
            yalign 1.5

        kevin "Here's the menu, sir. Pick which maid you would love to accompany you for your stay."

        hide kevin

        mc "Thank yo-"

        "And before you can say your thanks, he was already gone."

        mc "{i}Okay, weird... let's see what's on the menu today.{/i}"

        jump menu_scene

label menu_scene:
    if retries > 0:
        pause(1.0)
        mc "{i}Wait, wasn't there supposed to be someone here?{/i}"

    call screen menu

    $ selected_maid = _return
    $ menu_removed.append(selected_maid)

    jump expression selected_maid

label ant:
    "You have chosen Ant as your maid."


label charley:
    "You have chosen Charley as your maid."

label parker:
    "You have chosen Parker as your maid."

label abot:
    "You have chosen Abot as your maid."

label sebastian:
    "You have chosen Sebastian as your maid."

label ending_cafe:
    