# #imports are always on top
import random, math


class Game:
    def __init__(self, gold, xp, health,qp):
        global gconfig
        self.gold = gold
        self.xp = xp
        self.quest = [""]
        self.qp= qp
        self.gem_count=0
        self.str = random.randrange(1, 7)
        self.res = random.randrange(1, 7)
        self.dex = gconfig.points - self.str - self.res
        self.player_level = 1
        self.unspent_points = 0
        self.max_health = health + self.player_level * 5 + self.res * 10
        self.health = self.max_health
        self.enemy_level = 1
        self.enemy_hp = 0
        self.player_dmg = 0
        self.enemy_dmg = 0
        self.dungeon_kills = 0
        self.boss_hp = 500
        self.rank = "stranger"
        self.quest_points=1
        self.hp_drinks = 0
        self.equipped_weapon = []
        self.prev_location = ""
        self.location = ""
        self.key_items = []
        self.equipped_chest = []
        self.equipped_legs = []
        self.equipped_feet = []
        self.equipped_head = []
        self.player_status = []
        
    def __str__(self):
        return "your level is " + str(self.player_level) + "; you have " + str(self.xp) + " xp" + "\nyou have " + str(self.health) + " hp; you have " + str(self.gold) + " gold" + "\nyour current rank is " + self.rank + "\nyou have " + str(self.gem_count) + " gem/gems"

                
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
        self.levels = {1: 0, 2: 25, 3: 75, 4: 150, 5: 250, 6: 375, 7: 525, 8: 700, 9: 900, 10: 1150, 11: 1450, 12: 1800}
        self.ranks = {1: 1, 2: 5, 3: 10, 4: 20, 5: 40, 6: 80, 7: 160, 8: 320, 9: 640}
        self.points = 15
        self.hero_chance_to_evade = 0.1
        self.dex_evade_bonus = 0.01
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
        self.gods_bane_atk = 100000

class Story:
    def __init__(self):
        self.beach_story = "You decide to walk barefoot along the clean beach. The waves lap at your feet. you can see someone standing on a dock in the distance"
        self.southern_story = 'A vast expanse of golden sand stretches out just to the south of of you.\n The sandy dunes seem to continue far into the distance. Few have been known to survive the merciless sandstorms that are said to happen in the golden dunes.\n You see a merchent selling survival gear nearby\n'
        self.eastern_story = "'North of you you see a village, to the west of you is a crossroad, to the northwest you see a forest\n South of you you see a portal that appears to be broken,  and to the northeast you see a graveyard\n"
        self.dock_story = '''As you approach the man on the dock the man turns to face you, he then intoduces himself as the captain of a nearby vessal.\n
He claims to be able to be one of the few sailors to be able to cross the torental sea, but to do so it will cost you 100k gold.\n'''

        self.northern_story = '''you unlock the gate with the ancient key.\n 
The sound of a powerful mechanism at work can be heard as the gate slowly opens.\n
In the distance you see a mountain range commonly called The Severed Highlands.\n
Would you like to go to The Severed Highlands, or turn back?\n'''

# -=start code for game endings=-
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
            attack_regular(western_scene, 'dark cave')
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
    elif decision == 'help':
        help(game.location)

def dock_scene():
    global game
    game.location = dock_scene
    print(gstory.dock_story)
    decision = input("would you like to accept his offer, and attempt to cross the sea?\n") ##placeholder
    if decision == "yes" or decision == "y":
        if game.gold >= 100000:
            print('you accept his offer and cross the sea.')
            game.gold -= 100000
            print('you win')
            quit()
            ## new continent with many more adventures in stock, possibly start the second game here
        else:
            print("false")
        if game.gold < 100000:
            print("You dont have enough to do this try again at a later date")
            game.prev_location= dock_scene
            beach_scene()
        else:
            print("try again")
            dock_scene()
    elif decision == "no" or decision== "n":
        print(" you decline his offer and return to the beach")
        beach_scene()
        game.previous_location= dock_scene
    elif decision == "gold":
        game.gold += 100000000
        dock_scene()
    elif decision == "help" or decision == "Help":
        help(game.location)
    else:
        print(" that is not a choice")
        dock_scene()

    
def beach_scene():
    print(gstory.beach_story)
    decision = input('would you like to go back to the entrance of the dark cave or check out the sea?\n')
    if decision == 'sea':
        game.prev_location = beach_scene
        #dock_scene()
        decision2=input("are you sure this is a dungeon that could easily kill you, would you like to move forward?\n")
        if decision2=="y" or decision2=="yes":
            sea_scene()
    elif decision == 'cave' or decision == 'back':
        game.prev_location = beach_scene
        western_scene()
    elif decision == "help":
        help(game.location)
    else:
        print('location not found try again')
        beach_scene()
def sea_scene():
    global game,gconfig
    location = 'sea scene '
    stage = 1
    templocation = ''
    templocation+= location
    templocation += str(stage)
    game.location = sea_scene
    if game.dungeon_kills   < 8:
        game.dungeon_kills += 1
        attack_regular(sea_scene, templocation, True)
    elif 8 <= game.dungeon_kills   < 11:
        if game.dungeon_kills == 8:
            print('The Second stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
            while game.dungeon_kills<11:
                game.dungeon_kills += 1
                attack_regular(sea_scene, 'sea scene 2', True)
    elif 11 <= game.dungeon_kills and game.dungeon_kills < 12:
        if game.dungeon_kills == 11:
            print('The Third stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
        game.dungeon_kills += 1
        attack_regular(sea_scene, 'sea scene 3', True)
    elif game.dungeon_kills == 12:
        resetDungeons()
        game.key_items= game.key_items+ "Blue gem"
        print("you have gotten the blue gem as well as the scroll of power!")
        print("you read the scroll, written on it is the words 'The next stone was given to the demons by one of the former heros in exchange for near endless power.'\n")
        game.prev_location = sea_scene
        beach_scene()
# -=gives the user the choices for the right path=-
def eastern_scene():
    global game
    game.location = eastern_scene
    map(game.location)
    print(gstory.eastern_story)
    decision = input('choose either n, w, nw, s or ne\n')
    if decision == 'northeast' or decision == 'ne':
        print('You walk into the graveyard')
        attack_regular(eastern_scene, 'graveyard')
    elif decision == 'nw' and 'ancient key' not in game.key_items:
        bossfight(eastern_scene)
    elif decision == 'n':
        game.prev_location = eastern_scene
        village_scene()
    elif decision == 'w' or decision == 'west':
        game.prev_location = eastern_scene
        crossroads()
    elif (decision == 's' or decision == 'south') and "hero's quest" not in game.quest:
        game.prev_location = eastern_scene
        broken_portal()
    elif decision == 'nw' and 'ancient key' in game.key_items:
        print("you already have defeated this boss")
        eastern_scene()
    elif decision == 'help':
        help(game.location)
    else:
        print('sorry, no such option is available\n')
        eastern_scene()


def northern_scene():
    global game,gstory
    game.location = northern_scene
    print('''Two colossal stone statues stand on the sides of a gigantic stone gate.\n
Upon closer inspection of the gate you find a keyhole at the base of one of the doors.\n''')
    if 'ancient key' in game.key_items:
        print(gstory.northern_story)
        decision = input('choose either n, or s\n')
        if decision == 'north' or decision == 'n':
            print('You walk to the base of the nearest mountain')
            game.prev_location = northern_scene
            severed_highlands_scene()
        elif decision == 's' or decision == 'south':
            game.prev_location = game.location
            crossroads()
        elif decision == 'help':
            print('please, type south, or north\n')
    else:
        game.prev_scene = game.location
        print("finding no way to open the gate you return to the crossroads\n")
        crossroads()
def resetDungeons():
    global game
    print("you cleared the dungeon!")
    print("you got 10,000 gold as a reward")
    game.gold += 10000
    game.gem_count +=1
    game.dungeon_kills=0
    game.qp+=1
    print("you have ", game.qp,  " questpoints\n")
    print(game)
def severed_highlands_scene():
    global game
    game.location = severed_highlands_scene
    print("you can either go south to the gate or east to the abyssal depths\n")
    decision = input('choose either s or e\n')
    if decision == 's' or decision == 'south':
        print("You return to the gate\n")
        game.prev_location = severed_highlands_scene
        northern_scene()
    elif decision == 'e' or decision == 'east':
        if 'Purple gem' not in game.key_items and "hero's quest" in game.quest:
            print(" you see a deep pit and walk towards it\n")
            game.prev_location = severed_highlands_scene
            abyssal_depths_scene()
        elif "hero's quest" not in game.quest:
            print("you have no need to enter. Try to find the quest needed to enter.")
            severed_highlands_scene()
        elif "Purple gem" in game.key_items:
            print("you already have beaten this trial, there is no need to return.\n")
        elif decision == 'help':
            help(game.location)
        else:
            print("error")
            severed_highlands_scene()
def abyssal_depths_scene():
    global game,gconfig
    game.location = abyssal_depths_scene
    if game.dungeon_kills   < 8:
        game.dungeon_kills += 1
        attack_regular(abyssal_depths_scene, 'abyssal depths 1', True)
    elif 8 <= game.dungeon_kills   < 11:
        if game.dungeon_kills == 8:
            print('The Second stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
            while game.dungeon_kills<11:
                game.dungeon_kills += 1
                attack_regular(abyssal_depths_scene, 'abyssal depths 2', True)
    elif 11 <= game.dungeon_kills and game.dungeon_kills < 12:
        if game.dungeon_kills == 11:
            print('The Third stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
        game.dungeon_kills += 1
        attack_regular(abyssal_depths_scene, 'abyssal depths 3', True)
    elif game.dungeon_kills == 12:
        resetDungeons()
        game.key_items= game.key_items+"Purple gem"
        print("you have gotten the Purple gem, you see words inscribed in the wall next to the place where you found the stone")
        print(" you read the wall it says, ' look under the tides to find where the next stone hides'\n")
        game.prev_location = abyssal_depths_scene
        severed_highlands_scene()
def broken_portal():
    global game
    game.location = broken_portal
    print("you see a broken portal ahead of you\n")
    print("The portal has five slots; one slot had a gray gem embedded in the slot. A spirit appears and explains to you the story behind the portal. Once this land had bountiful resources and both the humans and demons lived peaceful lives. But this peace was not to last forever.  One day the Demon armies forces charged through the gate. They destroyed and pillaged everything in sight. Eventually The countries five hero's as well as thier armies stood against the demons in a long war. In the end only one hero remained. He defeated the demon king and returned the demons back to their home world. With the remainder of his strength he destroyed the demon's only way to return to our world, the portal. With the portal out of the way the hero hid the sacred gems throughout the world with the goal of the emons never being allowed to return again. But as of recently the demons have grown more powerful, and have found a way to create a new portal. All of the gems besides the gray one were eventually lost to time. It is now your job to find the remaining gems, repair the portal and defeat the demons that lay within.\n")
    print(" The sprit then reveals that he is the  ghost of that very hero who saved the world\n")
    if game.gem_count==3:
        print(" you enter the gems and the portal opens")
        
    decision = input('Would you like to accept this quest?\n')
    if decision == 'y' or decision == 'yes':
        if game.quest[0] != "hero's quest" or game.quest[1] != "hero's quest" or game.quest[2] != "hero's quest":
            print("You have accepted the hero's quest\n")
            game.quest[0]=("hero's quest")
            print("you have taken the quest. The spirit tells you the first gem resides where the serpant lies\n")
            game.prev_location = broken_portal
            eastern_scene()
        else:
            print("You already have this quest\n")
            broken_portal()
    elif decision == 'n' or decision == 'no':
        print("you decline the spirit. He replies 'feel free to reconsider!' you return to the east\n")
        game.prev_location = broken_portal
        eastern_scene()
    else:
        print("that is not an option please try again\n")
        broken_portal()
# -=code for desert path=-
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
        elif decision == 'help':
            print('please, type south, or north\n')

def golden_dunes_scene():
    global game
    game.location = golden_dunes_scene
    print('''you can move either west to the desert village, north back to the southern pass, or east to the Serpent's Den''')
    decision=input('choose either west, north, east\n')
    if decision == 'west' or decision == 'w':
        game.prev_location = golden_dunes_scene
        desert_village_scene()
    elif decision == 'east' or decision == 'e':
        game.prev_location = golden_dunes_scene
        if "hero's quest" in game.quest and "Yellow gem" not in game.key_items:
            desert_trial()
        elif "Yellow gem" in game.key_items:
            print("you already have beaten this trial, there is no need to return.\n")
            golden_dunes_scene()
        else:
            print("you don't have a reason to enter the serpent's den (maybe you are missing a quest?)\n")
            golden_dunes_scene()
    elif decision == 'n' or decision == 'north':
        game.prev_location == golden_dunes_scene
        southern_scene()
    elif decision == 'help':
        print('please, type west, east, or north\n')


def desert_trial():
    global game,gconfig
    game.location = desert_trial
    if game.dungeon_kills   < 8:
        game.dungeon_kills += 1
        attack_regular(desert_trial, 'desert trial 1', True)
    elif 8 <= game.dungeon_kills   < 11:
        if game.dungeon_kills == 8:
            print('The Second stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
            while game.dungeon_kills<11:
                game.dungeon_kills += 1
                attack_regular(desert_trial, 'desert trial 2', True)
    elif 11 <= game.dungeon_kills and game.dungeon_kills < 12:
        if game.dungeon_kills == 11:
            print('The Third stage of the Trial is starting!')
            hp_station = math.ceil(game.max_health*0.8)
            if game.health < hp_station:
                restored = hp_station - game.health
                game.health = hp_station
                print(f'The fountain of Health has restored {restored} HP!')
        game.dungeon_kills += 1
        attack_regular(desert_trial, 'desert trial 3', True)
    elif game.dungeon_kills == 12:
        resetDungeons()
        game.key_items= game.key_items+ "Yellow gem"
        print("you have gotten the Yellow gem as well as the sacred scroll!")
        print("you read the sacred scroll, written on it is the words 'The next stone can be found, way down deep under the ground.'\n")
        game.prev_location = desert_trial
        golden_dunes_scene()
    
    
def desert_village_scene():
    global game
    game.location = desert_village_scene
    print('you entered the desert village')
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
        game.prev_location = desert_village_scene
        enter_hero_screen()
    if village == 'no' or village == 'n' or village == 'exit' or village == 'leave' or village == 'road':
        print("You decide to leave the desert village and return to the golden dunes")
        golden_dunes_scene()


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
res | {game.res}
You have {game.unspent_points} to improve stats.
    ''')
    if game.unspent_points>0:
        decision = input('Which one you want to improve you have? str, dex, con? or leave to leave\n')
    else:
        decision = input('Nothing to do. leave?\n')
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
    decision = input("you have one availible quest slot which quest would you like to take 1 or 2?\n")
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


def calc_enemy_dmg(enemy_base_dmg):
    global game
    chance_to_evade = (round(gconfig.hero_chance_to_evade + game.dex * gconfig.dex_evade_bonus, 2))*100
    chance_to_evade = chance_to_evade
    roll_5d20 = random.randint(1, 100)
    status_inflict = random.randint(1,50+ game.res)
    if roll_5d20 <= chance_to_evade:
        print("Your chance to evade is ", chance_to_evade, "%")
        print("You rolled ", roll_5d20, ", and thus enemy missed")
        enemy_base_dmg = 0
    return enemy_base_dmg


def get_hero_dmg():
    global game, gconfig
    calc_player_dmg = game.player_dmg + (2 ^ game.player_level) + game.str * 5
    # please note, you should take in DECREMENTAL ORDER BY ATK POWER
    if 'gods_bane' in game.equipped_weapon:
        calc_player_dmg += gconfig.gods_bane_atk
    elif 'scarab blade' in game.equipped_weapon:
        calc_player_dmg += gconfig.scarab_blade_atk
        #print('your attack is improved by your scarab blade')
    elif 'damassk sword' in game.equipped_weapon:
        calc_player_dmg += gconfig.damask_sword_atk
        #print('your attack is improved by your damassk sword')
    elif 'trident' in game.equipped_weapon:
        calc_player_dmg += gconfig.trident_atk
        #print('your attack is improved by your trident')
    chance_to_hit = round(gconfig.hero_chance_to_hit + game.dex * gconfig.dex_accuracy_bonus, 2)*100
    roll_5d20 = random.randint(1, 100)
    if roll_5d20 > chance_to_hit:
        print("Your chance to hit is", chance_to_hit, "%")
        print("You rolled ", roll_5d20, ", and thus you have missed")
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
            game.res += 1
    if bool_level_changed:
        game.max_health = gconfig.default_hero_health + game.player_level * 5 + game.res * 10
def check_new_rank():
    global game, gconfig
    bool_rank_changed = False
    while game.qp > gconfig.ranks[game.rank+1]:
        bool_rank_changed = True
        game.rank += 1

# -=code for battles=-
def attack_regular(previous_scene, location=None, trial=False):
    global game, gconfig
    if not trial:
        print(location)
    if location == "desert trial 1":
        enemy_list = ['scorpion', 'snake']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "desert trial 2":
        enemy_list = ['champ of scroptions', 'champ of snakes']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "desert trial 3":
        enemy_list = ['manticore', 'sphinx']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "abyssal depths 1":
        enemy_list = ['lesser demon', 'ghoul']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "abyssal depths 2":
        enemy_list = ['shade', 'cursed golem']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "abyssal depths 3":
        enemy_list = ['soul eater', 'greater demon']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "sea scene 1":
        enemy_list = ['great white', 'pirate']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "sea scene 2":
        enemy_list = ['mermaid', 'giant squid']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "sea scene 3":
        enemy_list = ['kracken', 'ghoul pirates']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "graveyard":
        enemy_list = ['zombie', 'undead soldier', 'undead archer']
        enemy_name = enemy_list[random.randint(0, len(enemy_list)-1)]
    elif location == "dark cave":
        enemy_list = ['bat', 'spider', 'undead archer']
        enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
    else:
        enemy_list = ['bat', 'zombie', 'wolf', 'undead']
        enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
    randoms(location)
    game.enemy_hp = game.enemy_level * 50
    print('A level', game.enemy_level, enemy_name, ' appears it has', game.enemy_hp, 'hp')
    if location in ['desert trial 1', 'desert trial 2', 'desert trial 3', 'abyssal depths 1','abyssal depths 2','abyssal depths 3','sea scene 1', 'sea scene 2', 'sea scene 3']:
        decision = 'fight'
    else:
        decision = input('fight or flee?\n')
    if decision == 'fight' or decision =='1':
        while game.enemy_hp > 0 and game.health >= 1:
            enemy_dmg = calc_enemy_dmg(game.enemy_dmg)
            if enemy_dmg != 0:
                game.health = game.health - enemy_dmg
                print('The enemy did', enemy_dmg, 'damage,', 'you have', game.health, 'health')
            if game.health >= 1:
                if game.health < 25 and game.hp_drinks > 0:
                    game.hp_drinks -= 1
                    game.health += 50
                    print("you drink a hp drink vital and restored 50 health by this")
                player_dmg = get_hero_dmg()
                game.enemy_hp = game.enemy_hp - player_dmg
                if player_dmg != 0:
                    if game.enemy_hp <= 0:
                        game.enemy_hp=0
                    print('You did', player_dmg, 'damage,', 'the enemy has', game.enemy_hp, 'hp\n')
            elif game.health <= 0:
                game.die()
        if game.enemy_hp <= 0:
            game.gold += 50
            game.xp += game.enemy_level * 3
            check_new_level()
            ##check_new_rank()
            if not trial:
                print(game)
            previous_scene()
    elif decision == 'flee':
        previous_scene()
    else:
        print('no such way!')
        attack_regular(previous_scene, location)


def bossfight(previous_scene):
    global game, gconfig
    randoms()
    decision = input("Are you sure you want to progress, there is a strong enemy ahead?\n")
    if decision == 'turn back' or decision == 'back' or decision == 'no':
        previous_scene()
    else:
        print("A Goblin King appears, he towers over you")
        print('And he has', game.boss_hp, 'hp')
        while game.boss_hp > 0 and game.health >= 0:
            bossdam = random.randint(20, 100)
            bossdam = calc_enemy_dmg(bossdam)
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


# -=code for the inital choice=-
def map(scene):
    global game
    map = ''
    if game.location == "crossroads":
        map = '''The World's Map on The Crossroads Sign:

                      North    
                        ||           
        West========Crossroads========East
                        ||                    
                      South            
                               
          '''
    if game.location == "eastern_scene":
        map = '''The World's Map on The Crossroads Sign:

                     Forest   Village Graveyard
                          \\    ||    //
        Crossroads=============East
                                || 
                           Broken Portal 
                     
                               
          '''
    print(map)

def crossroads():
    global game, test2
    game.location = "crossroads"
    # TBC - to be created by gods of the World
    map(game.location)
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
        gconfig.hero_chance_to_evade = 0.1
        game.hp_drinks = 20
        game.dex = 999
        game.res = 999
        game.str = 999
        game.equipped_weapon = ['gods_bane']
        game.equipped_chest = ['desert chestplate']
        game.equipped_head = ['developers_crown']
        game.gold = 10000
        game.key_items=('ancient key')
        crossroads()
    else:
        print('sorry, no such option is available\n')
        crossroads()
    # #end code for the crossroads scene


def randoms(enemy_location=None):
    global game
    # -=code for randomized variable=-
    if enemy_location   == 'desert trial 2':
        game.enemy_level = random.randint(5, 7)
    elif enemy_location == 'desert trial 3':
        game.enemy_level = random.randint(7, 10)
    else:
        game.enemy_level = random.randint(1, 5)
    if enemy_location   == 'sea scene 2':
        game.enemy_level = random.randint(15, 17)
    elif enemy_location == 'sea scene 3':
        game.enemy_level = random.randint(17, 20)
    else:
        game.enemy_level = random.randint(11, 15)
    game.enemy_dmg = random.randint(5, 10)
    game.player_dmg = random.randint(50, 100)
def help(back):
    global game
    loc = game.location
    print("Basic commands include: north, south, east, west\n")
    answer = input("to continue to more advaced help type 1, to return to the game press 2")
    if answer == "1":
        print('')
    elif answer == "2":
        if back == "eastern_scene":
            eastern_scene()
        else:
            print(back)
            help(game.location)
    elif answer != 1 and answer !=2:
        print(game.location)
        help(game.location)

if __name__ == "__main__":
    gconfig = Config()
    game = Game(0, 1, gconfig.default_hero_health,0)
    game.prev_location = ""
    gstory = Story()
    questlist = ['1. slay 10 Bandits\n', '2. slay 10 undead soldiers\n']
    # #starting intro to game
    print(" Hello there! Welcome to the world of Grimm!")
    print("\nMy name is Arcus but you can call me The Narrator of this story, as well as the God of this world!")
    print("\nThis world is a vast place, called Grimm inhabited by many creatures\n")
    crossroads()
