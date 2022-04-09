
   
   
#imports are always on top
import random
import math
game = {}
game["gold"] = 0
game["xp"] = 1
game['health'] = 100
game['player_level'] = 1
game['enemy_level'] = 1
game['enemy_hp'] = 0
game['player_dmg'] = 0
game['enemy_dmg'] = 0
game['boss_hp'] = 500
game['rank'] = " "

c2a = ''
enemy = ['bat','undead soldier']
win1 = False

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
    global game
    print("your level is ",game['player_level'],)
    print("you have ",game['xp']," xp ")
    game['rank']=math.floor(game['player_level']/10)
    print("your current rank is ", game['rank'])

##gives the user the choices for the right path
def choice2():
    global game
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
        if village=='yes' or village=='y' and game['gold']>=100:
            game['gold']-=100
            villageinn(100)
        elif village=='yes' and game['gold']<100:
            print("You can not afford to heal you are {} gold short".format(100-game['gold']))
        if village=='no' or village=='n':
            print("You decide to leave the village and return to the crossroad")
            choice2()


##code for the village
def villageinn(healamount):
    global game
    print('you enter the inn\n')
    choiceinn=input('for 100 gold you can rest to full hp. Would you like to do so?\n')
    if choiceinn=='yes' or choiceinn=='y':
        game['health']=100
        game['gold'] -= 100
        print("you heal for {}".format(healamount))
        print("Now healed you leave the village and return to the crossroads")
        choice2()
    elif choiceinn=='no' or choiceinn=='n':
        print('you have have gone too far there is no turning back')
##end code for village


##code for battles
def attack2():
    global game
    global enemy
    randoms()
    game['enemy_hp']=game['enemy_level']*50
    print('A level',game['enemy_level'],enemy,' appears it has', game['enemy_hp'],'hp')
    c3b=input('fight or flee?\n')
    if c3b=='fight':
        while game['enemy_hp']>0 and game['health']>=1:
            game['health']=game['health']-game['enemy_dmg']
            print('The enemy did',game['enemy_dmg'],'damage','you have', game['health'],'health')
            if game['health']>=1:
                game['enemy_hp']=game['enemy_hp']-game['player_dmg']
                print('You did',game['player_dmg'],'damage','the enemy has', game['enemy_hp'],'hp\n')
            elif game['health']<=0:
                print("you die")
                break
        if game['enemy_hp']<=0:
            game['gold']+=50
            game['xp']+=game['enemy_level']*5
            game['player_level']=math.floor(game['xp']/10)
            ##print("you leveled up, you level is now",playerlevel)
            status()
            choice2()
    elif c3b=='flee':
        choice2()


def attack3():
    global game
    global enemy
    global c2a
    randoms()
    lastChance=input("Are you sure you want to progress, there is a strong enemy ahead?\n")
    if lastChance=='turn back' or lastChance=='back' or lastChance=='no':
        choice2()
    else:
        print("A goblin king appears, he towers over you")
        game['player_dmg']=game['player_dmg']+(2^game['player_dmg'])
        print('A Goblin King appears it has', game['boss_hp'],'hp')
        while game['boss_hp']>0 and game['health']>=0:
            bossdam=random.randint(20,100)
            game['health']=game['health']-bossdam
            print('The enemy did',bossdam,'damage','you have', game['health'],'health')
            game['boss_hp']=game['boss_hp']-game['player_dmg']
            print('You did',game['player_dmg'],'damage','the enemy has', game['boss_hp'],'hp\n')
        if game['boss_hp']<=0 and game['health']>0:
            game['gold']+=1000
            status()
            print("you win")
        if game['health']<=0:
            print("you died \n game over")


def attack1():
    global game
    global enemy
    global c2a
    global win1
    randoms()
    game['enemy_hp']=game['enemy_level']*50
    playerdam=game['player_dmg']+(2^game['player_level'])
    print('A level',game['enemy_level'],enemy,' appears it has', game['enemy_hp'],'hp')
    c3b=input('fight or flee?\n')
    if c3b=='fight':
        while game['enemy_hp']>0 and game['health']>=0:
            game['health']=game['health']-game['enemy_dmg']
            print('The enemy did',game['enemy_dmg'],'damage','you have', game['health'],'health')
            game['enemy_hp']=game['enemy_hp']-game['player_dmg']
            print('You did',game['player_dmg'],'damage','the enemy has', game['enemy_hp'],'hp\n')
        if game['enemy_hp']<=0:
            game['xp']+=game['enemy_level']*5
            status()
            game['gold']+=100
            win1=True
            scene1()
    elif c3b=='flee' and c2a=='north' or c2a=='n':
        scene1()

##end code for battles

##code for the inital choice
def scene1():
    global game
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
enemy = (enemy[random.randint(0, 1)])

def randoms():
    global game
    ## code for randomized variable
    game['enemy_level'] = random.randint(1,5)
    game['enemy_dmg'] = random.randint(5,10)
    game['player_dmg'] = random.randint(50,100)
scene1()
