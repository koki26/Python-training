import random
from colorama import Fore, Style

class Player:
    def __init__(self):
        self.player_class = 0
        self.health = 0
        self.damage = 0
        self.defence = 0
        self.current_weapon = None
        self.inventory = []
        self.alive = True

    def get_player_class(self):
        if self.player_class == 1:
            return("Mage")
        elif self.player_class == 2:
            return("Warrior")
        elif self.player_class == 3:
            return("Archer")
        
    def get_current_weapon(self):
        if self.current_weapon == 1:
            return("Mage staff")
        elif self.current_weapon == 2:
            return("Sword")
        elif self.current_weapon == 3:
            return("Bow")

    def get_current_weapon_damage(self):
        if self.current_weapon == 1:
            return(10)
        elif self.current_weapon == 2:
            return(15)
        elif self.current_weapon == 3:
            return(20)
    
    def alive_check(self):
        if self.health > 0:
            self.alive = True
        else:
            self.alive = False
class Enemy():
    enemy_type = 0
    enemy_health = 0
    enemy_damage = 0
    enemy_level = 0

    def get_type(self):
        if self.enemy_type == 1:
            return("Goblin")
        elif self.enemy_type == 2:
            return("Orc")
        elif self.enemy_type == 3:
            return("Dragon")
        elif self.enemy_type == 4:
            return("Skeleton")

    def get_enemy_health(self):
        if self.enemy_type == 1:
            return(10)
        elif self.enemy_type == 2:
            return(20)
        elif self.enemy_type == 3:
            return(50)
        elif self.enemy_type == 4:
            return(30)
        
    def get_enemy_damage(self):
        if self.enemy_type == 1:
            return(5)
        elif self.enemy_type == 2:
            return(10)
        elif self.enemy_type == 3:
            return(20)
        elif self.enemy_type == 4:
            return(15)
    

class Item:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name

    def get_item_name(self):
        return self.name

Staff = Item(1, "Mage staff")
Sword = Item(2, "Sword")
Bow = Item(3, "Bow")
Health_potion = Item(4, "Health potion")
Mana_potion = Item(5, "Mana potion")
Chainmail_armor = Item(6, "Chainmail armor")
Leather_armor = Item(7, "Leather armor")
Plate_armor = Item(8, "Plate armor")
Dragon_scale_armor = Item(9, "Dragon scale armor")
Gold_coin = Item(10, "Gold coin")




class Map():
    def next_step(current_player, current_stage, can_rest):
        
        rr = 0
        while rr != 1 and rr != 2:
            print("You have reached the next step")
            print("What do you do?")
            print("1. Continue")
            print("2. Rest")
            print("3. Check inventory")
            print("4. Check stats")
            rr = int(input())
            
            if rr == 1:
                print("You have continued")
            elif rr == 2:
                if can_rest == True:
                    print("You have rested")
                    current_player.health += 10
                else: 
                    print("You are not tired")
            elif rr == 3:
                print("\n=== Inventory ===")
                for i, item in enumerate(current_player.inventory, 1):
                    print(f"{i}. {item.get_item_name()}")
                print("=================\n")
            elif rr == 4:
                print("Your stats are:")
                print(f"Health: {current_player.health}")
                print(f"Attack: {current_player.damage}")
                print(f"Defense: {current_player.defense}")

        random_cc = random.randint(1, 3)
        print(f"Current stage: {current_stage}")
        if random_cc == 1:
            monster = Enemy()
            monster.enemy_type = random.randint(1, 4)
            monster.enemy_level = random.randint(1, 10) + current_stage
            monster.enemy_health = monster.get_enemy_health() + current_stage * 2
            monster.enemy_damage = monster.get_enemy_damage() + current_stage * 2
            print("You have encountered a monster!")
            while monster.enemy_health > 0 and current_player.alive == True:
                print(f"Monster type: {monster.enemy_type}")
                print(f"Monster level: {monster.enemy_level}")
                print(f"Monster health: {monster.enemy_health}")
                print(f"Your health: {current_player.health}")
                print("What do you do?")
                print("1. Attack")
                print("2. Run")
                print("3. Use Item")
                r = input()
                if r == "1":
                    print("You have attacked the monster!")
                    atc = random.randint(1, 100)
                    if atc < 50:
                        print("You have successfully attacked the monster!")
                        monster.enemy_health -= current_player.damage + current_player.get_current_weapon_damage()
                    else:
                        print("You have failed to attack the monster!")
                        current_player.health -= monster.enemy_damage + monster.enemy_level - current_player.defense
                        current_player.alive_check()

                elif r == "2":
                    ran = random.randint(1, 100)
                    if ran < 25:
                        print("You have run away from the monster!")
                        break
                    else:
                        print("You have failed to run away from the monster!")
                        current_player.health -= monster.enemy_damage + monster.enemy_level - current_player.defense
                        current_player.alive_check()
                elif r == "3":
                    print("What item do you want to use?")
                    print("1. Health Potion")
                    print("2. Mana Potion")


        elif random_cc == 2:
            print("You have encountered a treasure chest!")
            print("What do you do?")
            print("1. Open")
            print("2. Ignore")
            r = input()
            if r == "1":
                print("You have opened the treasure chest!")
                random_cc = random.randint(1, 3)
                if random_cc == 1:
                    print("You have found a health potion!")
                    current_player.inventory.append(4)
                elif random_cc == 2:
                    print("You have found a damage potion!")
                elif random_cc == 3:
                    print("You have found a gold coin!")
            elif r == "2":
                print("You have ignored the treasure chest!")
        elif random_cc == 3:
            print("You have encountered a friendly NPC!")
            print("What do you do?")
            print("1. Talk")
            print("2. Ignore")
            r = input()
            if r == "1":
                print("You have talked to the NPC!")
                rnd = random.randint(1, 3)
                if rnd == 1:
                    print("You have been given a health potion!")
                    current_player.inventory.append(4)
                elif rnd == 2:
                    print("You have been given a damage potion!")
                    current_player.inventory.append(5)
                elif rnd == 3:
                    print("You have been given a gold coin!")
                    current_player.inventory.append(6)
            elif r == "2":
                print("You have ignored the NPC!")

def main():
    player = Player()
    while player.player_class < 1 or player.player_class > 3:
        try:
            print("<< Welcome to Ctrl+Quest >>")
            print("<<   Select your class   >>")
            print("<<       [1] Mage        >>")
            print("<<       [2] Warrior     >>")
            print("<<       [3] Archer      >>")
            player.player_class = int(input())
            if player.player_class < 1 or player.player_class > 3:
                raise ValueError
        except:
            print("Not a valid number or not a class number!")
    print(f"You have selected {Player.get_player_class(player)}")
    if player.player_class == 1:
        player.health = 100
        player.damage = 10
        player.current_weapon = 1
        player.inventory.append(Staff)
    elif player.player_class == 2:
        player.health = 150
        player.damage = 20
        player.current_weapon = 2
        player.inventory.append(Sword)
    elif player.player_class == 3:
        player.health = 120
        player.damage = 15
        player.current_weapon = 3
        player.inventory.append(Bow)
    cur_step = 0
    tired = True
    while player.alive:
        Map.next_step(player, cur_step, tired)
        cur_step += 1
        player.alive_check()
        if tired == False:
            cu_st = cur_step
            cu_st_temp = cur_step
            if cu_st == cu_st_temp+5:
                tired = True
                player.can_rest = True
            else:
                cu_st += 1
    if player.alive == False:
        print(Fore.RED + Style.BRIGHT)
        print("====================================")
        print("              YOU DIED!             ")
        print("====================================")
        print(Style.RESET_ALL)


if __name__=="__main__":
    main()