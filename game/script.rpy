# Declare characters used by this game. The color argument colorizes the
# name of the character.
define T = Character("Theo", image="theo")
define A = DynamicCharacter("a_name", image="ariadne")
define V = DynamicCharacter("v_name", image="vinny")
define I = Character("Icarus", image="icarus")
define F = Character("Francis")
define E = Character("Eduardo")

define Classmate1 = Character("Classmate 1")
define Classmate2 = Character("Classmate 2")
define Teacher = Character("Teacher")

# Pronoun variables
default they = "they"
default them = "them"
default their = "their"
default theyre = "they're"

# Stats
default himbully = 0
define snailChoice = 0

# Other variables
define toy = "My Little Pony"
define verb = ""
define gift = ""
define ending = 0
define hasAri = 0

# Verb modification function for pronouns
init python:
    def verbMod(verbThey, verbHeShe):
        if (they == "they"):
            return verbThey
        else:
            return verbHeShe

# Images
image side theo happy = "images/theo_sprites/theo_happy.png"
image side theo neutral = "images/theo_sprites/theo_neutral.png"
image side theo sad = "images/theo_sprites/theo_sad.png"
image side theo angy = "images/theo_sprites/theo_angry.png"
image side theo shocked = "images/theo_sprites/theo_shocked.png"

image vinny happy = "images/vinny_sprites/vinny_clothed/vinny_clothed_happy.png"
image vinny neutral = "images/vinny_sprites/vinny_clothed/vinny_clothed_neutral.png"
image vinny sad = "images/vinny_sprites/vinny_clothed/vinny_clothed_sad.png"
image vinny shocked = "images/vinny_sprites/vinny_clothed/vinny_clothed_shocked.png"
image vinny happy2 = "images/vinny_sprites/vinny_naked/vinny_naked_happy.png"
image vinny neutral2 = "images/vinny_sprites/vinny_naked/vinny_naked_neutral.png"
image vinny sad2 = "images/vinny_sprites/vinny_naked/vinny_naked_sad.png"
image vinny shocked2 = "images/vinny_sprites/vinny_naked/vinny_naked_shocked.png"

image icarus happy = "images/icarus_sprites/icarus_happy.png"
image icarus neutral = "images/icarus_sprites/icarus_neutral.png"
image icarus angy = "images/icarus_sprites/icarus_angry.png"

image ariadne happy = "images/ariadne_sprites/ariadne_happy.png"
image ariadne neutral = "images/ariadne_sprites/ariadne_neutral.png"
image ariadne sad = "images/ariadne_sprites/ariadne_sad.png"
image ariadne angy = "images/ariadne_sprites/ariadne_angry.png"
image ariadne shocked = "images/ariadne_sprites/ariadne_shocked.png"

image ariadne yarn1 = "images/ariadne_sprites/ariadne_yarn/ariadne_yarn_happy.png"
image ariadne yarn2 = "images/ariadne_sprites/ariadne_yarn/ariadne_yarn_neutral.png"

# ---------- The game starts here. ----------

label start:
    T neutral "Hey, I'm Theo."
    menu:
        T "What pronouns should I use?"
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

    T neutral "Cool. See you around, I guess."

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
        "\"Yeah, that’s stupid. At least get the Transformers Toys Heroic, not Playskool.\"":
            $ himbully -= 1
            $ toy = "Transformers"

        "\"Yeah, that’s stupid. Gen 4 of My Little Pony is so much better than Gen 3.\"":
            $ himbully -= 1

        "\"I don’t really care about what losers do.\"":
            jump sceneEnterMaze

    Classmate1 "Why do you know about [toy]?"

    T angy "What? No, I don’t... I was just making it up."
    "Theo sighs in relief when [their] friends drop that line of questioning. [they!c] would never admit to liking something as corny as [toy]."

label sceneEnterMaze:

    scene bg cornmaze

    "Inside the corn maze, Theo takes a wrong left and loses [their] classmates."

    T angy "What the crap? Did those posers ditch me?"

    $ verb = verbMod("hope", "hopes")
    "Theo is sure they’re just around the corner. [they!c] [verb] [their] friends haven’t noticed [theyre] missing. It would be embarrassing to get lost in such a small maze."
    $ verb = verbMod("realize", "realizes")
    "Every fork looks the same. Theo begins to feel dizzy. By the time [they] [verb] [theyre] hopelessly lost, the walls have ***********************corn maze background"

    scene bg labyrinth
    with dissolve

    $ a_name = "???"
    A "Are you lost? What a cat-tastrophe! Nya-ha-ha!"

    T shocked "W-Who’s there?"

    show ariadne happy
    A "Hi there! You look like you need some help!"

    T angy "I don’t need help!"

    A "Luckily for you, I’m a generous feline!"
    show ariadne neutral
    A "The sooner you’re gone, the better."
    show ariadne happy
    A "There’s Icarus flying over us now. Icarus! Come whisk-er this trespasser away!"

    "Theo looks up. A white winged figure briefly silhouettes against the blue sky. A distant response floats down."

    show ariadne shocked

    I "What am I, Ariadne, your personal chauffeur?"
    $ a_name = "Ariadne"

    show ariadne angy
    A "You–hiss!"
    show ariadne neutral

    "Ariadne grooms herself with a huff."

    show ariadne happy
    A "That lazy bum. Now it’s up to me to help you out. Stay paws-itive, you’ll be home in no time!"

    "Theo isn’t sure whether [theyre] hallucinating. A flying person and a talking cat? The sun must’ve gotten to [them]. Perhaps this is all a fever dream and [theyre] going to wake up any minute."
    "Regardless of whether this is real, the cat is waiting for Theo’s response."

    menu:
        "\"Fine. Anything as long as I don’t have to hang out with weirdos too long.\"":
            $ himbully -= 1

        "\"I can find the way out by myself.\"":
            show ariadne happy
            A "You have no choice but to follow me!"
            jump yarn

        "\"I don’t need any help from you weirdos.\"":
            $ himbully -= 1

    show ariadne neutral
    A "Watch who you’re calling a weirdo."
    show ariadne happy
    A "Anyway, you have no choice but to follow me!"

label yarn:
    show ariadne yarn2
    A "Without this yarn, you have no way of tracking where you’ve come from in the labyrinth. And the only one who can use this yarn… "
    show ariadne yarn1
    A "... is me-ow!"

    "Theo scoffs. *** However, one thing sticks out to [them]."

    T neutral "Labyrinth? This is a corn maze."

    show ariadne happy
    A "How a-mew-sing! You seem to have gotten turned around without even trying. That’s a fresh talent!"
    A "Follow me, lost human!"
    hide ariadne

    $ verb = verbMod("trudge", "trudges")
    "It’s hard to admit, but Ariadne is right. Theo has no idea which direction is out. [they!c] [verb] after Ariadne as she rolls out her yarn ball."

label miniSnailMaze:

    scene black

    "Soon, they come across a curious square table. The top of it is deeply grooved in grid-like patterns, forming a miniature maze. Ariadne leaps atop the edge of the maze and peers inside it."

    show ariadne happy at left
    A "Eduardo? Is that you?"

    "Theo follows Ariadne’s line of sight to spot Eduardo within the maze. A trail of slime marks Eduardo’s pathing, which double-backs and loops around. He is having difficulty escaping the maze because he is a tiny snail."
    "He is too small to see that he is only a few turns away from the exit."

    E "Eh… eh…. ehhh-xaust-ehhhhd…"

    show ariadne sad
    A "Oh no, you poor thing."

    "Ariadne cranes her neck to figure out the solution to the table-maze, but she is too short to see the entire thing at once. She points a paw at Theo."

    show ariadne neutral
    A "You…"

    T neutral "Theo."

    show ariadne happy
    A "...Theo, be a kitten and help him out!"

    menu: # stat checks for these choices?? → tulasi help
        "Help Eduardo solve the maze.":
            $ himbully += 1
            $ snailChoice += 1
            "Theo studies the maze."
            T neutral "Go forward until you hit the wall, then take two rights and a left."
            E "W… Whoa…"
            "Theo gets the impression that Eduardo is grateful."
            show ariadne neutral

        "\"Looks lame.\"":
            E "W… Ehh…"
            show ariadne neutral
            "Theo gets the impression that Eduardo is tired and sad."

        "Use a block to wall Eduardo into a box.":
            $ himbully -= 1
            $ snailChoice -= 1
            show ariadne neutral
            E "W… Wehh!"
            "Theo gets the impression that Eduardo is scared."
            show ariadne angy
            A "That’s not very mice!"
            "Ariadne uses a paw to bat your block away from Eduardo."
            show ariadne neutral
            A "Let’s not paws for too long."
            jump afterSnail

    "Ariadne studies Theo with an unreadable expression."

    show ariadne happy
    A "Let’s not paws for too long!"
    hide ariadne

label afterSnail:

    scene bg labyrinth

    "Theo and Ariadne double back on themselves several times. Fortunately, Ariadne’s yarn allows them to retrace their steps and try a different route."

    show ariadne happy at center
    A "Meow, don’t get the wrong idea. I do know where we are going. However, the labyrinth shifts around every so often, so you can never memorize a path for the next day!"

    T neutral "Huh? You said you know where you’re going, but also that you don’t know any paths."

    A "Nya-ha-ha! It’s never meow-notonous!"
    A "The labyrinth is a great retirement spot."
    hide ariadne

label vinnyPartOne:

    "Theo and Ariadne emerge into a small clearing. In the center of it sits a strange creature. Theo can only describe the creature as some sort of cow-centaur with a nerd torso. They are everything Theo dislikes."

    show vinny sad at right

    "When they speak, their voice is slow and surprisingly deep."

    $ v_name = "???"
    V "Only three views today… one less than yesterday. I’ll never be famous."

    show ariadne shocked at left
    A "Vinny, what have I told you about checking your views too often?"
    show ariadne neutral

    $ v_name = "Vinny"
    V "I want to be a moo-vie star…"

    show ariadne happy
    A "I promise, you’re famous to me! That one less viewer was only because Eduardo was stuck in a maze today, he didn’t mean to miss your stream."
    show ariadne neutral

    "Vinny shakes his head and lows."

    V "Only my friends watch me… when will the world recognize my looo-minosity?"

    show ariadne happy
    A "Soon, I’m paw-sitive! Now perk up, we have a trespasser today!"

    show vinny neutral
    V "Moo… a guest?"

    if himbully > 0:
        A "[their!c] name is Theo!"
    else:
        A "[their!c] name is Cleo!"
        T neutral "Theo."

    V "Theo… will you watch my vlogs?"

    menu:
        "\"I guess… if I’m stuck in this maze and have nothing else to do.\"" if himbully >= 0:
            $ himbully += 1
            show vinny happy
            V "Wonderful, marvelous! Five regular moo-ers–I mean, viewers!"
            show ariadne happy

        "\"Why?\"":
            show vinny shocked
            V "Why… why! It’s been so long since anybody asked me that question."
            "Vinny clears his throat with a great hacking cough."
            V "To become a star, of course. My dream is to spread a-moo-sement to the masses!"
            show ariadne happy

        "\"Why would I watch a weirdo vlog?\"":
            $ himbully -= 1
            show ariadne angy
            A "You can't call others weirdos!"
            show vinny neutral
            "Vinny draws himself up. His hair seems to puff up with his spirit."
            V "I am indeed a weirdo. And I’m proud of it!"
            show ariadne neutral

        "\"Pineapples and cows are literally the most uncool thing I’ve ever seen.\"" if himbully < 0:
            $ himbully -= 2
            show ariadne angy
            A "There’s nothing wrong with pineapples and cows together! Besides, Vinny’s only half cow!"
            show vinny neutral
            "Vinny draws himself up. His hair seems to puff up with his spirit."
            V "I am indeed half cow, like my brother. He was the Minotaur. I’m proud of it!"
            show ariadne neutral

    show vinny neutral
    A "Regardless, Theo here got lost on a school trip. I’m leading [them] out of the labyrinth."

    T angy "Don’t say it in such an embarrassing way!"

    "Ariadne ignores Theo to address Vinny."

    show ariadne happy
    if snailChoice == 1:
        A "Theo has some rough edges, but I’m confident that there’s a good person somewhere deep down there! [they!c] helped Eduardo out just now."
    elif snailChoice == 0:
        A "I’m not sure that Theo is the kind of viewer you want. [they!c] didn’t even help Eduardo out of the table-maze just now!"
    else:
        A "I’m not sure that Theo is the kind of viewer you want. [they!c] walled Eduardo into the table-maze just now!"

    show vinny shocked
    V "Interesting…"
    show vinny neutral
    V "No matter your character, Theo, I’m glad you are escaping the labyrinth. You belong to your School Trip."

    show ariadne happy
    A "It’s school trip, all lowercase!"
    show ariadne neutral

    V "Right. I would help you, but…"
    show vinny sad
    V "Unfortunately, my line is bound to this labyrinth with a curse. I will never be able to leave. My only hope of becoming famous is my vlogging channel."
    show vinny neutral
    V "So I would really appreciate your views."
    show vinny sad
    V "Thanks for stopping by…"

    show ariadne happy
    A "Anytime, Vinny! You know I don’t have any hobbies."
    hide ariadne
    hide vinny

label icarusPartOne:

    "Theo is less skeptical that Ariadne is actually leading him out, after meeting Vinny."

    show ariadne neutral at center
    A "You should know, Theo, that what I admire most about Vinny is that he’s not afraid to be himself. I wish more people would see that, so that he could achieve his goal."

    "Ariadne fluffs her tail thoughtfully."

    show ariadne happy
    A "Also, neither Vinny nor his line is actually cursed. So don’t feel too bad for him."

    T shocked "Then why does he stay in that one place?"

    show ariadne neutral
    A "In reality, he is simply too tall for the doorways in this labyrinth."

    T neutral "Not too wide?"

    show ariadne happy
    A "Nya-ha-ha! Don’t ask him that to his face, he’ll grow insecure about his body!"
    hide ariadne

    "It is another few minutes before the winged person from the very beginning swoops in from above. Theo sighs. This is just one encounter after another."

    show icarus neutral at right
    I "You dimwits still tryna get out of here?"

    show ariadne happy at left
    A "I don’t see you helping!"

    show icarus happy
    I "Hah. And waste more time with you, when I could be listening to {b}DEATH METAL{/b}?"
    show icarus neutral

    "Icarus cracks her knuckles. Permanent scowl lines frame her mouth. She narrows her eyes."

    show ariadne neutral
    show icarus angy
    I "As if I would do anything so weak."
    show icarus neutral

    show ariadne happy
    A "Did you watch Vinny’s vlog today?"

    show icarus angy
    I "Of course I did."

    menu:
        #(if watch, "i plan to watch it to"?)
        "\"You… watch Vinny’s vlog?\" Icarus does not seem the type.":
            $ himbully += 1
            show icarus happy
            I "You don’t?"

        "\"Boring.\"":
            show icarus neutral
            I "So are you."

        "\"Seems like a weakling thing to me.\"" if himbully < 0:
            $ himbully -= 1
            show icarus angy
            I "Bold words from a sprout!"

    show icarus neutral

    show ariadne happy
    A "Have you come to help us, Icarus?"

    I "As if. And don’t ask me to, because I can leave whenever I want."

    A "Then why do you keep coming back?"

    show icarus angy
    I "I wouldn’t come here at all if I weren’t so bored!"
    show icarus neutral
    I "Whatever."
    I "Don’t mind me. Go on, this should be entertaining."
    hide icarus

    "Icarus flies upwards, but the shadows of her wings remind Theo that she is watching." # * wHAT am i saying here icarus just gotta go
    "This time, Ariadne points out a direction to Theo and lets [them] lead the way. They make good progress."
    "The last doorway, however, is blocked by the desk of a professional frog. The nameplate on his desk says \"FRANCIS.\""

label frogBusinessman:

    F "Greetings, travelers. Please sit and have some tea; I always enjoy company between three and seven pm. What brings you to my den on this charming afternoon?"

    menu:
        "\"Your desk is blocking the path to exit the labyrinth.\"":
            $ himbully += 1
            show ariadne happy
            A "Yes, Francis, we need your help! Theo here is on his way out of our home."

        "Wait for Ariadne to respond.":
            $ himbully += 0
            show ariadne happy
            A "Francis, we need your help! Theo here is on his way out of our home, but your desk is blocking the path."

        "We’re not here to visit you.":
            $ himbully -= 1
            show ariadne neutral
            A "We’re here for a different reason. But of course, any other day I would be happy to visit you!"

            show ariadne happy
            A "Francis, we need your help! Theo here is on his way out of our home, but your desk is blocking the path."

    F "Hm…"

    show ariadne neutral

    F "I’m afraid I cannot help you right now."
    F "My computer is running important calculations on the intrinsic value of several new company stocks."

    if himbully > 2:
        T happy "Like, math?"
        T neutral "I uh... I sorta like math."
    elif himbully > -2:
        T "Stocks?"
    else:
        T "Math? That’s a half-baked reason."

    F "Observe here."

    "Francis shows them a complicated collection of graphs and spreadsheets on his screen. He has a command line window open, on which numbers scroll past endlessly."

    F "This is essential to maximize my profits from the stock market income stream."

    show ariadne sad

    F "So, I am loathe to move my computer and risk jeopardizing these calculations. I hope you understand."

    T neutral "That’s not how computers work…"

    A "Is there any way we can convince you to help? You could run these numbers later."

    F "Well, investment is time-sensitive."

    show ariadne neutral

    F "Perhaps if you brought me an object of equal value to the profits I would lose from the delay…"
    F "I could sell it in my online shop."
    F "Then, I could assist you."

    show ariadne happy
    A "Yes! Thank you, Francis!"

    "Francis returns to his work, ignoring everything else."

# GENREIC LABYRINTH
    A "You heard the frog, Theo! Find a valuable object for Francis to sell!"

    T shock "You don’t have one?"

    show ariadne neutral
    A "No."
    show ariadne happy
    A "I don’t need meow-terial possessions when I have such good friends!"
    A "Anyway, it’s your choice how to approach this challenge."

    "Theo considers [their] options…"
    "[they!c] could just refuse to do anything, and leave Ariadne to figure something out."
    "On the other hand, Icarus can fly out of the labyrinth at will. Perhaps she could help fetch something from the outside world."
    "Vinny might also have something."

    menu:
        "Do nothing.":
            jump askAriadne

        "Ask Icarus.":
            jump askIcarus

        "Ask Vinny.":
            jump askVinny

label askAriadne:

    "Theo retraces [their] steps to the hallway outside of Francis’ area."

    T angy "I really don’t have anything on me. And I can’t ask anyone else."
    T neutral "You have to have something, Ariadne."
    T neutral "What about your yarn ball?"

    show ariadne angy
    A "Now you’re being silly on purpose!"
    A "I would never give up my yarn ball."

    T neutral "I don’t see the problem here. You could make Icarus get you another one."

    show ariadne sad
    A "Hm… to give up my yarn ball of four decades…"
    A "Just so that Theo can leave…"
    show ariadne neutral
    A "Not worth it."

    $ gift = "nothing"
    jump frogEnd

label askIcarus:

    T neutral "What if we asked Icarus?"

    if himbully > 1:
        show ariadne happy
        A "Good idea!"
    else:
        show ariadne neutral
        A "Worth a shot."

    "Theo retraces [their] steps with Ariadne's yarn to the hallway where [they] met Icarus."

    # show labyrinth background

    T neutral "Icarus, you there?"

    show icarus happy at right
    I "Who has summoned me?"
    show icarus neutral
    I "Oh, it’s you. Still loitering here, sprout?"

    T angy "Not for much longer…"
    T neutral "…if you help me."

    show icarus angy
    I "Ehh, do I seem like a problem solving roll of duct tape to you? I’m not the helpful type!"

    if himbully > 2:
        show icarus neutral
        I "I suppose, though, since you haven’t been the worst person who could have gotten lost here, I could do you a favor this once."
        show icarus angy
        I "You’d better pay me back."
        show icarus happy
        I "What do you want, kid?"
        T "I need something valuable to give to Francis so he’ll move his desk and let us pass."
        I "Ha!"
        I "I’ve got the thing for you. I was going to give this to Francis myself later."
        "Icarus produces a fedora with a wide brim."
        T happy "Perfect!"
        show ariadne happy
        A "Thanks, Icarus! Don’t forget, Vinny’s streaming tomorrow at seven!"
        show icarus mad
        I "Don’t insult me. My memory is working fine."
        $ gift = "fedora"

    else:
        show icarus neutral
        I "Seriously though, you’re dreaming. I don’t help posers who bully people to make themselves feel better."
        show icarus angy
        I "Even in such a short time, I can tell that you don’t care enough about others to make me care about you."
        show icarus happy
        I "But it’s funny that you thought you had a chance!"
        $ gift = "nothing"

    hide icarus
    jump frogEnd

label askVinny:
    show ariadne happy
    A "Worth a shot!"

    "Theo retraces [their] steps with Ariadnes’ yarn until they arrive back at Vinny’s room."

# center of labyrinth
    show vinny shocked at right
    V "Moo’s there? I mean, who’s there?"
    show vinny neutral
    V "I need to practice talking without this lisp…"

    show ariadne happy
    A "We’re back!"

    show vinny happy
    V "So soon? Moo you want to hang out?"

    show ariadne neutral

    show vinny sad
    V "Moo… moo… do…"
    show vinny neutral

    show ariadne happy

    T neutral "We’re looking for a valuable object to give Francis so he’ll stop blocking the path to get out of here."
    T neutral "Got anything that fits the bill?"

    V "Hum… my vlogging camera was pretty expensive…"
    V "That’s what Icarus told me. She got it for me on my birthday. I don’t know how she could have afforded it, she said it’s worth thousands."
    show vinny sad
    V "I could never give it up."

    show vinny neutral
    show ariadne neutral
    V "Try someone else. I can’t help you."

    menu:
        "Bully Vinny for something, anything.":
            $ himbully -= 1

        "Try Icarus.":
            hide vinny
            jump askIcarus

        "You can’t get an object, then.":
            hide vinny
            jump askAriadne

    show vinny shocked

    show ariadne neutral

    T angy "Come on, you can’t say that you’ve been stuck here with no other objects whatsoever this entire time!"

    show ariadne shocked

    T angy "I’ll never watch you stream if you don’t cough something up!"

    show ariadne angy
    A "Don’t bully him!"

    show vinny sad
    V "I can’t afford to lose any viewers…"

    T angy "Nobody wants to watch you right now because you’re just a dumb cow stuck in a labyrinth."

    A "He’s a bull, not a cow!"

    T neutral "This is your one chance to gain viewers. But if you don’t help me…"

    show vinny shocked
    show ariadne shocked

    T angy "I’ll tell all my friends to never watch you either!"
    T angy "And believe me, I have a lot of friends!"

    show ariadne angy
    A "I don’t believe you."

    show vinny neutral
    V "I’m not just a dumb cow. I love who I am."
    show vinny sad
    V "But since you put it that way… I do need more viewers."

    T happy "I’m glad you came around."

    V "The problem is, I don’t have anything else valuable, other than my shirt."

    show vinny shocked
    show ariadne shocked
    T "Then I want your shirt."

    V "That’s–that’s indecent!"

    "Under Theo’s insistence, Vinny reluctantly hands over his shirt."

    show ariadne sad

    show vinny shocked2
    V "It’s cold…"
    show vinny sad2

    T happy "Perfect."
    T shocked "Where did all these muscles come from, though?"

    V "All there is to do here is exercise…"
    hide vinny

    $ gift = "pineapple shirt"

    jump frogEnd

label frogEnd:

    # GENERIC LABYRINTH (or f’s room?)

    if gift != "nothing":

        "[gift!c] in hand, Ariadne and Theo return to Francis’ workstation."

        show ariadne neutral
        A "Francis, we’ve found an object for you to sell!"

        F "Hello again."
        F "This is… a [gift]?"

        show ariadne happy
        A "It’s not just any [gift]! This is unique!"

        T neutral "I put in so much effort to get it, so it’d better be enough…"

        F "I love it!"
        F "I know exactly what description to write for this."

        if gift == "pineapple shirt":
            F "This pineapple dream will make you gleam!"
        else:
            F "This spiffy fedora has a gentleman’s aura!"

    else:
        "Having found nothing, Ariadne and Theo return to Francis’ workstation."

        show ariadne sad
        A "Francis… we’ve failed you. We don’t have anything to sell."

        F "That is disappointing, but please do not feel too bad."

        show ariadne happy

        F "During your absence, I discovered a lustrous rock!"
        F "Although your object would have been worth more, this will do just fine."

    "Francis lifts his desk clean off of the ground and motions for Ariadne and Theo to make their way through."

label argument:
    # generic labyrinth

    "After a while of walking, Theo and Ariadne happen upon a familiar length of yarn."

    T shock "We’ve been here before."

    show ariadne happy
    A "Sometimes, it happens."
    show ariadne neutral
    A "Let’s go back to the right turn instead of the left…"

    "The right turn leads them to another length of yarn."

    T angy "We’ve been here before, too!"

    show ariadne happy
    A "Have patience."

    "They try again. This time they emerge into the corridor before Vinny’s clearing."

    T angy "What’s up with this? Why aren’t we out yet?"

    show ariadne neutral
    A "Patience is a virtue! We can try again…"

    if himbully > 2:
        T neutral "This labyrinth doesn’t make any sense. I thought we were heading in the right direction."
        A "Meow-be, we need to head in the left direction!"

        $ hasAri = 1
        jump vinnyPartTwo

    elif himbully > -1:
        T angy "This labyrinth doesn’t make any sense."

        show ariadne angy
        A "Hey meow, I want you out too! But don’t insult my home."
        show ariadne neutral
        A "Sometimes things are strange and not straightforward. That’s the charm of it! The labyrinth always has fun things to do."

        T angy "I’m not here to have fun. I wasn’t meant to be here at all. I want things to go back to normal."

        show ariadne angy
        A "Just because we’re not normal, doesn’t mean we’re not worth getting to know!"

        "Ariadne hisses and claws at her yarn."

        show ariadne neutral
        A "There! Now, the yarn is tangled."
        A "You’d better cool your claw-ful temper, or I won’t come back!"
        hide ariadne

        "Ariadne stalks off with her back arched."
        $ hasAri = 0

        jump vinnyPartTwo

    else:
        T angy "This labyrinth doesn’t make any sense. It’s stupid! I want out already."

        show ariadne angy
        A "Hey meow, I want you out too! But don’t insult my home."
        show ariadne neutral
        A "Sometimes things are strange and not straightforward. That’s the charm of it! The labyrinth always has fun things to do."

        T angy "I don’t care about this stupid labyrinth."

        show ariadne angy
        A "Well, this labyrinth doesn’t care about you!"
        A "Icarus, I’m begging you. Take this child off my hands."

        "Icarus lands with a flurry of feathers. Her face is dark."

        show icarus angy
        I "I’ve had enough of this one too."
        hide ariadne

        "Icarus strides towards Theo. Theo cringes away, but she only swipes [them] up by [their] shoulders and ascends into the sky. She seems to delight in the way Theo squeals in fright when she tosses [them] onto the ground outside the corn maze after a steep dive."

        show icarus happy
        I "That’s that for you, brat! See that you change your attitude, unless you wanna die alone."
        show icarus neutral
        I "Middle schoolers always wanna be cool, but the most uncool thing is betraying yourself just to fit in."
        hide icarus

        jump outsideMaze

label vinnyPartTwo:

    "Sullen, Theo re-arrives at Vinny’s."
    if gift == "pineapple shirt":
        show vinny shocked2
        V "Back again?"

        if hasAri == 1:
            show ariadne neutral
            A "Still on our way out. Theo is becoming impatient, though."

            show vinny neutral2
            V "I remember when I was young and impatient to be famous..."
            V "I’m still that way."
        else:
            T neutral "Ariadne tangled her yarn and ditched me."
            V "What did you do?"
            T angy "Why do you assume right away that it’s something I did?"
            T neutral "She’s the one who threw a hissy fit. I only said I wanted to leave."
            T angy "That’s what we’ve been trying to do all along!"

        show vinny neutral2
        V "The most important things take time, Theo. Take it from me."
        show vinny sad2
        V "I’m not famous yet."

        T neutral "You’re pretty weird to me."

        show vinny happy2
        V "Yes, I’m weird!"

        T mad "That’s not a compliment!"
        T neutral "I only meant, I don’t understand how you want to be famous so much. What makes you deserve to be famous, when you’re so…"
        T neutral "Not mainstream?"

        show vinny happy2
        V "Oh, you’re asking about my special self-cow-nfidence!"

        T shocked "That’s not what I’m asking about…"

        V "Of course, I deserve to be famous! I stand out."
        show vinny neutral2
        V "People who want to fit in, they erase many of the unique parts of themselves."
        show vinny happy2
        V "Those moo-nique parts are in fact what endears them to udders! The things that I care about aren’t less important to me just because they aren’t important to everyone else."
        show vinny neutral2
        V "You have a moo-nique interest of your own, right?"

        T angy "I’m not a loser!"

        show vinny shocked2
        V "Such a vehement response…"

        show vinny neutral2
        V "Having an interest doesn’t mean you’re a loser."

        show vinny happy2
        V "It means you aren’t boring!"

        T shocked "I can’t believe you’re actually making sense."
        T sad "I suppose… you have a point."
        T neutral "…"
        T happy "I like dolls!"

        V "You’re not so bad, calf!"

        "Icarus swoops in."

        show icarus happy at center
        I "Huh, I suppose you aren’t just some cardboard cutout after all. You’ve earned my help."
        hide icarus

        if hasAri == 1:
            "Icarus picks up the yarn and soars upward. Theo sees her weaving over the labyrinth, in and out of sight."
        else:
            "Icarus picks up the tangled yarn and soars upward. Theo sees her weaving over the labyrinth, in and out of sight."

        "Eventually, Theo hears a distant call…"

        I "Alright sprout, follow the yarn."

        "Vinny gives Theo an encouraging smile as [they] step tentatively back into the labyrinth corridors."
        hide vinny
        hide ariadne
    else:
        show vinny shocked
        V "Back again?"

        if hasAri == 1:
            show ariadne neutral
            A "Still on our way out. Theo is becoming impatient, though."

            show vinny neutral
            V "I remember when I was young and impatient to be famous..."
            V "I’m still that way."
        else:
            T neutral "Ariadne tangled her yarn and ditched me."
            V "What did you do?"
            T angy "Why do you assume right away that it’s something I did?"
            T neutral "She’s the one who threw a hissy fit. I only said I wanted to leave."
            T angy "That’s what we’ve been trying to do all along!"

        show vinny neutral
        V "The most important things take time, Theo. Take it from me."
        show vinny sad
        V "I’m not famous yet."

        T neutral "You’re pretty weird to me."

        show vinny happy
        V "Yes, I’m weird!"

        T mad "That’s not a compliment!"
        T neutral "I only meant, I don’t understand how you want to be famous so much. What makes you deserve to be famous, when you’re so…"
        T neutral "Not mainstream?"

        show vinny happy
        V "Oh, you’re asking about my special self-cow-nfidence!"

        T shocked "That’s not what I’m asking about…"

        V "Of course, I deserve to be famous! I stand out."
        show vinny neutral
        V "People who want to fit in, they erase many of the unique parts of themselves."
        show vinny happy
        V "Those moo-nique parts are in fact what endears them to udders! The things that I care about aren’t less important to me just because they aren’t important to everyone else."
        show vinny neutral
        V "You have a moo-nique interest of your own, right?"

        T angy "I’m not a loser!"

        show vinny shocked
        V "Such a vehement response…"

        show vinny neutral
        V "Having an interest doesn’t mean you’re a loser."

        show vinny happy
        V "It means you aren’t boring!"

        T shocked "I can’t believe you’re actually making sense."
        T sad "I suppose… you have a point."
        T neutral "…"
        T happy "I like dolls!"

        V "You’re not so bad, calf!"

        "Icarus swoops in."

        show icarus happy at center
        I "Huh, I suppose you aren’t just some cardboard cutout after all. You’ve earned my help."
        hide icarus

        if hasAri == 1:
            "Icarus picks up the yarn and soars upward. Theo sees her weaving over the labyrinth, in and out of sight."
        else:
            "Icarus picks up the tangled yarn and soars upward. Theo sees her weaving over the labyrinth, in and out of sight."

        "Eventually, Theo hears a distant call…"

        I "Alright sprout, follow the yarn."

        "Vinny gives Theo an encouraging smile as [they] step tentatively back into the labyrinth corridors."
        hide vinny
        hide ariadne

label outsideMaze:
    # outside maze

    stop music fadeout 1.0
    play music "audio/Kevin MacLeod - Nu Flute.mp3"

    T neutral "Hey…"

    Teacher "Theo, where have you been? I was just about to mark you as missing."

    "Theo reflects on the labyrinth."

    if himbully > 2:
        "The maze and its inhabitants took some getting used to. It was all weird, but kind of cool. Icarus was the most normal one in there, and Icarus has wings."
    elif himbully > -1:
        "The maze and its inhabitants were all weird. Icarus was the most normal one in there, and Icarus has wings."
    else:
        "The maze and its inhabitants were all weird. Talking animals? Give Theo a break."

    T neutral "I wanted to solve the maze by myself. And I did."

    Teacher "Congratulations. Next time, let someone know before wandering off."

    "Theo rejoins his friends, who jeer at him."

    Classmate1 "Got lost, Theo?"

    menu:
        "Leave them for the student with the dolls." if himbully > -1:
            $ ending = 1
            "Theo had been gone for only a day, and [their] posse turned on [them]. It isn’t worth trying to fit in with these posers."
            T neutral "Whatever."
            Classmate1 "Wait, where are you going?"
            T happy "To find more brain cells, after half of them just shriveled up from being near you."
            Classmate2 "Ooh!"
            Outcast "Here to make fun of me again? Tch. Stop pretending."
            T angy "I’m not pretending."

            if toy == "Transformers":
                T neutral "If you’re into Transformers, then Transformers Toys Heroic is much better than Playskool."
                T happy "You should come over today so I can show you."
                Outcast "Really? Okay! But you're totally wrong about Playskool."
            else:
                T neutral "If you’re into My Little Pony, then Gen 4 is far superior to Gen 3."
                T happy "You should come over today so I can show you."
                Outcast "Really? Okay! But you're totally wrong about Gen 3."
            T neutral "Figures that the only person around here with some taste, actually has horrible taste."

        "Play it off.":
            $ ending = 0
            T shocked "Me, get lost? You’re making stuff up."
            T neutral "I only go where I want to go."
            "Theo looks wistfully at the dolls in the hands of that student he was making fun of earlier."
            Classmate2 "You’re too cool! Find anything interesting?"
            T neutral "So there was this talking cat…"
            Classmate1 "Really?!"
            T happy "Ha! I’m messing with you. You should have seen your faces!"

        "Jeer back." if himbully < -1:
            $ ending = -1
            T shocked "Me, get lost? You’re making stuff up."
            T angy "I saw more of that maze than you’ll ever see! You dimwits only ever follow the teacher or me."
            T neutral "Good thing, too. I couldn’t imagine the hospital bills if you tried to think for yourselves."
            Classmate1 "We don’t have to follow you, you know!"
            "Theo sits alone on the train ride home, cursing the labyrinth for ruining [their] field trip."
            "[they!c] just wanted to fit in… but ended up standing out anyway."

label endGame:

    scene black

    "The End"

    if ending == 1:
        "Wow, you made choices that changed Theo to become nicer!"
        "That must have been difficult. He’s quite stubborn."
    elif ending == 0:
        "Somehow, Theo barely changed at all in the labyrinth."
        "He’s quite stubborn!"
    else:
        "I can’t help but think that you could have been a nicer person today."
        "Does Theo feel bad at all? ><"

    "Regardless of what you chose, we hope you enjoyed the outcomes."
    "Thank you for playing! Support us by rating this game and leaving a comment."
    "If you liked this, check out other games made for Slice of Jam!"

    return
