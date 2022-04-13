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
        self.equipped = []
        self.prev_location = ""
        self.location = ""

    def status(self):
        print("your level is ", self.player_level, "; you have ", self.xp, " xp")
        print("you have ", self.health, " hp; you have ", self.gold, " gold")
        print("your current rank is ", self.rank)

    def die(self):
        print("you just died")


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
            attack_regular("western_scene")
        else:
            ending_cave_collapsed()
    elif decision == 'south' or decision == 'back' or decision == 'turn back':
        print('You move back to the crossroads ')
        game.prev_location = "western_scene"
        crossroads()


# #gives the user the choices for the right path
def eastern_scene():
    global game
    game.location = "eastern_scene"
    print('North of you you see a village \n to the northwest you see a forest and to the northeast you see a graveyard\n')
    decision = input('choose either n, nw or ne\n')
    if decision == 'northeast' or decision == 'ne':
        print('You walk into the graveyard')
        attack_regular("eastern_scene")
    elif decision == 'nw':
        bossfight("eastern_scene")
    elif decision == 'n':
        game.prev_location = "eastern_scene"
        village_scene()
    elif decision == 'w' or decision == 'west':
        game.prev_location = "eastern_scene"
        crossroads()


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
    shop_choice = input('''you see healing drinks, 25g each, and 
                       the damassk steel sword for 1,000g. 
                       You have {} gold.
                       What would you like to buy? drinks or the sword?
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
            game.equipped.append("damassk sword")
            print("You bought your sword, swing it over your shoulder and headed to the exit")
            village_scene()
        else:
            print("you don't have enough money for that!")
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


##code for battles
def attack_regular(previous_scene):
    global game
    global enemy
    randoms()
    game.enemy_hp = game.enemy_level * 50
    print('A level', game.enemy_level, enemy, ' appears it has', game.enemy_hp, 'hp')
    decision = input('fight or flee?\n')
    if decision == 'fight':
        player_dmg = game.player_dmg + (2 ^ game.player_level)
        if 'damassk sword' in game.equipped:
            player_dmg += 100
            print('your attack is improved by your damassk sword')
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
            game.status()
            globals()[previous_scene]()
    elif decision == 'flee':
        globals()[previous_scene]()


def bossfight(previous_scene):
    global game
    global enemy
    randoms()
    decision = input("Are you sure you want to progress, there is a strong enemy ahead?\n")
    if decision == 'turn back' or decision == 'back' or decision == 'no':
        globals()[previous_scene]()
    else:
        print("A Goblin King appears, he towers over you")
        print('And he has', game.boss_hp, 'hp')
        player_dmg = game.player_dmg + (2 ^ game.player_level)
        if 'damassk sword' in game.equipped:
            player_dmg += 100
            print('your attack is improved by your damassk sword')
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
            print("you win")
            globals()[previous_scene]()
        if game.health <= 0:
            print("you died \n game over")


##end code for battles

##code for the inital choice
def crossroads():
    global game
    game.location = "crossroads"
    # TBC - to be created by gods of the World
    print('''The World's Map on The Crossroads Sign:
    Dark Cave           TBC         Forest   Village   Graveyard
      ||                ||            \\\      ||      //
TBC==West==========Crossroads================East============TBC
      ||                ||                     ||
      TBC               TBC                   TBC       
          ''')
    decision = input(
        '''You find yourself at The Crossroad, which seems the center of the world.
Do you want to move west or move east? (type commands like w or west) \n''')

    if decision == 'east' or decision == 'e':
        game.prev_location = "crossroads"
        eastern_scene()
        return
    if decision == 'west' or decision == 'w':
        game.prev_location = "crossroads"
        western_scene()
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
    enemy = ['bat', 'undead soldier']
    enemy = (enemy[random.randint(0, 1)])
    # #starting intro to game
    print(" Hello there! Welcome to the world of Grimm!")
    print("\nMy name is Arcus but you can call me The Narrator of this story, as well as the God of this world!")
    print("\nThis world is a vast place, called Grimm inhabited by many creatures\n")
    crossroads()
