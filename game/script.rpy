# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ant = Character("Ant")
define charley = Character("Charley")
define parker = Character("Parker")
define abot = Character("Abot")
define seb = Character("Sebastian")
define mc = Character("Anthony")

define arlecchino = Character("Arlecchino")

# The game starts here.

label start:    
    "Today is Novemeber 9th, 2026. A very special day for a certain someone."

    "It is your birthday. You've been looking forward this ever since he planned a whole hangout session with your friends."

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

    show bg door

    play sound knock

    "You hear a knock on your door."

    "Honey? Are you awake?"

    "A woman's voice is coming from behind the door."

    mc "Yea, I just woke up. I'll be right there."

    "You walk up to the door to open it."

    play sound door_open

    show arlecchino
    
    arlecchino "Happy Birthday, sweetie. How was your sleep?"

    mc "Thank you, Arlecchino. It was great, thanks for asking."

    arlecchino "Did you do your dailies yet?"

    mc "I have not, I should do that soon. Thanks for reminding me."

    arlecchino "Of course, can't miss a day. I'll go grab you your medicine as well."

    hide arlecchino

    "Arlecchino leaves your bedroom to grab your daily dose of medicine..."

    "Dr. Pepper."

    show bg computer

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

    hide bg computer

    "After a couple of hours of finishing your dailies and drinking your gallon of Dr. Pepper, it was time for you to start your day."

    show bg bedroom

    "Your stomach growls as it only consumed only Dr. Pepper."

    mc "Boy, I am sure hungry."

    show arlecchino

    arlecchino "Don't worry, honey! I just cooked you some food."

    "Arlecchino presents you her cooking."

    "A succulent, juicy steak."

    mc "Wow, thank you so much!"

    "You proceed to grab a bite of the steak."

    mc "Mmm! This taste..."

    hide bg bedroom

    "You collasped all of a sudden"

    "You forgot Arlecchino cooks her steak raw."

    "Game Over."

    "Or... is it?"

    jump realistic

label realistic:
    "You suddenly woke up, breathing heavily."

    mc "{i}I knew that was too good to be true.{/i}"

    "You looked over to your right. Your Arlecchino dakimakura is laying next to you."

    "You sighed and stood up to open up your blinds."

    show bg animebedroom

    mc "Today is my birthday and yet..."

    mc "no one to celebrate it with."

    "Today is your day off from being a corporate slave."

    "You decided to use your yearly one day off today but planned anything."

    "You pulled out your phone to doomscrolled a bit to look for something to do."

    "You stumbled upon an ad that happened to open today near your place."

    mc "Oh, today this place just opened. It's also near my place."

    mc "Wouldn't mind checking it out, got nothing else to do."

    hide bg animebedroom

    "You went to get ready by showering and dressing up in your favorite Suisei shirt, favorite Ina jacket, favorite baggy black pants, and favorite tote bag."

    "You put in your shoes and went out the door."

    jump outside

label outside:
    show bg city

    play music city volume 0.2 loop

    mc "{i}The cicadas are louder than ever.{/i}"

    mc "{i}I imagined by November, it would get colder but the fact it is still hot for cicadas to be making these noises is geniunely crazy.{/i}"

    "You walk your way to the place and see a couple of high schoolers having fun."

    "You wish a bit to have someone to hang out with."

    hide bg city

    mc "Welp, I guess this is the place."

    show bg cafe_entrance

    mc "Why did I even choose to go here of all places to be for my birthday?"

    mc "Oh, whatever. Better than staying at home doing dailies all day."

    hide bg cafe_entrace

    jump maid:

label maid:
    