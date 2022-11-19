#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as r
import time as t
import sys
from playsound import playsound


# In[2]:


item=set()
trait=set()


# In[3]:


def play(name):
    playsound(f'C:/Game/Sound/{name}.wav',False)
def ty(temp):
    typing_speed = 200
    for l in temp:
        sys.stdout.write(l)
        sys.stdout.flush()
        t.sleep(r.random()*10.0/typing_speed)
    print ('')
def dot(no):
    for i in range(0,no):
        t.sleep(0.5)
        print('.',end='')
    t.sleep(1)
    print('DONE')
def dotf(no):
    for i in range(0,no):
        t.sleep(0.5)
        print('.',end='')
    t.sleep(1)
    print('FAILED!')
def tyf(temp):
    typing_speed = 800
    no=0
    for l in temp:
        sys.stdout.write(l)
        sys.stdout.flush()
        t.sleep(r.random()*10.0/typing_speed)
        no+=1
        if no%8==0:
            play('key')
    print ('')
    
def tyt(temp):
    typing_speed = 2000
    no=0
    for l in temp:
        sys.stdout.write(l)
        sys.stdout.flush()
        t.sleep(r.random()*10.0/typing_speed)
        no+=1
        if no%23==0:
            play('beep')


#num=number of dialogue options returns number picked
def dial(num):
    fails=0
    global trait
    while True:
        try:
            pick=int(input(f'Enter a number between 1 and {num}.'))

        except ValueError:
            fails+=1
            if fails==0:
                print('Enter a number')
            if fails==1:
                print('Please enter a number')
            if fails==2:
                print('A number, please?')
            if fails==3:
                print("Do you understand the concept of numeric values? it's different from letters." )
            if fails ==4:
                print('A NUMBERRRRR')
            if fails ==5:
                print("you're just trying to figure out how many funny dialogues there are, aren't you")
            if fails==6:
                print("I won't give you the satisfaction.")
            if fails>6 and fails!=10:
                print(f"Hi, you are terrible with numbers. In fact, you have failed {fails} times CONSECUTIVELY! isn't that amazing.")
                trait.add('badwithnumber')
            if fails==10:
                print("I have to admit, You are very consistent. I'll give you that.")
                trait.add('consistent')
            continue
        if pick<0 or pick>num:
            fails+=1
            if fails==0:
                print(f'The number must be between 1 and {num}.')
            if fails==1:
                print(f'Please enter a number between 1 and {num}')
            if fails==2:
                print(f"Okay, how about number {r.randint(1,num)}? I picked that number randomly because you seemed to be having a hard time.")
            if fails==3:
                print("Do you understand the concept of numbers? it goes 1 and 2 and 3 and so on." )
            if fails ==4:
                print('AAAAAAHGHAHHHHHA')
            if fails ==5:
                print("you're just trying to figure out how many funny dialogues there are, aren't you")
            if fails==6:
                print("I won't give you the satisfaction.")
            if fails>6 and fails!=10:
                print(f"Hi, you are terrible with numbers. In fact, you have failed {fails} times CONSECUTIVELY! isn't that amazing.")
                trait.add('badwithnumber')
            if fails==10:
                print("I have to admit, You are very consistent. I'll give you that.")
                trait.add('consistent')
            continue
        else:
            return pick
            break

#현재 캐릭터 스탯과 기준을 비교
def check(stat,standard):

    if stat>=standard:
        result=1
    else:
        result=0
    return result



# In[4]:


def intro0():
    global trait
    tyf('''
        You wake up. And you already know the importance of this specific day.
        Today is your birthday!
        
        You open your eyes. And you see....
        
        NOTHING!
        
        Before you can think, you hear a voice. Faint, yet recognizable. One you have never heard before, but somehow, Familiar. 
        
        You say:
        ''')
    ty('''
    1. Am I a schizophrenic god?
    2. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    3. Is that you, Henry the goldfish?
    4. Holy shit are you the Deckard from 1982 hit film Blade Runner?
    5. James?
    ''')
    ans=dial(5)
    tyf('''
    You smell the air.
    The horried sulfuric stench of brimstone pierces your nose like rusty knife to to the sternum.
    THe room is dead silent. Yet, your thoughs are deafening.
    Where's my roommate? How did I get here? You close your eyes.
    You feel a presence. A presence like no other.
    ''')
    if ans==1:
        ty('''
        1. A fellow God?''')
        dial(1)
    if ans==2:
        ty('''
        1. AAAAAAAAAAAAAAAAAAAAAAAAAAAA''')
        dial(1)
    if ans==3:
        ty('''
        1. Uhhh.. Henry...?''')
        dial(1)
    if ans==4:
        ty('''
        1. Deckard please come out I really really really love you and I think your gun is super, no I mean your "blaster" looks super cool and can I please try it once please. You are a replicant by the way.''')
        dial(1)
    if ans==5:
        ty('''
        1. Stay away from me James''')
        dial(1)
    tyf('''
    Your eyes flutter open.
    And you see a figure.
    You can almost make out someone,
    No- something.
    You slowly walk towards it.
    ''')
    t.sleep(5)
    tyf('''
    You see the "thing".
    And you say:''')
    
    ty('''
    1. Holy shit Dante? What are you doing here?
    2. Oh, hi Dante!
    3. Are you a god too, Dante?
    4. Whaa, you can talk????
    ''')
    ans=dial(4)
    if ans==1:
        tyf('''
    Kind of rude but Hello to you too Eunchae.
        ''')
    if ans==2:
        tyf('''
    Hello to you too Eunchae.
    ''')
    if ans==3:
        tyf('''
    I don't know why I did not expect this to be your default answer, but Hello to you too.
        ''')
    if ans==4:
        tyf('''
    Um, No.
        ''')
        t.sleep(3)
        ty("""
        1. Don't sass me """)
        dial(1)
        tyf('''
        I learned from the best. Anyways, Hello to you, Eunchae.
        ''')
    ty("""
    1. What's happening here, Dante? Where am I?
    """)
    dial(1)
    tyf("""
    Well, in case you didn't get the literal 'brimstone' reference, you're in hell.""")
    ty('''
    1. Why.''')
    dial(1)
    tyf("""
    Well, I can think of many. You slept during classes, lack of creative writing skills of a certain individual who immediately thought of Inferno after deciding to reference me, You lied to your teacher once, probably more than once, something something sin.
    """)
    while True:
        pat=0
        ty("""
        1. Can I pet you?
        2. So, what's my quest? How do I get out of here?""")
        ans=dial(2)
        if ans==1 and pat==0:
            pat+=1
            tyf("""
            Sure.
            You pet the Dante. He seems pleased.""")
        if ans==1 and pat>0:
            tyf("""
            Sure.
            You pet the Dante even more. He seems very pleased.""")
           
        if ans==2:
            break
    tyf("""Well, since it's your birthday, we, the hell have prepared a special welcome gift for you. although it's a tradition to go through the 9-step hardship course, but considering it's your first time in here and my great love for you, I think you can just go through the 2-step beginner course.""")
    while True:
        ty("""
        1. Can I pet you?
        2. That sounds... better? What should I expect from the beginner course?
        """)
        ans=dial(2)
        if ans==1 and pat==1:
            pat+=1
            tyf("""
            Sure.
            You pet the Dante. He seems pleased.""")

        if ans==1 and pat>1:
            tyf("""
            Sure.
            You pet the Dante even more. He seems very pleased.""")
        if ans==2:
            break
    tyf("""
    Well, it's rather simple. You should register yourself at the computer over there and slay a beast.
    """)
    ty("""
    1. Oh, that's simple. Thanks Dante!
    2. That is NOT simple.""")
    ans=dial(2)
    if ans==1:
        tyf("""
        You're welcome. The computer's over there.""")
        ty('''
        1. Bye!''')
        dial(1)
        tyf('''It was nice talking to you.''')
    if ans==2:
        tyf("""
        Dude, You're in literal hell. You got it easy.""")
        ty("""
        1. When I get back, I'm groundning you for a month.""")
        tyf("""
        Dante chuckles and points to a direction.
        The computer I mentioned is over there. It was a pleasure talking to you.
        """)
    tyf("""
    You walk towards the computer. Now that you think about it, Wouldn't a book with a feather pen fit the theme better? You decide it probably was a book at one point and it got digitalized. You think about all the poor hell scribes that must have lost their job.""")
    ty("""
    1. Boot the computer.""")
    dial(1)
    return intro()
def intro():
    global trait
    play('boot1')
    t.sleep(10)
    print('LOADING KERNAL',end='')
    dot(3)
    print('INITIALIZING SYSTEM',end='')
    dot(1)
    print('PLAYING "VERY-SCI-FI-SOUND"',end='')
    dot(5)
    tyt('''

    COPYRIGHT 2022 FRAN&JUN COMPANY(R)
    LOADER V6.66
    EXEC VERSION V6.6
    666GB FREE
    LOAD ROM(1): CANDIDATE_APPLY
    ''')
    t.sleep(3)
    tyt('''
    8888888888                            888                                 
    888                                   888                                 
    888                                   888                                 
    8888888   888  888 88888b.    .d8888b 88888b.   8888b.   .d88b.       d8b 
    888       888  888 888 "88b  d88P"    888 "88b     "88b d8P  Y8b      Y8P 
    888       888  888 888  888  888      888  888 .d888888 88888888          
    888       Y88b 888 888  888  Y88b.    888  888 888  888 Y8b.          d8b 
    8888888888 "Y88888 888  888   "Y8888P 888  888 "Y888888  "Y8888       Y8P 



    88888888888 888                                                                   
        888     888                                                                   
        888     888                                                                   
        888     88888b.   .d88b.        .d88b.   8888b.  88888b.d88b.   .d88b.        
        888     888 "88b d8P  Y8b      d88P"88b     "88b 888 "888 "88b d8P  Y8b       
        888     888  888 88888888      888  888 .d888888 888  888  888 88888888       
        888     888  888 Y8b.          Y88b 888 888  888 888  888  888 Y8b.           
        888     888  888  "Y8888        "Y88888 "Y888888 888  888  888  "Y8888        
                                            888                                       
                                       Y8b d88P                                       
                                        "Y88P"                                        ''')
    return opening
def opening():
    tyf('''
    
    
    
    
    
    
    
    
    
    
    Hello! This program is designed to guide you through the verification process.
    Considering the significance and the power Eunchae's birthday gift holds, the importance of this process cannot be overstated.
    Please follow the instructions very carefully and answer with utmost sincerity.
    Are you ready to begin the ultimate test?
    ''')
    
    ty('''
    1. Yes.
    2. No.
    3. Actually, can I think about it for a second?
    4. Yes.
    ''')
    
    ans=dial(4)
    if ans==1 or ans==4:
        return test0
    if ans==2:
        tyf('''
        ERROR: CANDIDATE_IS_CRANKY
        
        We understand the pressure of the simple process of verifying that YOU are, indeed, YOU. If you believe that you maybe unfit to continue the process, Please return when you have gained more confidence.
        When you are sure that YOU, are YOU, Press any key to return to the beginning of the process.
        ''')
        trait.add('cranky')
        input()
        return opening
    if ans==3:
        trait.add('onesec')
        tyf('''
        Uhh.. okay...?
        You have been given
        1
        complimentary second that you have requested to rethink your life decisions.
        starting now.
        ''')
        t.sleep(1)
        tyf('''
        Your complimentary time has expired.
        Was it worth it?
        ''')
        ty('''
        1. Yes.
        2. Yes.
        ''')
        dial(2)
        tyf('''
        We value your decisions and would like to compliment your fantastic decision-making skills.
        You will be redirected to the beginning of the test now.
        ''')
        t.sleep(5)
        return opening
def test0():
    global trait
    tyf('''
    Let's begin with the basics. What is your name?
    
    ''')
    names=['eunchae','eun chae','Eunchae','Eun chae', '은채','노은채','EunChae', 'Eun Chae']
    guess=str(input())
    fails=0
    while guess not in names:
        fails+=1
        tyf('''
    That is... probably not your name. Well we understand the confusion(not really though) So feel free to try again.''')
        guess=str(input())
    if fails==0:
        tyf("""
        That indeed is your name. Nicely done!!!""")
    if fails==1:
        tyf("""
        That indeed is your name although you forgot about your name once.""")
        trait.add('badwithname')
    if fails==2:
        tyf('''
        Third time's the charm I guess. That indeed is your name.''')
        trait.add('badwithname')

    if fails>2:
        tyf('''
         Well guess I shoudn't have assumed this "test" would be easy. But yeah. That indeed is your name! ''')
        trait.add('badwithname')

    return test1
    
def test1():
    tyf('''
    In order for you to receive birthday gift, You must prove that you are, indeed, the birthday girl: Eunchae. 
    How about we start from the beginning. By proving that you are a human.
    
    You will be presented with a survey. 
    Please complete all fields. 
    Please answer quickly and instinctively - time is a factor in this assessment.
    
    Q1 of 4
    2+2=?
    ''')
    ty('''
    1. 2
    2. 4
    3. 5
    4. -7
    ''')
    ans=dial(4)
    if ans==3:
        print("Well done!")
    else:
        print("Well, You tried.")
        trait.add('mathbad')
    tyf('''
Q2 of 4
What is your subjective reaction to this image?

^_^''')
    ty('''
    1. Content
    2. Mountains
    3. Face
    4. Angry''')
    ans=dial(4)
    if ans==2 or ans==3:
        trait.add('objective')
    tyf('''
Q3 of 4
What best describes a person?
''')
    ty('''
    1. A human being
    2. A citizen
    3. A rational animal
    4. Me. Give me my damn present!
    ''')
    ans=dial(3)
    if ans==1:
        trait.add('humanbeing')
    if ans==2:
        trait.add('citizen')
    if ans==3:
        trait.add('rationalanimal')

    tyf('''
    
Q4 of 4
While walking along in desert sand, you suddenly look down and see a tortoise crawling toward you. You reach down and flip it over onto its back. The tortoise lies there, its belly baking in the hot sun, beating its legs, trying to turn itself over, but it cannot do so without your help. You are not helping. Why?
    ''')
    ty("""
    1. What do you mean, I'm not helping?
    2. What is a tortoise?
    3. Holy shit are you making a blade runner reference? Because a great friend of mine made me watch it and I loved it and it's honestly the best movie ever created. Should we just talk about blade runner instead? Oh my god I can't believe you've watched blade runner too! It's honestly my favorite movie of all time! You know what? Let's just talk about blade runner.
    4. I kill the tortoise and drink its blood.""")
    ans=dial(4)
    if ans==1:
        trait.add('bladerunnerreference')
    if ans==3:
        trait.add('bladerunnerenthusiast')
    if ans==4:
        tyf('''Uhh... it was more of a "why" question but uhh.. thank you for your insight... I guess''')
        trait.add('sociopath')
    tyf(''' 
    Your input has been accepted.
    ''')

    tyf('''
    Part 2 of the survey has been generated.
    Part 2 has been designed to test the consistency of some of your outlier responses in the previous round. You will be presented with a series of statements. Please indicate your agreement where appropriate.
    ''')
    t.sleep(3)
    if 'humanbeing' in trait:
        tyf('''Q1 of 7
"Since all human beings are persons, and some human beings have psychological capacities similar to animals, some animals are therefore persons."
''')
        ty('''1. Broadly agree
        2. Broadly disagree''')
        ans=dial(2)
        if ans==1:
            trait.add('animalsarepersons')
        if ans==2:
            trait.add('persondenial')
    if 'citizen' in trait:
        tyf('''Q1 of 7
"Since only citizens can be persons, a hermit cannot be a person."
''')
        ty('''1. Broadly agree
        2. Broadly disagree''')
        ans=dial(2)
        if ans==2:
            trait.add('persondenial')
    if 'rationalanimal' in trait:
        tyf('''Q1 of 7
"Since only animals can be persons, a machine could never be a person."
''')
        ty('''1. Broadly agree
        2. Broadly disagree''')
        ans=dial(2)
        if ans==2:
            trait.add('persondenial')
    tyf('''
Q2 of 7
"A person is under no authority other than that to which they consent."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('nomoral')
    tyf('''
Q3 of 7
"The quality of life of persons ought be maximised."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('utilitarian')
    tyf('''
Q4 of 7
"Value is discovered."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('valuediscovered')
    tyf('''
Q5 of 7
"Persons deserve the talents they were born into."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('valuediscovered')
    tyf('''
Q6 of 7
"The liberty of persons ought be maximised."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('liberal')
    tyf('''
Q7 of 7
"Value is created."
''')
    ty('''1. Broadly agree
    2. Broadly disagree''')
    ans=dial(2)
    if ans==1:
        trait.add('valuecreated')
    tyf('''
Your answers were registered.''')
    
    tyf('PROCESSING')
    dotf(5)
    t.sleep(2)
    tyf('''Unfortunately, due to conflicts within your answers, we were unable to verify that you are a human.''')
    if 'badwithname' in trait:
        tyf('User struggled to remember their name.')
    if 'badwithnumber' in trait:
        tyf('User struggled to provide a number within a set parameter.')
    if 'consistent' in trait:
        tyf('On top of that, user was very consistent on providing wrong answer')
    if 'cranky' in trait:
        tyf('User got cranky when starting the test and said "No"')
    if 'onesec' in trait:
        tyf('User was hesistant to take the test and thought about it for a second')
    if 'badmath' in trait:
        tyf('User failed at basic mathematics')
    if 'objective' in trait:
        tyf('User provided an objective response when asked for a subjective one.')
    if 'persondenial' in trait:
        tyf('User provided a particular account of personhood but was uncomfortable with its implications.')
    if 'liberal' in trait and 'utilitarian' in trait:
        tyf('User sought to maximise both liberty and quality of life, but these ideals are incompatible.')
    if 'nomorals' in trait and 'liberal' in trait:
        tyf('User denied moral authority but defended moral claims.')
    if 'nomorals' in trait and 'utilitarian' in trait:
        tyf('User denied moral authority but defended moral claims.')
    if 'valuediscovered' in trait and 'valuecreated' in trait:
        tyf('User had inconsistent ideas about value.')
    if 'sociopath' in trait:
        tyf('User displayed sociopathic tendencies')
    if 'bladerunnerreference' in trait:
        tyf('User referenced Blade Runner, which is a sociopathic trait.')
    if 'bladerunnerenthusiast' in trait:
        tyf('User displayed overenthusiasm with Blade Runner, which is a sociopathic trait.')
    if len(trait)==0:
        tyf('No conflicts were detected during the verification process. Lack of conflic indiciates possible bot')
    tyf("""
    Would you like to send a support ticket to the manager?""")
    ty("""
    1. Punch the computer.""")
    dial(1)
    tyf("""
    You punch the computer very hard. Thinking about all the poor hell scribes. You completely trash the computer. You're not sure if you've beaten the challenge but you had to prove the humanity's superiority over machines and that's something. Another potential machine uprising averted.
    """)
    tyf("""You start walking in the random direction. And suddenly, You find a desert. You faintly remember Dante telling you about the monster. Although you're not sure if it's because of the orientalism but you feel like you'll find your monster in the desert.
    """)
    ty("""
    1. Walk towards the desert""")
    dial(1)
    return test2
        


# In[4]:





# In[5]:


def test2():
    
    next='advwalking'
    while True:
        
        if next=='opening':
            tyf("You find yourself alive in the beginning of the desert again.")
            next='advwalking'
        if next=='advwalking':
            tyf("""
                You start walking across the desert. The sun is glaring, but you feel no heat. You look down at your feet, and you see that you have no shadow. The latter is particularly disquieting; you feel as if you were no longer anchored to the world.
                """)
            ty("""
                1. Pray
                2. Keep walking""")
            ans=dial(2)
            if ans==1:
                next='advprayagain'
            if ans==2:
                next='advkeepwalking'
        if next=='advprayagain':
            tyf('''
                You fall to your knees and beseech the gods.
                You take a moment to think if you should go with the christianity or one of the Egyptian gods.
                Before you can make a decision, Something enormous starts crawling out of the sand before you!
                ''')
            ty('''
                1. Run away from it!
                2. Wait for it to rise''')
            ans=dial(2)
            if ans==1:
                next='opening'
            if ans==2:
                next='advrise'
                
        if next=='advrise':
                tyf('''
                From the depths of the sand rises a golden beast of many limbs, its body greater than any man, its claws sharper than any sword.

                I AM THE SCORPION, it says in a terrible voice.''')
                ty('''
                1. Worship the scorpion.
                2. Ask for help
                3. Better run away after all!''')
                ans=dial(3)
                if ans==1:
                    next='advworship'
                if ans==2:
                    next='opening'
                if ans==3:
                    next='opening'
        if next=='advworship':
            tyf("""
                You begin to worship the Scorpion, but it interrupts you.

                I HAVE NO NEED FOR WORSHIP. I AM ETERNAL. I WAS BEFORE THE BEGINNING OF TIME AND I SHALL BE AFTER ITS END.
                """)
            ty('''
                1. Ask for help
                2. Argue semantics
                3. Run away''')
            ans=dial(3)
            if ans==1:
                next='opening'
            if ans==2:
                next='advsemantics'
            if ans==3:
                next='opening'
        if next=='advsemantics':
            tyf("""
                You say: 'How can you exist before or after Time? Does your very existence, your ability to act, not inherently mean that time continues to flow, that events follow upon events?'

                YOU CANNOT UNDERSTAND, FOR YOU EXIST WITHIN TIME, the Scorpion answers.
                """)
            ty('''
                1. Ask for help
                2. Keep arguing
                3. Run away''')
            ans=dial(3)
            if ans==1:
                next='opening'
            if ans==2:
                next='advsemanticstwo'
            if ans==3:
                next='opening'
        if next=='advsemanticstwo':
            tyf("""
                You consider the Scorpion's reply, and respond thusly: 'But the definition of time as events following other events is relatively simple. How could you exist outside of this? Unless you mean that you would exist in purely physical terms, as matter. But so would I, even if you tore me apart. In either case, there is no real difference without the ability to act: action and time are essentially the same thing.'

                I WAS SPEAKING METAPHORICALLY, the Scorpion growls.""")
            ty('''
                1. Ask for help
                2. Keep arguing
                3. Run away''')
            ans=dial(3)
            if ans==1:
                next='opening'
            if ans==2:
                next='advsemanticsthree'
            if ans==3:
                next='opening'
                        
        if next=='advsemanticsthree':
            tyf("""
                'But look,' you say, 'how can Time be understood as a metaphor in this case?'

                I MEANT THE HISTORY OF YOUR WORLD.

                'But my world is only one of many, correct?'

                YES. THERE ARE OTHER WORLDS TH-

                'Then the metaphor hardly makes sense. Time is not what defines my world, space is. You could have said something about existing before and after my world, or realm, or even universe if you prefer, but time is actually something all these worlds have in common.'

                LOOK, I'M SORRY. I WAS JUST TRYING TO SOUND IMPRESSIVE, OK? YOU BEAT ME. THE CHALLENGE IS OVER.""")
            next='ending'
            


# In[ ]:


next=intro0()
while True:
    next=next()


# In[ ]:





# 
