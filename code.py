
   
   
#imports are always on top
import random
import math
gold=0
xp=1
health = 100
playerlevel = 1
enemylevel = 0
enemyhp = 0
c2a = ''
enemy = ['bat','undead soldier']
win1 = False
bosshp=500
rank=" "
##starting intro to game
print(" Hello there! Welcome to the world of Grimm!")
print("\nMy name is Arcus but you can call me The Narrator of this story, as well as the God of this world!")
print("\nThis world is a vast place, called Grimm inhabited by many creatures\n")
##start code for game endings
##trying to remove most deadends
def ending1():
    print('As you enter the cave the ceiling collapses behind you')
    print('You decide to leave the cave and emerge through a grove of trees into a forest')
    print('You settle down and live out the rest of your days alone in the peaceful forest\n')
    print('congrats you reached the first ending')
def bossfight():
    attack3()
##end code for ending
def status():
    global playerlevel
    global xp
    global rank
    print("your level is ",playerlevel,)
    print("you have ",xp," xp ")
    rank=math.floor(playerlevel/10)
    print("your current rank is ",rank)

##gives the user the choices for the right path
def choice2():
    global gold
    print('North of you you see a village \n to the northwest you see a forest and to the northeast you see a graveyard\n')
    choicetwob=input('choose either n, nw or ne\n')
    if choicetwob== 'northeast' or choicetwob== 'ne':
        print('You walk into the graveyard')
        attack2()
    elif choicetwob=='nw':
        bossfight()
    elif choicetwob=='n':
        print('you enter the village')
        village=input('as you enter the village one establishment stands out to you, the inn do you want to enter the inn?\n')
        if village=='yes' or village=='y' and gold>=100:
            gold-=100
            villageinn(100)
        elif village=='yes' and gold<100:
            print("You can not afford to heal you are {} gold short".format(100-gold))
        if village=='no' or village=='n':
            print("You decide to leave the village and return to the crossroad")
            choice2()


##code for the village
def villageinn(healamount):
    global health
    print('you enter the inn\n')
    choiceinn=input('for 100 gold you can rest to full hp. Would you like to do so?\n')
    if choiceinn=='yes' or choiceinn=='y':
        health=100
        print("you heal for {}".format(healamount))
        print("Now healed you leave the village and return to the crossroads")
        choice2()
    elif choiceinn=='no' or choiceinn=='n':
        print('you have have gone too far there is no turning back')
##end code for village


##code for battles
def attack2():
    global enemy
    global xp
    global gold
    global health
    global enemyhp
    global playerlevel
    randoms()
    enemyhp=enemylevel*50
    print('A level',enemylevel,enemy,' appears it has', enemyhp,'hp')
    c3b=input('fight or flee?\n')
    if c3b=='fight':
        while enemyhp>0 and health>=1:
            health=health-enemydam
            print('The enemy did',enemydam,'damage','you have', health,'health')
            if health>=1:
                enemyhp=enemyhp-playerdam
                print('You did',playerdam,'damage','the enemy has', enemyhp,'hp\n')
            elif health<=0:
                print("you die")
                break
        if enemyhp<=0:
            gold+=50
            xp+=enemylevel*5
            playerlevel=math.floor(xp/10)
            ##print("you leveled up, you level is now",playerlevel)
            status()
            choice2()
    elif c3b=='flee':
        choice2()
def attack3():
    global enemy
    global gold
    global c2a
    global bosshp
    global health
    global playerdam
    randoms()
    lastChance=input("Are you sure you want to progress, there is a strong enemy ahead?\n")
    if lastChance=='turn back' or lastChance=='back' or lastChance=='no':
        choice2()
    else:
        print("A goblin king appears, he towers over you")
        playerdam=playerdam+(2^playerdam)
        print('A Goblin King appears it has', bosshp,'hp')
        while bosshp>0 and health>=0:
            bossdam=random.randint(20,100)
            health=health-bossdam
            print('The enemy did',bossdam,'damage','you have', health,'health')
            bosshp=bosshp-playerdam
            print('You did',playerdam,'damage','the enemy has', bosshp,'hp\n') 
        if bosshp<=0 and health>0:
            gold+=1000
            status()
            print("you win")
        if health<=0:
            print("you died \n game over")
def attack1():
    global enemy
    global xp
    global gold
    global c2a
    global enemyhp
    global win1
    global health
    global enemydam
    global playerdam
    randoms()
    enemyhp=enemylevel*50
    playerdam=playerdam+(2^playerlevel)
    print('A level',enemylevel,enemy,' appears it has', enemyhp,'hp')
    c3b=input('fight or flee?\n')
    if c3b=='fight':
        while enemyhp>0 and health>=0:
            health=health-enemydam
            print('The enemy did',enemydam,'damage','you have', health,'health')
            enemyhp=enemyhp-playerdam
            print('You did',playerdam,'damage','the enemy has', enemyhp,'hp\n') 
        if enemyhp<=0:
            xp+=enemylevel*5
            status()
            gold+=100
            win1=True
            scene1()
    elif c3b=='flee' and c2a=='north' or c2a=='n':
        scene1()

##end code for battles

##code for the inital choice
def scene1():
    global c2a
    c1=input(' You find yourself in the center of a crossroad,Do you want to move west or move east? (type commands like w or west) \n')
    if c1=='east' or c1=='e':
        choice2()
        return
    if c1=='west' or c1=='w':
        print('You move west')
        c2a=input('You see a dark cave ahead of you to the north\n Do you move north or turn back?\n')
    if c2a=='north' or c2a=='n':
        print('You move into the dark cave\n')
        if win1==False:
            attack1()
        elif win1==True:
            ending1()
    elif c2a=='south' or c2a=='back' or c2a=='turn back':
        print('You move back to the crossroads ')
        scene1()
##end code for inital choice


'''{def win_graveyard():
    if choicetwob=='ne' or choicetwob=='nourtheast':
        print('You are in a graveyard, to the southwest there is a path that leads to a crossroad \n ')
        c3b=input('choose either village, nw or ne')
    if choicetwob== 'southwest' or c2b== 'sw':
        print('You walk back to the crossroads')
'''

##running all the functions to run the code
enemy = (enemy[random.randint(0,1)])
def randoms():
    global enemylevel
    global playerdam
    global enemydam
    ## code for randomized variable
    enemylevel = random.randint(1,5)
    enemydam = random.randint(5,10)
    playerdam = random.randint(50,100)
scene1()
