# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ant = Character("Ant")
define charley = Character("Kazuma Kiryu")
define parker = Character("Ali G")
define abot = Character("Abot")
define seb = Character("Sebastian")
define mc = Character("Anthony")
define kevin = Character("Kevin")

define arlecchino = Character("Arlecchino")
define x = Character("?")

default persistent.retries = 0
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

image bg notification:
    "images/bg notification.png"
    xysize (1920, 1080)
    fit "cover'"

image bg black:
    "images/bg black.jpg"
    xysize (1920, 1080)
    fit "cover"


image abot:
    "characters/ABot/abot.png"
    xalign 0.5
    yalign 0.5

image abot sad:
    "characters/ABot/abot sad.png"
    xalign 0.5
    yalign 0.5

image abot speak:
    "characters/Abot/abot speak.png"
    xalign 0.5
    yalign 0.5

image ant:
    "characters/Ant/ant.png"
    xalign 0.5
    yalign 0.5

image charley:
    "characters/Charley/charley maid.png"
    xalign 0.5
    yalign 0.5

image charley hearts:
    "characters/Charley/charley hearts.png"
    xalign 0.5
    yalign 0.5

image charley load:
    "characters/Charley/charley load.png"
    xalign 0.5
    yalign 0.5

image charley points:
    "characters/Charley/charley points.png"
    xalign 0.5
    yalign 0.5

image charley stares:
    "characters/Charley/charley stares.png"
    xalign 0.5
    yalign 0.5

image parker:
    "characters/Parker/parker peace.png"
    xalign 0.5
    yalign 0.5

image parker points:
    "characters/Parker/parker points.png"
    xalign 0.5
    yalign 0.5

# The game starts here.

label start:
    if persistent.retries > 0:
        scene bg cafe_seat
        $ persistent.menu_removed = []
        jump menu_scene
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

    jump cafe_entrance

label begin_cafe:
    if persistent.retries > 0:
        scene bg black
        play sound rezero_return
        pause (1.0)

    scene bg cafe_entrance

    mc "Why did I even choose to go here of all places to be for my birthday?"

    mc "Oh, whatever. Better than staying at home doing dailies all day."

    "You entered the maid cafe despite your embarrassment of going in alone."

    stop music

    scene bg black

    jump maid

label maid:
    scene bg cafe_hall

    play music cafe_bg_1 volume 0.1 fadein 1.0 loop 

    "The moment you walked in, you immediately get blasted by the Blend S opening but something is different about it."

    if persistent.retries > 0:
        mc "{i}Why do I feel like I've heard this before?{/i}"

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

    jump menu_scene

label menu_scene:
    mc "{i}Okay, weird... let's see what's on the menu today.{/i}"

    mc "{i}Okay, why the fuck is the menu just a piece of paper?{/i}"

    if persistent.retries > 0:
        pause(1.0)
        mc "{i}Wait, wasn't there supposed to be someone here?{/i}"

    call screen menu

    $ selected_maid = _return
    $ persistent.menu_removed.append(selected_maid)

    jump expression selected_maid

label abot:
    "You have chosen Abot as your maid."

    "As you wait for your maid, you comtemplate on your baka, chud, lonely life and using a maid cafe as an excuse to feel less lonely."

    "You sighed in sadness."

    mc "{i}Where did I go wrong?{/i}"

    "You see a maid coming towards you."

    show abot

    mc "{i}Wow... he looks gorgeous.{/i}"

    hide abot
    show abot speak

    play sound "characters/ABot/ABotLine1.wav"

    abot "Hey, thanks for choosing me as your maid. I'll be here to serve any request you have today. Uh, what would you like to order?"

    hide abot 
    show abot

    menu:
        "Nans Lasanga":
            "You have chosen Nans Lasanga."
            mc "I\'ll have the Nans Lasanga."
        "Rice and Peas":
            "You have chosen... Rice and Peas?"
            mc "I\'ll have the Rice and Peas."
        "Fish and Chips":
            "You have opted for the jolly good Fish and Chips."
            mc "I\'ll have the Fish and Chips."

    hide abot
    show abot speak
    
    play sound "characters/ABot/ABotLine2.wav"

    abot "Very well. I shall get that ready for you, sir."

    hide abot

    scene bg black

    "You then proceed to wait what felt like eternity for your food."

    pause 5.0

    mc "{i}It does NOT take that long to make my food.{/i}"

    scene bg cafe_seat

    "You see your maid coming towards you with your food but looks very sad."

    show abot sad

    play sound "characters/ABot/ABotLine3alt.wav"

    abot "Uhm... here you go, sir. Uhh, sorry. I lost my 50/50 and it... kinda shrunk."

    mc "{i}Ah. No wonder it looked so small. I thought I was imagining things.{/i}"

    mc "{i}No matter. Maybe the food is just to die for, you know? Gotta keep a positive mindset.{/i}"

    menu:
        mc "{i}But, how should I reply to him?{/i}"

        "Nod":
            "You nod your head at him."

            "He looks confused and nods back."

            "Then, there's just an awkward silence."

            "Bad option."

        "Spread Wings":
            "You spread out your arms like they're wings."

            hide abot
            show abot

            "He looks confused but somehow it made him feel better."

            "Good option."

        "Be Intimidating":
            "You stare at him."

            hide abot sad

            "He starts sweating and feeling uncomfortable that he left."

            "Bad option."
    
    hide abot

    "You grab a bite of your food but hesitates for a bit because of your dream."

    mc "{i}It's... an interesting taste profile. I'll give them that.{/i}"

    "After some time, you somehow ate it all."

    "As you're about to leave to pay for your check, the maid comes to your table."

    play sound "characters/ABot/ABotLine4.wav"

    show abot speak

    abot "Hey, sir! I also happen to know it's your birthday and I just want to say happy birthday! Hope it's going great."

    mc "Aww, thanks!"

    mc "{i}...how does he know it's my birthday?{/i}"

    mc "{i}Man, this place keeps getting weirder by the second.{/i}"

    mc "{i}At least someone wished me a happy birthday so that made me happy.{/i}"

    play sound "characters/Abot/ABotLine5.wav"

    abot "Well, sir. This is goodbye for now. I hope you come again though. Byeee!"

    mc "Bye! It was nice having you as my maid."

    hide abot

    call ending_cafe

    "Ending ABot"

    return

label ant:
    "You have chosen Ant as your maid."

    "As you wait for your maid, you comtemplate on your baka, chud, lonely life and using a maid cafe as an excuse to feel less lonely."

    "You sighed in sadness."

    mc "{i}Where did I go wrong?{/i}"

    "You see a maid(?) coming towards you."

    show ant

    play sound "characters/Ant/maidline1.mp3"

    ant "H-Huh?... You chose me? Well it seems like you have good taste after all… You read the description so you know my name already, right? Good, this is embarrassing as it is…"
    
    play sound "characters/Ant/maidline2.mp3"

    ant "What? No, it\'s not like I wanted you to choose me or anything… but thanks anyway, I guess…"

    play sound "characters/Ant/maidline3.mp3"

    ant "Alright, so, are you gonna tell me what you want to eat or not, moron?"

    menu:
        "Nans Lasanga":
            "You have chosen Nans Lasanga."
            mc "I\'ll have the Nans Lasanga."
        "Rice and Peas":
            "You have chosen... Rice and Peas?"
            mc "I\'ll have the Rice and Peas."
        "Fish and Chips":
            "You have opted for the jolly good Fish and Chips."
            mc "I\'ll have the Fish and Chips."

    play sound "characters/Ant/maidline4.mp3"
    ant "You seriously ordered that? I mean, if that\'s what you want, dumbass…"

    scene bg black

    "You then proceed to wait what felt like eternity for your food."

    pause 5.0

    mc "{i}It does NOT take that long to make my food.{/i}"

    scene bg cafe_seat

    "You see your maid coming towards you for your food."

    show ant

    play sound "characters/Ant/maidline5.mp3"
    ant "Sorry for the wait, here\'s your order- What? You want me to do what to your food? Spit in it? I… What the hell is wrong with you?... Sigh… I don\'t do this for just anyone, you know that? Consider yourself lucky."

    ant "{i}Spits on your food{/i}"

    menu:
        mc "{i}How do I even reply to that...?{/i}"

        "Sing a Beautiful Tune":
            "You start singing to Bibbidiba by Hoshimachi Suisei for whatever reason."

            "He looks at you weirdly but you can see his ears blushing."

            "Good option."

        "Be Intimidating":
            "You stare at him intensely."

            "He looks at you disgustingly and bitch slaps you."

            "Bad option."

        "Do a Somersault":
            "For whatever reason, your body starts moving on its own."

            "You stand on top of the table and did a somersault for the first time."

            "He stares at you in awe, not sure what to make of that."

            "Bad option."
    
    hide ant

    "You grab a bite of your food but hesitates for a bit because of your dream."

    mc "{i}It's... an interesting taste profile. I'll give them that.{/i}"

    "After some time, you somehow ate it all."

    "As you're about to leave to pay for your check, the maid comes to your table."

    show ant

    play sound "characters/Ant/maidline7.mp3"

    ant "Despite the sick and twisted thing you just asked me to do… I couldn\'t let a birthday boy as cute as you go without some sort of celebratory treat, right? Yeah, yeah, wipe that smile off your face, freak…"

    pause 1.0

    mc "...thanks??"

    mc "{i}...how does he know it's my birthday?{/i}"

    mc "{i}Man, this place keeps getting weirder by the second.{/i}"

    mc "{i}At least someone wished me a happy birthday so that made me a bit happy despite the tsundere he is.{/i}"

    play sound "characters/Ant/maidline8.mp3"

    ant "You\'re leaving already?-- I mean, bye or whatever. It\'s not like I want you to come back or anything, dummy…"

    mc "Uhm, yea, sorry. I-It was nice having you as my maid! Haha.."

    hide ant

    call ending_cafe

    "Ending Ant"

    show ant

    play sound "characters/Ant/maidline9.mp3"

    pause 12.0

    return


label charley:
    "You have chosen Charley as your maid."

    "As you wait for your maid, you comtemplate on your baka, chud, lonely life and using a maid cafe as an excuse to feel less lonely."

    "You sighed in sadness."

    mc "{i}Where did I go wrong?{/i}"

    "You see a maid coming towards you."

    show charley

    play sound "characters/Charley/Introduction.mp3" # play voice 1
    
    charley "yōkoso。私wo選ndeitadaki、本当niarigatōgozaimasu。"

    mc "{i}I have no clue what he just said to me.{/i}"

    mc "{i}Is there English subtitles for this?{/i}"

    "A mysterious screen pops in front of you."

    hide charley
    scene bg notification
    play sound notification volume 0.5

    "You have been granted Google Translation English Subtitles (SSR)."

    mc "{i}Oh sweet.{/i}"

    scene bg cafe_seat

    show charley

    play sound "characters/Charley/Introduction.mp3"

    charley "Welcome. Thank you very much for choosing me."

    show charley hearts
    play audio magic

    play audio "characters/Charley/Name.mp3"

    charley "My name is Kiryu, Dragon of Dojima."

    show charley

    play sound "characters/Charley/Order.mp3"

    charley "What would you like to eat?"

    # menu
    menu:
        "Nans Lasanga":
            "You have chosen Nans Lasanga."
            mc "I\'ll have the Nans Lasanga."
        "Rice and Peas":
            "You have chosen... Rice and Peas?"
            mc "I\'ll have the Rice and Peas."
        "Fish and Chips":
            "You have opted for the jolly good Fish and Chips."
            mc "I\'ll have the Fish and Chips."

    show charley points

    play sound "characters/Charley/Acknowledges_1.mp3"

    charley "That is an excellent choice."

    show charley load

    play sound "characters/Charley/Acknowledges_2.mp3"

    charley "I will be right back."

    hide charley

    scene bg black

    "You then proceed to wait what felt like eternity for your food."

    pause 5.0

    mc "{i}It does NOT take that long to make my food.{/i}"

    scene bg cafe_seat

    "You see your maid coming towards you for your food."

    show charley stares

    "He gives you your food and stares at you for a period of time."

    # birdtime menu
    menu:
        mc "{i}How do I reply to that?{/i}"

        "Spread Wings":
            "You spread your arms out like they're wings."

            "Kiryu looks at you weirdly."

            "You feel the embarrassment rushing to you, you lowered your wings."

            "Bad option."

        "Be Intimidating":
            "You stare at Kiryu intensely like the thousand yard stare."

            show charley stares
            "Kiryu stares back."

            "You stare at his eyes even more intensely like it was the only thing that mattered right now."

            "Kiryu stares at you with his sharp eyes, not blinking once."

            "You both are communicating each other with your stares and acknowledges each other as fellow brethrens."

            "Good option."

        "Dance":
            play sound dance
            "You start pulling out the Fortnite dance right in front of him."

            show charley points
            "Kiryu hits you back with an even harder and more cooler dance to counter."

            "You felt defeated from the sheer aura of his dance moves."

            mc "{i}I-Impossible. How can he be so cool?{/i}"

            "Bad option."
    
    hide charley

    "You grab a bite of your food but hesitates for a bit because of your dream."

    mc "{i}It's... an interesting taste profile. I'll give them that.{/i}"

    "After some time, you somehow ate it all."

    "As you're about to leave to pay for your check, the maid comes to your table."

    show charley

    play sound "<to 3.2>characters/Charley/Birthday.mp3"

    charley "I heard it's your birthday."

    show charley hearts
    play audio magic

    play audio "<from 3.21>characters/Charley/Birthday.mp3"

    charley "Happy birthday."

    mc "Thank you, my brother."

    mc "{i}...how does he know it's my birthday?{/i}"

    mc "{i}Man, this place keeps getting weirder by the second.{/i}"

    mc "{i}At least someone wished me a happy birthday so that made me a bit happy despite the tsundere he is.{/i}"

    show charley stares

    play sound "characters/Charley/Goodbye_1.mp3"

    charley "Please come again."

    show charley hearts
    play audio magic

    play audio "characters/Charley/Goodbye_2.mp3"

    charley "See you later, Anthony."

    mc "Thanks, my brother. We shall meet again."

    hide charley # hide char

    call ending_cafe

    "Ending Charley" # end char

    return

label parker:
    "You have chosen Parker as your maid."

    "As you wait for your maid, you comtemplate on your baka, chud, lonely life and using a maid cafe as an excuse to feel less lonely."

    "You sighed in sadness."

    mc "{i}Where did I go wrong?{/i}"

    "You see a maid coming towards you."

    show parker # char

    play sound "characters/Parker/Introduction.mp3" # play voice 1

    # dialogue 1
    parker "wah gwan, bruv. thank u for choosing me, Ali G, to be ur mate today, innit."
    
    # filler char and dialogue and voice

    show parker points

    play sound "characters/Parker/Filler.mp3" # play voice 2

    parker "make sure u remember to stream my new song. ♪{i}Who is I, Mm, Who is I, Uh, Who is I{/i}♪"

    # dialogue 2
    show parker

    play sound "characters/Parker/Order.mp3"

    parker "yo anyways bruv, what u like to eat, yknow? u feel me, innit?"

    # menu
    menu:
        "Nans Lasanga":
            "You have chosen Nans Lasanga"
            mc "I\'ll have the Nans Lasanga."
        "Rice and Peas":
            "You have chosen... Rice and Peas?"
            mc "I\'ll have the Rice and Peas."
        "Fish and Chips":
            "You have opted for the jolly good Fish and Chips."
            mc "I\'ll have the Fish and Chips."

    # dialogue and voice acknowledges order (3)

    play sound "characters/Parker/Acknowledge.mp3"
    
    parker "booyahkasha, i is gonna bring u da best food __ used to make. rest in peace __, had the biggest {b}rack{/b}."

    hide parker

    # hide char

    scene bg black

    "You then proceed to wait what felt like eternity for your food."

    pause 5.0

    mc "{i}It does NOT take that long to make my food.{/i}"

    scene bg cafe_seat

    "You see your maid coming towards you for your food."

    # show char
    show parker

    # dialogue and voice 4, brings order
    play sound "characters/Parker/Return.mp3"

    parker "wah gwan, i is back, yknow what im sayin? u know i put a little bit of, yknow, i puttin' a little bit of that {b}tree{/b}, innit, yknow what i mean, that little bit of {b}tree{/b} in that food, bruv, so. just, just sit back n enjoy it, bruv, yknow what im sayin, yknow what i sayin?"
    # birdtime menu
    menu:
        mc "{i}How do I even reply to that...?{/i}"

    
    hide # hide char

    "You grab a bite of your food but hesitates for a bit because of your dream."

    mc "{i}It's... an interesting taste profile. I'll give them that.{/i}"

    "After some time, you somehow ate it all."

    "As you're about to leave to pay for your check, the maid comes to your table."

    show # show char

    # dilogue and voice 5, birthday

    mc "...thanks??"

    mc "{i}...how does he know it's my birthday?{/i}"

    mc "{i}Man, this place keeps getting weirder by the second.{/i}"

    mc "{i}At least someone wished me a happy birthday so that made me a bit happy despite the tsundere he is.{/i}"

    # dialogue and voice 6, goodbye

    mc "Uhm, yea, sorry. I-It was nice having you as my maid! Haha.."

    hide # hide char

    call ending_cafe

    "Ending " # end char

    return

```
label sebastian:
    "You have chosen Sebastian as your maid."

    "As you wait for your maid, you comtemplate on your baka, chud, lonely life and using a maid cafe as an excuse to feel less lonely."

    "You sighed in sadness."

    mc "{i}Where did I go wrong?{/i}"

    "You see a maid(?) coming towards you."

    show # char

    play sound "characters" # play voice 1

    # dialogue 1
    
    # filler char and dialogue and voice

    play sound "characters" # play voice 2

    # dialogue 2

    # menu
    menu:
        "Nans Lasanga":
            "You have chosen Nans Lasanga"
            mc "I\'ll have the Nans Lasanga."
        "Rice and Peas":
            "You have chosen... Rice and Peas?"
            mc "I\'ll have the Rice and Peas."
        "Fish and Chips":
            "You have opted for the jolly good Fish and Chips."
            mc "I\'ll have the Fish and Chips."

    # dialogue and voice acknowledges order (3)

    # hide char

    scene bg black

    "You then proceed to wait what felt like eternity for your food."

    pause 5.0

    mc "{i}It does NOT take that long to make my food.{/i}"

    scene bg cafe_seat

    "You see your maid coming towards you for your food."

    # show char
    show 

    # dialogue and voice 4, brings order

    # birdtime menu
    menu:
        mc "{i}How do I even reply to that...?{/i}"

    
    hide # hide char

    "You grab a bite of your food but hesitates for a bit because of your dream."

    mc "{i}It's... an interesting taste profile. I'll give them that.{/i}"

    "After some time, you somehow ate it all."

    "As you're about to leave to pay for your check, the maid comes to your table."

    show # show char

    # dilogue and voice 5, birthday

    mc "...thanks??"

    mc "{i}...how does he know it's my birthday?{/i}"

    mc "{i}Man, this place keeps getting weirder by the second.{/i}"

    mc "{i}At least someone wished me a happy birthday so that made me a bit happy despite the tsundere he is.{/i}"

    # dialogue and voice 6, goodbye

    mc "Uhm, yea, sorry. I-It was nice having you as my maid! Haha.."

    hide # hide char

    call ending_cafe

    "Ending " # end char

    return
```
label ending_cafe:
    scene bg cafe_hall

    "You went to go pay for your food of $100."

    mc "{i}Never coming here again.{/i}"

    "As you walk out of the maid cafe, you feel your heartbeating so fast."

    scene bg black

    "You then collasped in front of the exit."

    "You can't feel your body at all."

    "It just given up on you for no reason."

    mc "{i}What's happening to me?!{/i}"

    mc "{i}Am I going to..{/i}"

    play sound death

    "You died."

    $ persistent.retries += 1