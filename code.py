# #imports are always on top
import random


class Game:
    def __init__(self, gold, xp, health):
        self.gold = gold
        self.xp = xp
        self.quest = ""
        self.health = health
        self.max_health = health
        self.player_level = 1
        self.enemy_level = 1
        self.str = 5
        self.dex = 5
        self.con = 5
        self.unspent_points = 0
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
        self.equipped_chest = []
        self.equipped_legs = []
        self.equipped_feet = []
        self.equipped_head = []

    def __str__(self):
        return "your level is " + str(self.player_level) + "; you have " + str(self.xp) + " xp" + "\nyou have " + str(self.health) + " hp; you have " + str(self.gold) + " gold" + "\nyour current rank is " + self.rank

    def die(self):
        dice_d20 = random.randrange(1, 20)
        if dice_d20 <= 18:
            print(dice_d20)
            print("you just died")
        else:
            print("looks like you could use some help, let me revive you")
            self.health = game.max_health
            if self.prev_location == "":
                self.prev_location = crossroads
            self.prev_location()


class Config:
    def __init__(self):
        self.levels = {1: 0, 2: 50, 3: 150, 4: 300, 5: 500, 6: 750, 7: 1050, 8: 1400, 9: 1800, 10: 2300, 11: 2900, 12: 3600}
        self.hero_chance_to_hit = 0.7
        self.dex_accuracy_bonus = 0.01
        self.default_hero_health = 100
        self.hp_drink_price = 25
        self.hp_drink_hpower = 50 
        self.damask_sword_price = 1000
        self.damask_sword_atk = 100
        self.trident_price = 500
        self.trident_atk = 50
        self.scarab_blade_price = 5000
        self.scarab_blade_atk = 200
class Story:
    def __init__(self):
        self.beach_story = "you decide to walk barefoot along the clean beach. The waves lap at your feet. you can see someone standing on a dock in the distance"
        self.southern_story = 'A vast expanse of golden sand stretches out just to the south of of you.\n The sandy dunes seem to continue far into the distance. Few have been known to survive the merciless sandstorms that are said to happen in the golden dunes.\n You see a merchent selling survival gear nearby\n'
        self.eastern_story = "'North of you you see a village, to the west of you is a crossroad , to the northwest you see a forest\n South of you you see a portal that appears to be broken,  and to the northeast you see a graveyard\n"
# #start code for game endings
def ending_cave_collapsed():
    print('As you enter the cave the ceiling collapses behind you')
    print('You decide to leave the cave and emerge through a grove of trees into a forest')
    print('You settle down and live out the rest of your days alone in the peaceful forest\n')
    print('congrats you reached the first ending')


def western_scene():
    global game
    game.location = "western scene"
    print('You moved west')
    decision = input('You see a dark cave ahead of you to the north\n And a Sandy Beach to the west of you \nDo you move north, move west, or turn back?\n')
    if decision == 'north' or decision == 'n':
        print('You move into the dark cave\n')
        dice_d20 = random.randrange(1, 20)
        if dice_d20 <= 18:
            attack_regular(western_scene)
        else:
            ending_cave_collapsed()
    elif decision == 'south' or decision == 'back' or decision == 'turn back':
        print('You move back to the crossroads ')
        game.prev_location = western_scene
        crossroads()
    elif decision == 'west' or decision == 'w':
        print('you run to the sandy beach and dip your feet in the water')
        game.prev_location = western_scene
        beach_scene()

def beach_scene():
    print(gstory.beach_story)
    decision=input('would you like to go back to the entrance of the dark cave or check out the dock?')
    if decision == 'dock':
        game.prev_location = beach_scene
        
# #gives the user the choices for the right path
def eastern_scene():
    global game
    game.location = eastern_scene
    print(gstory.eastern_story)
    decision = input('choose either n, w, nw or ne\n')
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
    elif decision == 'help' or decision == 'h':
        print('ne, n, nw, w\n')
        eastern_scene()
    else:
        print('sorry, no such option is available\n')
        eastern_scene()


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


##code for desert path======================================================================================================
def southern_scene():
    global game
    game.location = southern_scene
    print(gstory.southern_story)
    decision = input('choose either north, merchant, or south\n')
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
    game.location = golden_dunes_scene
    ##fill in rest of code



# # code for the desert market
def enter_desert_market():
    global game, gconfig
    if game.player_level<50:
        shop_choice = input('''you see healing drinks, 50g each,
                           and a desert chestplate for 200g. 
                           You have {} gold.
                           What would you like to buy? drinks, or the desert chestplate?
                           Or you wanna leave?\n'''.format(game.gold))
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
    elif game.player_level>=50:
        shop_choice = input('''you see healing drinks for 50g each, A Scarab Blade for 5000g,
                           and a desert chestplate for 200g. 
                           You have {} gold.
                           What would you like to buy? drinks, or the desert chestplate?
                           Or you wanna leave?\n'''.format(game.gold))
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
        elif shop_choice == 'blade' or shop_choice == 'scarab blade' or shop_choice == 'a scarab blade':
            if game.gold >= gconfig.scarab_blade_price:
                game.gold = game.gold - gconfig.scarab_blade_price
                game.equipped_weapon.append("scarab blade")
                print("You bought a Scarab Blade, equipped it and headed to the exit")
                southern_scene()
            else:
                print("you don't have enough money for that!")
                enter_desert_market()


# -=start code for village=-
def village_scene():
    global game
    game.location = village_scene
    print('you entered the village')
    village = input('''as you enter the village a few establishments stands out to you.
    There are inn, where you could be healed,
    a guild where you could accept quests,
    a shop, where ammunitions could be bought,
    a hero screen, where stat points could be spent, 
    and road to exit of the village. 
    What do you like to visit?\n''')
    if village == 'inn' or village == 'i' and game.gold >= 100:
        villageinn()
    elif village == 'inn' and game.gold < 100:
        print("You can not afford to heal you are {} gold short".format(100 - game.gold))
    elif village == 'shop':
        enter_village_shop()
    elif village == 'guild':
        enter_village_guild()
    elif village == 'hero':
        game.prev_location = village_scene
        enter_hero_screen()
    if village == 'no' or village == 'n' or village == 'exit' or village == 'leave' or village == 'road':
        print("You decide to leave the village and return to the crossroad")
        eastern_scene()


def enter_hero_screen():
    global game
    game.location = enter_hero_screen
    print(f'''
hp  | {game.health} / {game.max_health}
str | {game.str}
dex | {game.dex}
con | {game.con}
You have {game.unspent_points} to improve stats.
    ''')
    if game.unspent_points>0:
        decision = input('Which one you want to improve you have {game.unspent_points}? str, dex, con? or leave to leave\n')
    else:
        decision = input('Nothing to do. leave?')
    if decision == 'str' and game.unspent_points > 0:
        game.str += 1
        game.unspent_points -= 1
        if game.unspent_points > 0:
            enter_hero_screen()
        game.prev_location()
    elif decision == 'dex' and game.unspent_points > 0:
        game.dex += 1
        game.unspent_points -= 1
        if game.unspent_points > 0:
            enter_hero_screen()
        game.prev_location()
    elif decision == 'con' and game.unspent_points > 0:
        game.con += 1
        game.unspent_points -= 1
        game.max_health = gconfig.default_hero_health + game.player_level * 5 + game.con * 10
        if game.unspent_points > 0:
            enter_hero_screen()
        game.prev_location()
    elif decision == "leave":
        game.prev_location()
    else:
        game.prev_location()


def enter_village_guild():
    global game
    print("the current quests availible are ")
    for x in questlist:
        print(x)
    decision = input("you have one avilible quest slot which quest would you like to take 1 or 2?\n")
    if decision == '1':
        print("you chose quest 1")
        game.quest = questlist[0]
        village_scene()
    elif decision == '2':
        print("you chose quest 2")
        game.quest = questlist[1]
        village_scene()


##code for the shop
def enter_village_shop():
    global game, gconfig
    shop_choice = input(f'''    You see healing drinks, {gconfig.hp_drink_price}g each,
a trident for {gconfig.trident_price} and 
the damassk steel sword for {gconfig.damask_sword_price}. 
You have {game.gold} gold.
What would you like to buy? drinks, trident or the sword?
Or you wanna leave?''')
    if (shop_choice == 'drink' or shop_choice == 'drinks'
            or shop_choice == 'healing drink' or shop_choice == 'healing drinks'):
        amount = input('input how many drinks you would like to buy\n')
        if game.gold >= int(amount) * gconfig.hp_drink_price:
            game.gold = game.gold - int(amount) * gconfig.hp_drink_price
            game.hp_drinks += int(amount)
            print("You bought your drinks and headed to the exit")
            village_scene()
        else:
            print("you don't have enough money for that!")
            enter_village_shop()
    elif shop_choice == 'sword' or shop_choice == 'the sword' or shop_choice == 'the damassk steel sword':
        if game.gold >= gconfig.damask_sword_price:
            game.gold = game.gold - gconfig.damask_sword_price
            game.equipped_weapon.append("damassk sword")
            print("You bought your sword, swing it over your shoulder and headed to the exit")
            village_scene()
        else:
            print("you don't have enough money for that!")
            enter_village_shop()
    elif shop_choice == 'trident':
        if game.gold >= gconfig.trident_price:
            game.gold = game.gold - gconfig.trident_price
            game.equipped_weapon.append("trident")
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
        print(game.max_health)
        healamount  = game.max_health - game.health
        game.health = game.max_health
        game.gold  -= 100
        print("you have restored {} hp in the inn".format(healamount))
        print("Now healed you leave the village and return to the crossroads")
        village_scene()
    elif choiceinn == 'no' or choiceinn == 'n':
        print('you have have gone too far there is no turning back')
##end code for village ============================================================================================================


def get_hero_dmg():
    global game, gconfig
    calc_player_dmg = game.player_dmg + (2 ^ game.player_level) + game.str * 5
    # please note, you should take in DECREMENTAL ORDER BY ATK POWER
    if 'scarab blade' in game.equipped_weapon:
        calc_player_dmg += gconfig.scarab_blade_atk
        print('your attack is improved by your scarab blade')
    elif 'damassk sword' in game.equipped_weapon:
        calc_player_dmg += gconfig.damask_sword_atk
        print('your attack is improved by your damassk sword')
    elif 'trident' in game.equipped_weapon:
        calc_player_dmg += gconfig.trident_atk
        print('your attack is improved by your trident')
    chance_to_hit = gconfig.hero_chance_to_hit + game.dex * gconfig.dex_accuracy_bonus
    print("Your chance to hit is",  (chance_to_hit*100),"%")
    # -=multiply by 100 for easy math=-
    chance_to_hit = chance_to_hit * 100
    roll_5d20 = random.randint(5, 100)
    if roll_5d20 < chance_to_hit:
        print("You rolled a  ", roll_5d20, "you hit")
    if roll_5d20 > chance_to_hit:
        # -= missed! =-
        calc_player_dmg = 0
    return calc_player_dmg


def check_new_level():
    global game, gconfig
    bool_level_changed = False
    while game.xp > gconfig.levels[game.player_level+1]:
        bool_level_changed = True
        game.player_level += 1
        game.unspent_points += 1
        stat_increase = random.randint(1, 3)
        if stat_increase == 1:
            game.str += 1
        elif stat_increase == 2:
            game.dex += 1
        elif stat_increase == 3:
            game.con += 1
    if bool_level_changed:
        game.max_health = gconfig.default_hero_health + game.player_level * 5 + game.con * 10


# -=code for battles=-
def attack_regular(previous_scene):
    global game, gconfig
    global enemy_zone_1
    randoms()
    game.enemy_hp = game.enemy_level * 50
    print('A level', game.enemy_level, enemy_zone_1, ' appears it has', game.enemy_hp, 'hp')
    decision = input('fight or flee?\n')
    if decision == 'fight' or decision =='1':
        while game.enemy_hp > 0 and game.health >= 1:
            game.health = game.health - game.enemy_dmg
            print('The enemy did', game.enemy_dmg, 'damage,', 'you have', game.health, 'health')
            if game.health >= 1:
                if game.health < 25 and game.hp_drinks > 0:
                    game.hp_drinks -= 1
                    game.health    += 50
                    print("you drink a hp drink vital and restored 50 health by this")
                player_dmg = get_hero_dmg()
                game.enemy_hp = game.enemy_hp - player_dmg
                if player_dmg == 0:
                    print('You missed!\n')
                else:
                    if game.enemy_hp <= 0:
                        game.enemy_hp=0
                    print('You did', player_dmg, 'damage,', 'the enemy has', game.enemy_hp, 'hp\n')
            elif game.health <= 0:
                game.die()
        if game.enemy_hp <= 0:
            game.gold += 50
            game.xp += game.enemy_level * 3
            check_new_level()
            print(game)
            previous_scene()
    elif decision == 'flee':
        previous_scene()
    else:
        print('no such way!')
        attack_regular(previous_scene)


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
        while game.boss_hp > 0 and game.health >= 0:
            bossdam = random.randint(20, 100)
            game.health = game.health - bossdam
            print('The enemy did', bossdam, 'damage,', 'you have', game.health, 'health')
            if game.health < 25 and game.hp_drinks > 0:
                game.hp_drinks -= 1
                game.health += 50
                print("you drink a hp drink vital and restored 50 health by this")
            player_dmg = get_hero_dmg()
            game.boss_hp = game.boss_hp - player_dmg
            if player_dmg == 0:
                print('You missed!\n')
            else:
                if game.enemy_hp <= 0:
                    game.enemy_hp = 0
                print('You did', player_dmg, 'damage,', 'the enemy has', game.enemy_hp, 'hp\n')
        if game.boss_hp <= 0 and game.health > 0:
            game.gold += 1000
            game.xp   += 500
            check_new_level()
            print(game)
            game.key_items.append('ancient key')
            print("you have obtained the ancient key, maybe it opens something?")
            previous_scene()
        if game.health <= 0:
            game.die()


##end code for battles======================================================================================================

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
Do you want to move west, south, north, or move east? (type commands like w or west) \n''')

    if decision == 'east' or decision == 'e':
        game.prev_location = crossroads
        eastern_scene()
        return
    elif decision == 'west' or decision == 'w':
        game.prev_location = crossroads
        western_scene()
    elif decision == 'north' or decision == 'n':
        game.prev_location = crossroads
        northern_scene()
    elif decision == 'south' or decision == 's':
        game.prev_location = crossroads
        southern_scene()
    elif decision == 'help':
        print('please, type west, east, or north\n')
        crossroads()
    elif decision == 'debug':
        game.die()
    else:
        print('sorry, no such option is available\n')
        crossroads()
    # #end code for the crossroads scene


def randoms():
    global game
    # -=code for randomized variable=-
    game.enemy_level = random.randint(1, 5)
    game.enemy_dmg = random.randint(5, 10)
    game.player_dmg = random.randint(50, 100)


if __name__ == "__main__":
    gconfig = Config()
    game = Game(10000, 1, gconfig.default_hero_health)
    game.prev_location = ""
    gstory = Story()
    enemy_zone_1 = ['bat', 'undead soldier']
    enemy_zone_1 = (enemy_zone_1[random.randint(0, 1)])
    questlist = ['1. slay 10 bats\n', '2. slay 10 undead soldiers']
    # #starting intro to game
    print(" Hello there! Welcome to the world of Grimm!")
    print("\nMy name is Arcus but you can call me The Narrator of this story, as well as the God of this world!")
    print("\nThis world is a vast place, called Grimm inhabited by many creatures\n")
    crossroads()
