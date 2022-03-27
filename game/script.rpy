# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define T = Character("Theo", image="theo")
define A = DynamicCharacter("a_name", image="ariadne")
define V = Character("Vinny")
define I = Character("Icarus")
define F = Character("Francis")
define E = Character("Eduardo")

define Classmate1 = Character("Classmate 1")
define Classmate2 = Character("Classmate 2")

# Character images
#image side theo happy = ""
#image side theo neutral = ""
#image side theo sad = ""
#image side theo angy = ""
#image side theo shocked = ""

# Pronoun variables
default they = "they"
default them = "them"
default their = "their"
default theyre = "they're"

# Stats
default himbully = 10

# Other variables
define toy = "My Little Pony"
define verb = ""

# Verb modification function for pronouns
init python:
    def verbMod(verbThey, verbHeShe):
        if (they == "they"):
            return verbThey
        else:
            return verbHeShe

# ---------- The game starts here. ----------

label start:
    show T neutral
    menu:
        "Hey, I'm Theo. What pronouns should I use?"

        "He/him":
            $ they = "he"
            $ them = "him"
            $ their = "his"
            $ theyre = "he's"
        "She/her":
            $ they = "she"
            $ them = "her"
            $ their = "her"
            $ theyre = "she's"
        "They/them":
            $ they = "they"

    T neutral "Cool, see you around I guess."

label sceneBeforeMaze:
    scene black
    "A class of middle schoolers loiters around the entrance to a giant corn maze. Their teachers are taking attendance."

    Classmate1 "This is such a dumb field trip."

    T neutral "A corn maze? More like a corn lame."
    T happy "teehee"

    "Theo’s posse laughs. They are clumped together at the back of the group."
    Classmate2 "Speaking of lame, look at that! What a loser. Nobody plays with dolls anymore."

    "The outcast hears them and turns away. They are alone."

    menu:
        "Yeah, that’s stupid. At least get the Transformers Toys Heroic, not Playskool.":
            $ himbully -= 1
            $ toy = "Transformers"

        "Yeah, that’s stupid. Gen 4 of My Little Pony is so much better than Gen 3.":
            $ himbully -= 1

        "I don’t care about what losers do.":
            jump sceneEnterMaze

    Classmate1 "Why do you know about [toy]?"

    T angy "What? No, I don’t... I was just making it up."
    "Theo sighs in relief when [their] friends drop that line of questioning. [they!c] would never admit to liking something as corny as [toy]."

label sceneEnterMaze:

    "Inside the corn maze, Theo takes a wrong left and loses [their] classmates."

    T angy "What the crap? Did those posers ditch me?"

    $ verb = verbMod("hope", "hopes")
    "Theo is sure they’re just around the corner. [they!c] [verb] [their] friends haven’t noticed [theyre] missing. It would be embarrassing to get lost in such a small maze."
    $ verb = verbMod("realize", "realizes")
    "Every fork looks the same. Theo begins to feel dizzy. By the time [they] [verb] [theyre] hopelessly lost, the walls have ***********************corn maze background"

    $ a_name = "???"
    A "Are you lost? What a cat-tastrophe! Nya-ha-ha!"

    T shock "W-Who’s there?"

    show A happy
    A "Hi there! You look like you need some help!"

    T angy "I don’t need help!"

    A "Luckily for you, I’m a generous feline!"
    show A neutral
    A "The sooner you’re gone, the better."
    show A happy
    A "There’s Icarus flying over us now. Icarus! Come whisk-er this trespasser away!"

    "Theo looks up. A white winged figure briefly silhouettes against the blue sky. A distant response floats down."

    show A shock

    I "What am I, Ariadne, your personal chauffeur?"
    $ a_name = "Ariadne"

    show A angy
    A "You–hiss!"
    show A neutral

    "Ariadne grooms herself with a huff."

    show A happy
    A "That lazy bum. Now it’s up to me to help you out. Stay paws-itive, you’ll be home in no time!"

    "Theo isn’t sure whether [theyre] hallucinating. A flying person and a talking cat? The sun must’ve gotten to [them]. Perhaps this is all a fever dream and [theyre] going to wake up any minute."
    "Regardless of whether this is real, the cat is waiting for Theo’s response."

    menu:
        "Fine. Anything as long as I don’t have to hang out with weirdos too long.":
            $ himbully -= 1

        "I can find the way out by myself.":
            show A happy
            A "You have no choice but to follow me!"
            jump yarn

        "I don’t need any help from you weirdos.":
            $ himbully -= 1

    show A neutral
    A "Watch who you’re calling a weirdo."
    show A happy
    A "Anyway, you have no choice but to follow me!"

label yarn:
    show A neutral yarn
    A "Without this yarn, you have no way of tracking where you’ve come from in the labyrinth. And the only one who can use this yarn… "
    show A happy yarn
    A "... is me-ow!"
    show A happy

    "Theo scoffs. *** However, one thing sticks out to [them]."

    T neutral "Labyrinth? This is a corn maze."

    A "How a-mew-sing! You seem to have gotten turned around without even trying. That’s a fresh talent!"
    A "Follow me, lost human!"
    hide A

# GENERIC LABYRINTH
    $ verb = verbMod("trudge", "trudges")
    "It’s hard to admit, but Ariadne is right. Theo has no idea which direction is out. [they!c] trudge after Ariadne as she rolls out her yarn ball."

label miniSnailMaze:

    "Soon, they come across a curious square table. The top of it is deeply grooved in grid-like patterns, forming a miniature maze. Ariadne leaps atop the edge of the maze and peers inside it."

    show A happy at right
    A "Eduardo? Is that you?"

    "Theo follows Ariadne’s line of sight to spot Eduardo within the maze. A trail of slime marks Eduardo’s pathing, which double-backs and loops around. He is having difficulty escaping the maze because he is a tiny snail."
    "He is too small to see that he is only a few turns away from the exit."

    E "Eh… eh…. ehhh-xaust-ehhhhd…"

    show A sad
    A "Oh no, you poor thing."

    "Ariadne cranes her neck to figure out the solution to the table-maze, but she is too short to see the entire thing at once. She points a paw at Theo."

    show A neutral
    A "You…"

    T neutral "Theo."

    show A happy
    A "...Theo, be a kitten and help him out!"

    menu: # stat checks for these choices?? → tulasi help
        "Help Eduardo solve the maze.":
            $ himbully += 1
            "Theo studies the maze."
            T neutral "Go forward until you hit the wall, then take two rights and a left."
            E "W… Whoa…"
            "Theo gets the impression that Eduardo is grateful."

        "\"Looks lame.\"":
            E "W… Ehh…"
            "Theo gets the impression that Eduardo is tired and sad."
            show A neutral
            "Ariadne studies Theo with an unreadable expression."
            show A happy
            A "Let’s not paws for too long!"

        "Use a block to wall Eduardo into a box.":
            $ himbully -= 1
            E "W… Wehh!"
            "Theo gets the impression that Eduardo is scared."
            show A angy
            A "That’s not very mice!"
            "Ariadne uses a paw to bat your block away from Eduardo."
            show A neutral
            A "Let’s not paws for too long."
            jump afterSnail

    show A neutral

    "Ariadne studies Theo with an unreadable expression."

    show A happy
    A "Let’s not paws for too long!"
    hide A

label afterSnail:

    "Theo and Ariadne double back on themselves several times. Fortunately, Ariadne’s yarn allows them to retrace their steps and try a different route."

    show A happy at center
    A "Meow, don’t get the wrong idea. I do know where we are going. However, the labyrinth shifts around every so often, so you can never memorize a path for the next day!"

    T neutral "Huh? You said you know where you’re going, but also that you don’t know any paths."

    A "Nya-ha-ha! It’s never meow-notonous!"
    A "The labyrinth is a great retirement spot."

label endGame:
    return
