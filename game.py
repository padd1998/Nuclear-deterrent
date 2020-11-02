import time
from random import randint

from time import sleep
import sys

red = '\033[1;30;41m'
green =  '\033[1;32;40m' # Green Text

def the_chance():
    global ran
    ran = randint(1,10)

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def typewriter():
    global write
    for letter in write:
        sleep(0.01) # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(1)

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def intro():
    global chance
    global time_count
    chance = 8
    time_count = 120
    print(green+"""
    _   __           __                   ____       __                            __ 
   / | / /_  _______/ /__  ____ ______   / __ \___  / /____  _____________  ____  / /_
  /  |/ / / / / ___/ / _ \/ __ `/ ___/  / / / / _ \/ __/ _ \/ ___/ ___/ _ \/ __ \/ __/
 / /|  / /_/ / /__/ /  __/ /_/ / /     / /_/ /  __/ /_/  __/ /  / /  /  __/ / / / /_  
/_/ |_/\__,_/\___/_/\___/\__,_/_/     /_____/\___/\__/\___/_/  /_/   \___/_/ /_/\__/
""")
    begin = input("Do you want to begin the game? [Y/N]: ")
    if begin.upper() == "Y" or begin.upper() == "YES":
        print("ok lets go")
        time.sleep(1)
        fense()
    elif begin.upper() == "N" or begin.upper() == "NO":
        print("Enjoy your last 2 hours on earth")
    else:
        print("I don't understand, write that again please")
        intro()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def obey():
    global correct
    global ran
    global chance
    global time_count
    if chance < ran:
    #do the opposite
        correct = True
        if chance > 6:
            chance -= 1
    else:
        #do what he says
        # print("He does what you tell him")
        correct = True

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def fense():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = green+ """A nuclear missile has been set to launch for the UK in 2 hours' time. As head of the nuclear deterrent squad you have been assigned the task of directing one of the nation's most successful field agents on the mission. 

The nuclear base is surrounded by an electrified fence. There are two ways to get around this. The fuse box for the fence is at the back of the building.

On your left there are two armed-security guards, get around them and you will be able to disable the electric fence and climb over it. This will take 15 minutes.

The right way leads to the river and the drive-in entrance. This route is guarded by trained fighter dogs. Their barking would alert more security and their attack could be deadly. This will take 20 minutes

Should Agent 101 go [1] Left or [2] right?"""
    typewriter()
    
    
    l_r = input(" [1 or 2]: ")
    the_chance()
    obey()
    if l_r == "2" and correct == True:
        write = """
Risky call! But Agent101 always keeps some doggy treats in his pocket and managed to keep the dogs quiet while he got to the river and loading docks.

        """
        print("""
                             ;\\
                            |' \\
         _                  ; : ;
        / `-.              /: : |
       |  ,-.`-.          ,': : |
       \  :  `. `.       ,'-. : |
        \ ;    ;  `-.__,'    `-.|
         \ ;   ;  :::  ,::'`:.  `.
          \ `-. :  `    :.    `.  \\
           \   \    ,   ;   ,:    (\\
            \   :., :.    ,'o)): ` `-.
           ,/,' ;' ,::"'`.`---'   `.  `-._
         ,/  :  ; '"      `;'          ,--`.
        ;/   :; ;             ,:'     (   ,:)
          ,.,:.    ; ,:.,  ,-._ `.     \""'/
          '::'     `:'`  ,'(  \`._____.-'"'
             ;,   ;  `.  `. `._`-.  \\
             ;:.  ;:       `-._`-.\  \`.
              '`:. :        |' `. `\  ) \\
                 ` ;:       |    `--\__,'
                   '`      ,'
                        ,-'
""")

        time_count -= 20
        typewriter()
        dogs()
    elif l_r == "2" and correct == False:
        write = """
Unfortunately, Agent 101 has had a phobia of dogs since he was bitten on the nose by one aged 6. He will not be taking your advice this time.

        """
        time_count -= 15
        typewriter()
        guards()
    elif l_r == "1" and correct == True:
        write = """
Great news! The guard’s favourite football team are playing. He has been glued this phone the whole time so Agent101 was able to sneak past undetected.

        """
        time_count -= 15
        typewriter()
        guards()
    elif l_r == "1" and correct == False:
        write = """
Unfortunately, Agent 101 sees himself as a dog whisperer and so trusts that he will be able to win the dogs over. He will not be taking your advice this time.

"""
        time_count -= 20
        typewriter()
        dogs()
    else: 
        print("I dont understand, please try again")
        fense()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def guards():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
Now to get inside the base...

Should Agent101:
1)  Climb up the back window and enter the building through the vents. This will take 20 minutes.
2)  Knock out the guard to steal their uniform and use as a disguise. This will take 5 minutes

    """
    typewriter()
    write = """
[1] or [2]
    """
    l_r = input("[1] or [2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
Agent 101 is able to climb up a window at the back of the building which led to the vents. 

"""
        print("""
_____________________________________________________________________
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|      |      |_____|___|___|___|___|___|___|__
_|___|___|___|___|_____|      |      |___|___|___|___|___|___|___|___|
___|___|___|___|___|___|______|______|_____|___|___|___|___|___|___|__
_|___|___|___|___|_____|      |      |___|___|___|___|___|___|___|___|
___|___|___|___|___|___|      |      |_____|___|___|___|___|___|___|__
_|___|___|___|___|_____|______|______|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
""")
        time_count -= 20
        typewriter()
        window()
    elif l_r == "1" and correct == False:
        write = """
\"Do I look like spiderman to you?!\" He will not be taking your advice this time.

        """
        time_count -= 5
        typewriter()
        knockout()
    elif l_r == "2" and correct == True:
        write = """
Knock out the guard to steal their uniform and use as a disguise

"""
        time_count -= 5
        typewriter()
        print(""" 
                      ________________
                      \      __      /         __
                       \_____()_____/         /  )
                       '============`        /  /
                        #---\  /---#        /  /
                       (# @\| |/@  #)      /  /
                        \   (_)   /       /  /
                        |\ '---` /|      /  /
                _______/ \\_____// \____/ o_|
               /       \  /     \  /   / o_|
              / |           o|        / o_| \\
             /  |  _____     |       / /   \ \\
            /   |  |===|    o|      / /\    \ \\
           |    |   \@/      |     / /  \    \ \\
           |    |___________o|__/----)   \    \/
           |    '              ||  --)    \     |
           |___________________||  --)     \    /
                |           o|   ''''   |   \__/
                |            |          |
                """)
        knockout()
    elif l_r == "2" and correct == False:
        write = """
\"Do I look like Mike Tyson to you?!\" He will not be taking your advice this time.

        """
        time_count -= 20
        typewriter()
        window()
    else: 
        print("I dont understand, please try again")
        guards()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def window():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = "The [1] left vent seems like an easy way in, you can see the light at the end and estimate it would be a 10-minute crawl, however you can see cracks in the metal. The [2] right vent seems more stable but from the blueprint you know it would take around 30 minutes"
    typewriter()
    write = "\"Which way do I go in boss?\" [1] left or [2] right: "
    l_r = input("[1] or [2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        time_count -= 10
        left_vent()
    elif l_r == "1" and correct == False:
        write = """
\"A big guy like me? I’d fall straight through!\"  He will not be taking your advice this time.

        """
        time_count -= 30
        typewriter()
        right_vent()
    elif l_r == "2" and correct == True:
        time_count -= 30
        right_vent()
    elif l_r == "2" and correct == False:
        write = """
\"Oh come on! We don’t have time we have to take risks! I’ll take the left\" He will not be taking your advice this time.

        """
        time_count -= 10
        typewriter()
        left_vent()
    else: 
        print("I dont understand, please try again")
        window()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def knockout():
    global write
    global time_count
    write = """
You have chosen to fight the guard. As Agent 101 gets closer, he realises theres a massive size difference. The guard is built like a tank. However, Agent 101 is trained in Brazillian Jiu- Jitsu. \"Put him in a rear naked choke and don't let go\", you suggest. Agent 101 jumps on him from behind and tries to choke him out. The guard isn't having it and slams himself down and all you hear is a loud cracking. You can only assume the guard has just crushed every last bone in Agent 101's body. \"Agent, can you hear me?\" you ask in a panic. There is no response. 

"""
    typewriter()
    print(red+'''

8b    d8 88 .dP"Y8 .dP"Y8 88  dP"Yb  88b 88     888888    db    88 88     888888 8888b.  
88b  d88 88 `Ybo." `Ybo." 88 dP   Yb 88Yb88     88__     dPYb   88 88     88__    8I  Yb 
88YbdP88 88 o.`Y8b o.`Y8b 88 Yb   dP 88 Y88     88""    dP__Yb  88 88  .o 88""    8I  dY 
88 YY 88 88 8bodP' 8bodP' 88  YbodP  88  Y8     88     dP""""Yb 88 88ood8 888888 8888Y

''')
    l_r = input("Do you want to play again? [Y/N] ")
    if l_r.upper() == "Y":
        intro()
    elif l_r.upper() == "N":
        print("Well, have a nice life. ")
    else: 
        print("I dont understand, please try again")
        knockout()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def right_vent():
    global write
    global time_count
    write = """
An opening appears and Agent 101 finds himself in the cleaning closet, but he’s not alone...

"""
    typewriter()
    cleaning_cupboard()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def left_vent():
    global write
    global time_count
    write = """
Agent 101 made his way through the rickety vent but it couldn’t take his weight. He fell straight through the ceiling and landed in the middle of a meeting table with the Director of Central Intelligence. He got arrested. Mission Failed.

"""
    typewriter()
    nuclear_room()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def cleaning_cupboard():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
A cleaner is preparing her cart for her shift.
\"AHH What are you doing?!\" she yells

"""
    typewriter()
    write = """
Should Agent101:
1)  Bribe the cleaner to get keep her quiet. This may take up to 10 minutes
2)  Shoot her with a tranquiliser dart so that you can continue your mission in peace. It will be quick and painless, just a minute to silently set up the dart

"""
    typewriter()
    l_r = input("[1 or 2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
Sadly, the cleaner doesn’t speak English and misinterprets your advances for something even more disrespectful.

"""
        typewriter()
        bribe()
    elif l_r == "1" and correct == False:
        write = """
\"That will never work!\" He will not be taking your advice this time. Instead, he injects her with a sleeping drug. 
She falls to the ground before Agent 101 can catch her. 

        """
        time_count -= 1
        typewriter()
        body()
    elif l_r == "2" and correct == True:
        write = """
Agent101 shoots the cleaner with the tranquiliser dart and the cleaner falls to the ground.

"""
        time_count -= 1
        typewriter()
        print("""
                               ____
       _____,,,,,,,,,,,__     /    `.
---===<_____||| || :::|__|88=<=------)
            ```````````       \____.'  
""")
        body()
    elif l_r == "2" and correct == False:
        write = """
\"She isn’t the enemy here!\" He will not be taking your advice this time.

"""

        typewriter()
        bribe()
    else:
        print("Sorry, I didn't get that. ")
        cleaning_cupboard()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def bribe():
    global write
    global time_count
    write = """
She immediately sounds her personal alarm and security rush in and arrests Agent101 almost immediately. Mission failed.

"""
    typewriter()
    print(red+'''

8b    d8 88 .dP"Y8 .dP"Y8 88  dP"Yb  88b 88     888888    db    88 88     888888 8888b.  
88b  d88 88 `Ybo." `Ybo." 88 dP   Yb 88Yb88     88__     dPYb   88 88     88__    8I  Yb 
88YbdP88 88 o.`Y8b o.`Y8b 88 Yb   dP 88 Y88     88""    dP__Yb  88 88  .o 88""    8I  dY 
88 YY 88 88 8bodP' 8bodP' 88  YbodP  88  Y8     88     dP""""Yb 88 88ood8 888888 8888Y

''')
    l_r = input("Do you want to play again? [Y/N]")
    if l_r.upper() == "Y" or l_r.upper() == "YES":
        intro()
    elif l_r.upper() == "N" or l_r.upper() == "NO":
        print("Goodbye")
    else:
        print("I dont understand, please try again")
        bribe()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def body():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
Should Agent 101:
1)  Leave it where it is, He doesn’t have time to waste, besides whats the worst that could happen? This will take no time.
2)  Put the body in the cleaning cart, if someone finds an unconscious body alarms will be raised across the building. This will take 5 minutes

"""
    typewriter()
    l_r = input("[1 or 2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
He obeys you and walks on. 

"""
        typewriter()
        discover_body()
    elif l_r == "1" and correct == False:
        write = """
\"You can’t just leave her there, so undignified!\" He will not be taking your advice this time.

"""
        time_count -= 5
        typewriter()
        corridor()
    elif l_r == "2" and correct == True:
        write = """
He stuffs the body into the cart. 
"""
        time_count -= 5
        typewriter()
        corridor()
    elif l_r == "2" and correct == False:
        write = """
The body doesn't fit very well at all, so he gives up and leaves it there, despite your protestations. He will not follow your advice. 
"""
        typewriter()
        discover_body()
    else:
        print("I dont understand, please try again")
        body()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def discover_body():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
As the agent walks down the corridor, he hears shouts behind and is discovered. 
"""
    typewriter()
    print(red+'''

8b    d8 88 .dP"Y8 .dP"Y8 88  dP"Yb  88b 88     888888    db    88 88     888888 8888b.  
88b  d88 88 `Ybo." `Ybo." 88 dP   Yb 88Yb88     88__     dPYb   88 88     88__    8I  Yb 
88YbdP88 88 o.`Y8b o.`Y8b 88 Yb   dP 88 Y88     88""    dP__Yb  88 88  .o 88""    8I  dY 
88 YY 88 88 8bodP' 8bodP' 88  YbodP  88  Y8     88     dP""""Yb 88 88ood8 888888 8888Y

''')
    l_r = input("Do you want to play again? [Y/N]")
    the_chance()
    obey()
    if l_r.upper() == "Y" or l_r.upper() == "YES":
        intro()
    elif l_r.upper() == "N" or l_r.upper() == "NO":
        print("Goodbye")
    else:
        print("Say again. ")
        discover_body()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def corridor():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
You are in a corridor. Facing you are two doors. Pick nuclear activity [1] or control room [2]. 
"""
    typewriter()
    l_r = input("[1] or [2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
You picked the nuclear room. You enter it and die immediately of radiation poisoning. 
"""
        typewriter()
        nuclear_room()
    elif l_r == "1" and correct == False:
        write = """
The agent disobeys you and enters the control room. 
"""
        typewriter()
        control_room()
    elif l_r == "2" and correct == True:
        write = """
You enter the control room. 
"""
        typewriter()
        control_room()
    elif l_r == "2" and correct == False:
        write = """
The agent disobeys you and enters the nuclear room. He immediately dies of radiation poisoning. 
"""
        typewriter()
        nuclear_room()
    else:
        print("Say again. ")
        corridor()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def control_room():
    global write
    global time_count
    write = """
Luckily the control room is empty. Standing out from the hundreds of keys one stands out “DISABLE NUCLEAR MISSILE”. 
Agent101 immediately presses it and a question appears on the screen. Solve this, and all scheduled missiles will be disabled.

"""
    typewriter()
    input("""
Please enter the password to disable the nuclear protocol: 

""")
    time.sleep(3)
    write = """
Incorrect Password

"""
    typewriter()
    input("""
Please enter the password to disable the nuclear protocol (Attempt 2/3): 

""")
    time.sleep(3)
    typewriter()
    input("""
Please enter the password to disable the nuclear protocol (Attempt 3/3): 

""")
    time.sleep(3)
    write = """
Password accepted. Nuclear Protocol disabled.

"""
    typewriter()
    write = """
Congratulations! With only {} minutes to spare, you and Agent101 have disabled the nuclear missile and saved your country from annihilation! You have completed the game!

""".format(time_count)
    typewriter()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def nuclear_room():
    print(red+'''

8b    d8 88 .dP"Y8 .dP"Y8 88  dP"Yb  88b 88     888888    db    88 88     888888 8888b.  
88b  d88 88 `Ybo." `Ybo." 88 dP   Yb 88Yb88     88__     dPYb   88 88     88__    8I  Yb 
88YbdP88 88 o.`Y8b o.`Y8b 88 Yb   dP 88 Y88     88""    dP__Yb  88 88  .o 88""    8I  dY 
88 YY 88 88 8bodP' 8bodP' 88  YbodP  88  Y8     88     dP""""Yb 88 88ood8 888888 8888Y

''')
    global write
    global time_count
    write = "Do you want to play again?"
    typewriter()
    l_r = input("[Y/N]")
    if l_r.upper() == "Y" or l_r.upper() == "YES":
        intro()
    elif l_r.upper() == "N" or l_r.upper() == "NO":
        print("Goodbye")
    else:
        print("Say again. ")
        nuclear_room()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def dogs():
    global chance
    global ran
    global correct
    global write
    global time_count
    global time_car
    write = """
Agent 101 sneaks past the dogs. He notices a sewage pipe which could potentially lead him into the base. 
Alternatively, there is a truck on standby to go into the base at any minute, could this be another way in?
Should agent101:
1)  Use the sewage pipe, he will be able to climb up through the drains. This will take 45 mins.
2)  Hide in the back of the truck, it’s only a matter of time before it gets driven inside. This could take anywhere between 0 - 2 hours.

"""
    typewriter()
    l_r = input("[1] or [2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        print('''
       __             _,-"~^"-.
     _// )      _,-"~`         `.
   ." ( /`"-,-"`                 ;
  / 6                             ;
 /           ,             ,-"     ;
(,__.--.      \           /        ;
 //'   /`-.\   |          |        `._________
   _.-'_/`  )  )--...,,,___\     \-----------,)
 ((("~` _.-'.-'           __`-.   )         //
       ((("`             (((---~"`         //
                                          ((________________
                                          `----""""~~~~^^^```
''')
        write = """
Rabid rats attack Agent 101. It takes 15 minutes to get rid of them and get himself together.
After 45 minutes of drudging through the sewage there is an opening. 

"""
        time_count -= 60
        typewriter()
        drain()
    elif l_r == "1" and correct == False:
        write = """
/“You’ve got to be joking!/” He will not be taking your advice this time. He sneaks behind the truck.

"""
        time_car = randint(1, 120)
        time_count -= time_car
        typewriter()
        if time_count <= 0:
            write = "Nobody came to the truck. You hear sirens announcing the deployment of the nuclear bomb. It's the end of the world and Agent 101 spent his last moments hiding under a car." 
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            wait_under_car()
    elif l_r == "2" and correct == True:
        write = """
"Good idea", Agent 101 says. He sneaks behind the truck.

"""
        time_car = randint(1, 120)
        time_count -= time_car
        typewriter()
        if time_count <= 0:
            write = "Nobody came to the truck. You hear sirens announcing the deployment of the nuclear bomb. It's the end of the world and Agent 101 spent his last moments hiding under a car." 
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            wait_under_car()
    elif l_r == "2" and correct == False:
        write = """
 “I could be waiting there for hours! We don’t have time for this.” He will not be taking your advice this time.
"""
        typewriter()
        write = """
Rabid rats attack Agent 101. It takes 15 minutes to get rid of them and get himself together.
After 45 minutes of drudging through the sewage there is an opening. 

"""
        time_count -= 60
        typewriter()
        drain()
    else:
        print("I dont understand, please try again")
        dogs()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def drain():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
Agent 101 climbs up out of drain into the building with his shoes covered in sewage. There is a cleaning closet across the hall.
Should Agent 101
1)  Take 30 minutes to clean himself up
2)  Carry on the mission as is

"""
    typewriter()
    l_r = input("[1] or [2]:")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
Agent 101 enters the cleaning cupboard. 

"""
        time_count -= 30
        typewriter()
        if time_count <= 0:
            write = "You hear sirens through the earpiece announcing the launching of the bomb. Agent 101 took too long to clean himslef off and as a result the world is going to end."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            cleaning_cupboard()
    elif l_r == "1" and correct == False:
        write = """
“A little bit of dirt never hurt nobody!” He will not be taking your advice this time.
Agent101 continues down the hall but before he can find any more clues he is apprehended by two guards - his dirty shoes left a trail. 
Mission Failed.
"""
        typewriter()
        nuclear_room()
    elif l_r == "2" and correct == True:
        write = """
He walks away, leaving trail of sewage.

Agent101 continues down the hall but before he can find any more clues he is apprehended by two guards - his dirty shoes left a trail. Mission Failed.

"""
        typewriter()
        nuclear_room()
    elif l_r == "2" and correct == False:
        write = """
“I’ll leave a trail! Use your common sense!” He will not be taking your advice this time.

"""
        time_count -= 30
        typewriter()
        if time_count <= 0:
            write = "You hear sirens through the earpiece announcing the launching of the bomb. Agent 101 took too long to clean himslef off and as a result the world is going to end."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            cleaning_cupboard()
    else:
        print("I dont understand, please try again")
        drain()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def wait_under_car():
    global write
    global time_count
    global time_car
    write = """
Agent 101 clambers onto the underside of the truck. He is waiting for {} minutes for the driver to return and drive into the garage. 
""".format(time_car)
    typewriter()
    garage()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def garage():
    global chance
    global ran
    global correct
    global write
    global time_count
    write = """
Inside the garage are two routes to get to the control room. The first [1] lots of people are using (steal a uniform). 
The second [2] is a conveyer belt for materials and parts.
Should Agent101:
[1] Catch a ride on a conveyor belt of materials heading inside. This will take 10 minutes.
[2] Steal the drivers uniform and walk in as a staff member. This will take 20 minutes.

"""
    typewriter()
    l_r = input("[1] or [2]: ")
    the_chance()
    obey()
    if l_r == "1" and correct == True:
        write = """
Agent101 climbs out of the truck and onto the conveyor belt. While moving into the building 
all materials are compressed, crushing him to death. Mission failed.

"""
        typewriter()
        nuclear_room()
    elif l_r == "1" and correct == False:
        write = """
"How am I supposed to hide on there?” He will not be taking your advice this time. 

In full uniform Agent101 is able to walk into the building unchallenged. To avoid drawing attention he enters the first room he sees 
- the staff room. To his dismay the room is full with staff.

""" 
        time_count -= 20
        typewriter()
        if time_count <= 0:
            write = "You hear sirens through the earpiece announcing the launching of the bomb. The mission took too long and as a result the world is going to end."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            staff_room()
    elif l_r == "2" and correct == True:
        write = """
In full uniform Agent101 is able to walk into the building unchallenged. To avoid drawing attention he enters the first room he sees 
- the staff room. To his dismay the room is full with staff.

"""
        time_count -= 20
        typewriter()
        if time_count <= 0:
            write = "You hear sirens through the earpiece announcing the launching of the bomb. The mission took too long and as a result the world is going to end."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            staff_room()
    elif l_r == "2" and correct == False:
        write = """
Agent101 climbs out of the truck and onto the conveyor belt. While moving into the building 
all materials are compressed, crushing him to death. Mission failed.

"""
        typewriter()
        nuclear_room()
    else:
        print("I dont understand, please try again")
        garage()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

def staff_room():
    global write
    global time_count
    write = """
Should Agent 101:
[1] Strike up a conversation with another staff member and get directions (15 mins)
[2] Hurry away before anyone notices he is there (2 mins)
"""
    typewriter()
    l_r = input("[1] or [2]: ")     
    if l_r == "1" and correct == True:
        write = """
By pretending it’s his first day at work, Agent101 befriends a fellow driver who gives him a personal map of the building. 
He uses the map to get to the area of the building responsible for controlling nuclear activity. 

"""
        time_count -= 15
        typewriter()
        the_chance()
        obey()
        if time_count <= 0:
            write = "As Agent 101 is talking, a siren starts to ring to announce the launch of the nuclear missile. The world is about to end and the entire room starts clapping."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            corridor()
    elif l_r == "1" and correct == False:
        write = """
/“You want me to have a cup of tea too?/” He will not be taking your advice this time.

"""
        typewriter()
        write = """
Some of the staff get suspicious when they see Agent101 come in and go out so quickly. 
They alert security and he is arrested. Mission failed. 

"""
        typewriter()
        nuclear_room()
    elif l_r == "2" and correct == True:
        write = """
Some of the staff get suspicious when they see Agent101 come in and go out so quickly. 
They alert security and he is arrested. Mission failed. 
"""
        typewriter()
        nuclear_room()
    elif l_r == "2" and correct == False:
        write = """
/“How much more obvious can you get?!/” He will not be taking your advice this time.

"""
        typewriter()
        write = """
By pretending it’s his first day at work, Agent101 befriends a fellow driver who gives him a personal map of the building. 
He uses the map to get to the area of the building responsible for controlling nuclear activity. 

"""
        time_count -= 15
        typewriter()
        if time_count <= 0:
            write = "As Agent 101 is talking, a siren starts to ring to announce the launch of the nuclear missile. The world is about to end and the entire room starts clapping."
            typewriter()
            print(red+"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                         (/ / //  /|//||||\\  \ \  \ _)
    """)
            nuclear_room()
        else:
            corridor()
    else:
        print("I dont understand, please try again")
        staff_room()

#-------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------#

intro()