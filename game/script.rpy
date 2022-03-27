# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define T = Character("Theo", image="theo")
define A = DynamicCharacter("a_name", image="ariadne")
define V = DynamicCharacter("v_name", image="vinny")
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
default himbully = 0

# Other variables
define toy = "My Little Pony"
define verb = ""
define snailChoice = 0

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

    show A happy at left
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
            $ snailChoice += 1
            "Theo studies the maze."
            T neutral "Go forward until you hit the wall, then take two rights and a left."
            E "W… Whoa…"
            "Theo gets the impression that Eduardo is grateful."
            show A neutral

        "\"Looks lame.\"":
            E "W… Ehh…"
            show A neutral
            "Theo gets the impression that Eduardo is tired and sad."

        "Use a block to wall Eduardo into a box.":
            $ himbully -= 1
            $ snailChoice -= 1
            show A neutral
            E "W… Wehh!"
            "Theo gets the impression that Eduardo is scared."
            show A angy
            A "That’s not very mice!"
            "Ariadne uses a paw to bat your block away from Eduardo."
            show A neutral
            A "Let’s not paws for too long."
            jump afterSnail

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
    hide A

label vinnyPartOne:

    "Theo and Ariadne emerge into a small clearing. In the center of it sits a strange creature. Theo can only describe the creature as some sort of cow-centaur with a nerd torso. They are everything Theo dislikes."

    show V sad at right

    "When they speak, their voice is slow and surprisingly deep."

    $ v_name = "???"
    V "Only three views today… one less than yesterday. I’ll never be famous."

    show A shock at left
    A "Vinny, what have I told you about checking your views too often?"
    show A neutral

    $ v_name = "Vinny"
    V "I want to be a moo-vie star…"

    show A happy
    A "I promise, you’re famous to me! That one less viewer was only because Eduardo was stuck in a maze today, he didn’t mean to miss your stream."
    show A neutral

    "Vinny shakes his head and lows."

    show V angy
    V "Only my friends watch me… when will the world recognize my looo-minosity?"

    show A happy
    A "Soon, I’m paw-sitive! Now perk up, we have a trespasser today!"

    show V neutral
    V "Moo… a guest?"

    if himbully > 0:
        A "[their!c] name is Theo!"
    else:
        A "[their!c] name is Cleo!"
        T neutral "Theo."

    V "Theo… will you watch my vlogs?"

    menu: # NOTE depending on stats up til this point, restrict certain choices? Up to tulasi
        "I guess… if I’m stuck in this maze and have nothing else to do.":
            $ himbully += 1
            show V happy
            V "Wonderful, marvelous! Five regular moo-ers–I mean, viewers!"
            show A happy

        "Why?":
            show V shocked
            V "Why… why! It’s been so long since anybody asked me that question."
            "Vinny clears his throat with a great hacking cough."
            V "To become a star, of course. My dream is to spread a-moo-sement to the masses!"
            show A happy

        "Why would I ever watch a weirdo vlog?":
            $ himbully -= 1
            show A angy
            A "You can't call others weirdos!"
            show V neutral
            "Vinny draws himself up. His hair seems to puff up with his spirit."
            V "I am indeed a weirdo. And I’m proud of it!"
            show A neutral

        "Pineapples and cows are literally the most uncool thing I’ve ever seen.":
            $ himbully -= 2
            show A angy
            A "There’s nothing wrong with pineapples and cows together! Besides, Vinny’s only half cow!"
            show V neutral
            "Vinny draws himself up. His hair seems to puff up with his spirit."
            V "I am indeed half cow, like my brother. He was the Minotaur. I’m proud of it!"
            show A neutral

    show V neutral
    A "Regardless, Theo here got lost on a school trip. I’m leading [them] out of the labyrinth."

    T angy "Don’t say it in such an embarrassing way!"

    "Ariadne ignores Theo to address Vinny."

    show A happy
    if snailChoice == 1:
        A "Theo has some rough edges, but I’m confident that there’s a good person somewhere deep down there! [they!c] helped Eduardo out just now."
    elif snailChoice == 0:
        A "I’m not sure that Theo is the kind of viewer you want. [they!c] didn’t even help Eduardo out of the table-maze just now!"
    else:
        A "I’m not sure that Theo is the kind of viewer you want. [they!c] walled Eduardo into the table-maze just now!"

    show V shock
    V "Interesting…"
    show V neutral
    V "No matter your character, Theo, I’m glad you are escaping the labyrinth. You belong to your School Trip."

    show A happy
    A "It’s school trip, all lowercase!"
    show A neutral

    V "Right. I would help you, but…"
    show V sad
    V "Unfortunately, my line is bound to this labyrinth with a curse. I will never be able to leave. My only hope of becoming famous is my vlogging channel."
    show V neutral
    V "So I would really appreciate your views."
    show V sad
    V "Thanks for stopping by…"

    show A happy
    A "Anytime, Vinny! You know I don’t have any hobbies."
    hide A
    hide V

label icarusPartOne:

    "Theo is less skeptical that Ariadne is actually leading him out, after meeting Vinny."

    show A center
    A "You should know, Theo, that what I admire most about Vinny is that he’s not afraid to be himself. I wish more people would see that, so that he could achieve his goal."

    "Ariadne fluffs her tail thoughtfully."

    A "Also, neither Vinny nor his line is actually cursed. So don’t feel too bad for him."

    T shock "Then why does he stay in that one place?"

    show A neutral
    A "In reality, he is simply too tall for the doorways in this labyrinth."

    T neutral "Not too wide?"

    show A happy
    A "Nya-ha-ha! Don’t ask him that to his face, he’ll grow insecure about his body!"
    hide A

    "It is another few minutes before the winged person from the very beginning swoops in from above. Theo sighs. This is just one encounter after another."

    show I neutral at right
    I "You dimwits still tryna get out of here?"

    show A happy at left
    A "I don’t see you helping!"

    show I happy
    I "Hah. And waste more time with you, when I could be listening to {b}DEATH METAL{/b}?"
    show I neutral

    "Icarus cracks her knuckles. Permanent scowl lines frame her mouth. She narrows her eyes."

    show A neutral
    show I angy
    I "As if I would do anything so weak."
    show I neutral

    show A happy
    A "Did you watch Vinny’s vlog today?"

    show I angy
    I "Of course I did."

    menu:
        #(if watch, "i plan to watch it to"?)
        "\"You… watch Vinny’s vlog?\" Icarus does not seem the type.":
            $ himbully += 1
            show I happy
            I "You don’t?"

        "\"Boring.\"":
            show I neutral
            I "So are you."

        "\"Seems like a weakling thing to me.\"":
            $ himbully -= 1
            show I angy
            I "Bold words from a sprout!"

    show I neutral

    show A happy
    A "Have you come to help us, Icarus?"

    I "As if. And don’t ask me to, because I can leave whenever I want."

    A "Then why do you keep coming back?"

    show I angy
    I "I wouldn’t come here at all if I weren’t so bored!"
    show I neutral
    I "Whatever."
    I "Don’t mind me. Go on, this should be entertaining."

    "Icarus flies upwards, but the shadows of her wings remind Theo that she is watching." # * wHAT am i saying here icarus just gotta go
    "This time, Ariadne points out a direction to Theo and lets [them] lead the way. They make good progress."
    "The last doorway, however, is blocked by the desk of a professional frog. The nameplate on his desk says \"FRANCIS.\""

label frogBusinessman:

    F "Greetings, travelers. Please sit and have some tea; I always enjoy company between three and seven pm. What brings you to my den on this charming afternoon?"

label endGame:
    return
