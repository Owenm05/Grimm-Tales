# #imports are always on top
import random
import math


class Game:
    def __init__(self, gold, xp, health):
        self.gold = gold
        self.xp = xp
        self.health = health
        self.max_health = health
        self.player_level = 1
        self.enemy_level = 1
        self.enemy_hp = 0
        self.player_dmg = 0
        self.enemy_dmg = 0
        self.boss_hp = 500
        self.rank = "stranger"
        self.hp_drinks = 0
        self.equipped_weapon = []
        self.prev_location = ""
        self.location = ""
        self.key_items = []
        self.equipped_chest
    def __str__(self):
        return "your level is " + str(self.player_level) + "; you have " + str(self.xp) + " xp" + "\nyou have " + str(self.health) + " hp; you have " + str(self.gold) + " gold" + "\nyour current rank is " + self.rank

    def die(self):
        print("you just died")

class Config:
    def __init__(self):
        self.hp_drink_price = 25
        self.hp_drink_hpower = 50 
        self.damask_sword_price = 1000
        self.damask_sword_atk = 100
        self.trident_price = 500
        self.trident_atk = 50

# #start code for game endings
# #trying to remove most deadends
def ending_cave_collapsed():
    print('As you enter the cave the ceiling collapses behind you')
    print('You decide to leave the cave and emerge through a grove of trees into a forest')
    print('You settle down and live out the rest of your days alone in the peaceful forest\n')
    print('congrats you reached the first ending')


def western_scene():
    global game
    game.location = "western scene"
    print('You moved west')
    decision = input('You see a dark cave ahead of you to the north\n Do you move north or turn back?\n')
    if decision == 'north' or decision == 'n':
        print('You move into the dark cave\n')
        diceD20 = random.randrange(1, 20)
        if diceD20 <= 18:
            attack_regular(western_scene)
        else:
            ending_cave_collapsed()
    elif decision == 'south' or decision == 'back' or decision == 'turn back':
        print('You move back to the crossroads ')
        game.prev_location = western_scene
        crossroads()


# #gives the user the choices for the right path
def eastern_scene():
    global game
    game.location = eastern_scene
    print('North of you you see a village \nto the northwest you see a forest and to the northeast you see a graveyard\n')
    decision = input('choose either n, nw or ne\n')
    if decision == 'northeast' or decision == 'ne':
        print('You walk into the graveyard')
        attack_regular(eastern_scene)
    elif decision == 'nw':
        bossfight(eastern_scene)
    elif decision == 'n':
        game.prev_location = eastern_scene
        village_scene()
    elif decision == 'w' or decision == 'west':
        game.prev_location = eastern_scene
        crossroads()

def northern_scene():
    global game
    game.location = northern_scene
    print('Two colossal stone statues stand on the sides of a gigantic stone gate.\nUpon closer inspection of the gate you find a keyhole at the base of one of the doors.')
    if 'ancient key' in game.key_items:
        print(" you unlock the gate with the ancient key. \n The sound of a powerful mechcanism at work can be heard as the gate slowly opens.\nIn the distance you see a mountain range commonly called The Severed Highlands.\n Would you like to go to The Severed Highlands, or turn back?")
        decision = input('choose either n, or s')
        if decision == 'north' or decision == 'n':
            print('You walk to the base of the nearest mountain')
                ##add mountain code
def southern_scene():
    global game
    game.location = southern_scene
    print('A vast expanse of golden sand stretches out just to the south of of you. The sandy dunes seem to continue far into the distance. Few have been known to survive the merciless sandstorms that are said to happen in the golden dunes.\n You see a merchent selling survival gear nearby\n')
    decision = input('choose either n, merchant, or s')
        if decision == 'north' or decision == 'n':
            print('You walk back to the crossroad')
            game.prev_location = southern_scene
            crossroads()
        if decision == 'merchant':
            enter_desert_market()
        elif decision == 'south' or decision == 's':
             if 'desert chestplate' in game.equipped_chest:
                print("Knowing you have the necessary gear to enter the desert, you walk to the Golden Dunes.\n ")
                game.prev_location = southern_scene
                golden_dunes_scene()
             elif 'desert chestplate' not in game.equipped_chest:
                print('You do not have the required gear to enter the Golden Dunes try going to the merchant')
                southern_scene()
def golden_dunes_scene():
    global game
    game.location = golden_desert_scene
    ##fill in rest of code
## code for the desert market
def enter_desert_market():
    global game
    shop_choice = input('''you see healing drinks, 50g each,
                       and a desert chestplate for 200g. 
                       You have {} gold.
                       What would you like to buy? drinks, or the desert chestplate?
                       Or you wanna leave?'''.format(game.gold))
    if (shop_choice == 'drink' or shop_choice == 'drinks'
            or shop_choice == 'healing drink' or shop_choice == 'healing drinks'):
        amount = input('input how many drinks you would like to buy\n')
        if game.gold >= int(amount) * 50:
            game.gold = game.gold - int(amount) * 50
            game.hp_drinks += int(amount)
            print("You bought your drinks and headed to the exit")
            southern_scene()
        else:
            print("you don't have enough money for that!")
            enter_desert_market()
    elif shop_choice == 'chestplate' or shop_choice == 'desert chestplate' or shop_choice == 'the desert chestplate':
        if game.gold >= 200:
            game.gold = game.gold - 200
            game.equipped_chest.append("desert chestplate")
            print("You bought your chestplate, equipped it and headed to the exit")
            southern_scene()
        else:
            print("you don't have enough money for that!")
            enter_desert_market()

def village_scene():
    print('you entered the village')
    village = input('''as you enter the village a few establishments stands out to you.
    There are inn, where you could be healed, and a shop, and road to exit of the village. 
    What do you like to visit?\n''')
    if village == 'inn' or village == 'i' and game.gold >= 100:
        villageinn()
    elif village == 'inn' and game.gold < 100:
        print("You can not afford to heal you are {} gold short".format(100 - game.gold))
    elif village == 'shop':
        enter_village_shop()
    if village == 'no' or village == 'n' or village == 'exit' or village == 'leave' or village == 'road':
        print("You decide to leave the village and return to the crossroad")
        eastern_scene()


##code for the shop
def enter_village_shop():
    global game
    shop_choice = input('''you see healing drinks, 25g each,
                       a trident for 500g and 
                       the damassk steel sword for 1,000g. 
                       You have {} gold.
                       What would you like to buy? drinks, trident or the sword?
                       Or you wanna leave?'''.format(game.gold))
    if (shop_choice == 'drink' or shop_choice == 'drinks'
            or shop_choice == 'healing drink' or shop_choice == 'healing drinks'):
        amount = input('input how many drinks you would like to buy\n')
        if game.gold >= int(amount) * 25:
            game.gold = game.gold - int(amount) * 25
            game.hp_drinks += int(amount)
            print("You bought your drinks and headed to the exit")
            village_scene()
        else:
            print("you don't have enough money for that!")
            enter_village_shop()
    elif shop_choice == 'sword' or shop_choice == 'the sword' or shop_choice == 'the damassk steel sword':
        if game.gold >= 1000:
            game.gold = game.gold - 1000
            game.equipped_weapon.append("damassk sword")
            print("You bought your sword, swing it over your shoulder and headed to the exit")
            village_scene()
        else:
            print("you don't have enough money for that!")
            enter_village_shop()
    elif shop_choice == 'trident':
        if game.gold >= 500:
            game.golf = game.gold - 1000
            game.equiped_weapon.append("trident")
            print("You bought your trident, swung it over your shoulder and headed to the exit")
            village_scene()
        else:
            print("you dont have enough money for that!")
            enter_village_shop()
            
            
    else:
        village_scene()


##code for the village
def villageinn():
    global game
    print('you enter the inn\n')
    choiceinn = input('for 100 gold you can rest to full hp. Would you like to do so?\n')
    if choiceinn == 'yes' or choiceinn == 'y':
        healamount  = game.max_health - game.health
        game.health = game.max_health
        game.gold  -= 100
        print("you heal for {}".format(healamount))
        print("Now healed you leave the village and return to the crossroads")
        village_scene()
    elif choiceinn == 'no' or choiceinn == 'n':
        print('you have have gone too far there is no turning back')


##end code for village

def get_hero_dmg():
    global game, gconfig
    calc_player_dmg = game.player_dmg + (2 ^ game.player_level)
    if 'damassk sword' in game.equipped:
        calc_player_dmg += gconfig.damask_sword_atk
        print('your attack is improved by your damassk sword')
    elif 'trident' in game.equipped:
        calc_player_dmg += gconfig.trident_atk
        print('your attack is improved by your trident')
    return calc_player_dmg


##code for battles
def attack_regular(previous_scene):
    global game, gconfig
    global enemy
    randoms()
    game.enemy_hp = game.enemy_level * 50
    print('A level', game.enemy_level, enemy, ' appears it has', game.enemy_hp, 'hp')
    decision = input('fight or flee?\n')
    if decision == 'fight' or decision =='1':
        player_dmg = get_hero_dmg()    
        while game.enemy_hp > 0 and game.health >= 1:
            game.health = game.health - game.enemy_dmg
            print('The enemy did', game.enemy_dmg, 'damage,', 'you have', game.health, 'health')
            if game.health >= 1:
                if game.health < 25 and game.hp_drinks > 0:
                    game.hp_drinks -= 1
                    game.health    += 50
                    print("you drink a hp drink vital and restored 50 health by this")
                game.enemy_hp = game.enemy_hp - player_dmg
                if game.enemy_hp <= 0:
                    game.enemy_hp=0
                print('You did', player_dmg, 'damage,', 'the enemy has', game.enemy_hp, 'hp\n')
            elif game.health <= 0:
                print("you die")
                if game.player_level >= 2:
                    break
        if game.enemy_hp <= 0:
            game.gold += 50
            game.xp += game.enemy_level * 3
            game.player_level = math.floor(game.xp / 10)
            if game.player_level > 1:
                game.max_health = 100 + game.player_level * 5
            ##print("you leveled up, you level is now",playerlevel)
            print(game)
            previous_scene()
    elif decision == 'flee':
        previous_scene()
    else:
        print('no such way!')
        attack_regular()


def bossfight(previous_scene):
    global game, gconfig
    global enemy
    randoms()
    decision = input("Are you sure you want to progress, there is a strong enemy ahead?\n")
    if decision == 'turn back' or decision == 'back' or decision == 'no':
        previous_scene()
    else:
        print("A Goblin King appears, he towers over you")
        print('And he has', game.boss_hp, 'hp')
        player_dmg = get_hero_dmg
        while game.boss_hp > 0 and game.health >= 0:
            bossdam = random.randint(20, 100)
            game.health = game.health - bossdam
            print('The enemy did', bossdam, 'damage,', 'you have', game.health, 'health')
            if game.health < 25 and game.hp_drinks > 0:
                game.hp_drinks -= 1
                game.health += 50
                print("you drink a hp drink vital and restored 50 health by this")
            game.boss_hp = game.boss_hp - player_dmg
            print('You did', player_dmg, 'damage,', 'the enemy has', game.boss_hp, 'hp\n')
        if game.boss_hp <= 0 and game.health > 0:
            game.gold += 1000
            game.xp   += 100
            game.player_level = math.floor(game.xp / 10)
            if game.player_level > 1:
                game.max_health = 100 + game.player_level * 5
            game.status()
            game.key_items.append('ancient key')
            print("you have obtained the ancient key, maybe it opens something?")
            previous_scene()
        if game.health <= 0:
            print("you died \n game over")


##end code for battles

##code for the inital choice
def crossroads():
    global game
    game.location = "crossroads"
    # TBC - to be created by gods of the World
    print('''The World's Map on The Crossroads Sign:
    
                              The Severed Highlands===Abyssal Depths
                                         ||
               Peaceful Forest      Colossal Gate
                       ||                ||
                    Dark Cave         North         Forest   Village   Graveyard
                       ||                ||            \\\     ||      ///
TBC===Ocean===Beach===West==========Crossroads================East==============TBC
                                         ||                    || 
                                        South             Broken Portal      
                                         ||
                  Desert Village===Golden Dunes===Serpent's Den
          ''')
    decision = input(
        '''You find yourself at The Crossroad, which seems the center of the world.
Do you want to move west, north, or move east? (type commands like w or west) \n''')

    if decision == 'east' or decision == 'e':
        game.prev_location = crossroads
        eastern_scene()
        return
    if decision == 'west' or decision == 'w':
        game.prev_location = crossroads
        western_scene()
    if decision == 'north' or decision == 'n':
        game.prev_location = crossroads
        northern_scene()
    if decision == 'help':
        print('please, type west, east, or north\n')
        crossroads()
##end code for the crossroads scene


def randoms():
    global game
    ## code for randomized variable
    game.enemy_level = random.randint(1, 5)
    game.enemy_dmg = random.randint(5, 10)
    game.player_dmg = random.randint(50, 100)


if __name__ == "__main__":
    game = Game(0, 1, 100)
    game.prev_location = ""
    gconfig = Config()
    enemy = ['bat', 'undead soldier']
    enemy = (enemy[random.randint(0, 1)])
    # #starting intro to game
    print(" Hello there! Welcome to the world of Grimm!")
    print("\nMy name is Arcus but you can call me The Narrator of this story, as well as the God of this world!")
    print("\nThis world is a vast place, called Grimm inhabited by many creatures\n")
    crossroads()

