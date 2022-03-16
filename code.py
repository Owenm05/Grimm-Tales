
   
#imports are always on top
import random
gold=0
xp=1
health = 100
playerlevel = 1
enemylevel = 0
enemyhp = 0
c2a = ''
enemy = ['bat','undead soldier']
win1 = False


##start code for game endings
def ending1():
    print('As you enter the cave the ceiling collapses behind you')
    print('You decide to leave the cave and emerge through a grove of trees into a forest')
    print('You settle down and live out the rest of your days alone in the peaceful forest\n')
    print('congrats you reached the first ending')
def ending2():
    print ('A goblin horde surrounds you and defeats you')
    print('you die')
    print('you unlocked the second ending')
##end code for ending


##gives the user the choices for the right path
def choice2():
    global gold
    print('North of you you see a village \n to the northwest you see a forest and to the northeast you see a graveyard\n')
    choicetwob=input('choose either n, nw or ne\n')
    if choicetwob== 'northeast' or choicetwob== 'ne':
        print('You walk into the graveyard')
        attack2()
    elif choicetwob=='nw':
        ending2()
    elif choicetwob=='n':
        print('you enter the village')
        village=input('as you enter the village one establishment stands out to you, the inn do you want to enter the inn?\n')
        if village=='yes' or village=='y' and gold>=100:
            gold-=100
            villageinn(100)
        elif gold<100:
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
        print("you heal for {}".format(healamount))
        print("Now healed you leave the village and return to the crossroads")
        choice2()
    elif choiceinn=='no' or choiceinn=='n':
        print('you have have gone too far there is no turning back')
##end code for village


##code for graveyard battle
def attack2():
    global xp
    global gold
    global health
    global enemyhp
    global playerlevel
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
            xp+=enemylevel
            choice2()
    elif c3b=='flee':
        choice2()
##end code for graveyard battle


##start code for cave battle
def attack1():
    global xp
    global gold
    global c2a
    global enemyhp
    global win1
    global health
    enemyhp=enemylevel*50
    print('A level',enemylevel,enemy,' appears it has', enemyhp,'hp')
    c3b=input('fight or flee?\n')
    if c3b=='fight':
        while enemyhp>0:
            health=health-enemydam
            print('The enemy did',enemydam,'damage','you have', health,'health')
            enemyhp=enemyhp-playerdam
            print('You did',playerdam,'damage','the enemy has', enemyhp,'hp\n') 
        if enemyhp<=0:
            gold+=100
            xp+=enemylevel
            win1=True
            scene1()
    elif c3b=='flee' and c2a=='north' or c2a=='n':
        scene1()
##end code for graveyard battle


##code for the inital choice
def scene1():
    global c2a
    c1=input('You are at a crossroad,Do you want to move west or move east?\n')
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


def win_graveyard():
    if choicetwob=='ne' or choicetwob=='nourtheast':
        print('You are in a graveyard, to the southwest there is a path that leads to a crossroad \n ')
        c3b=input('choose either village, nw or ne')
    if choicetwob== 'southwest' or c2b== 'sw':
        print('You walk back to the crossroads')


##running all the functions to run the code
if __name__ == '__main__':
    ## code for randomized variable
    enemylevel = random.randint(1,5)
    enemydam = random.randint(5,10)
    playerdam = random.randint(50,100)
    enemynumber = random.randint(0,1)
    enemy = (enemy[random.randint(0,1)])

    scene1()

