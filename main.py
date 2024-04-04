from character import Hero, Enemy
from weapon import bow, sword

hero = Hero(name = "Hero", health = 100)

enemy = Enemy(name = "Enemy", health = 100, weapon = bow)


def action(choice: int):
    if choice == 0:
        hero.attack(enemy)
        return
    
    if choice == 1:
        while True:
            new_weapon = int(input("\nEnter weapon to equip: "))
            
            if new_weapon == 1:
                hero.equip(sword)
                return
            
            if new_weapon == 2:
                hero.equip(bow)
                return

            print("\nEnter valid weapon: ")

    if choice == 2:
        hero.drop()
        return


def main():

    action(1)
    
    while hero.health != 0 and enemy.health != 0:
        
        choice = int(input("\nEnter action: "))

        if choice == 0 or choice == 1 or choice == 2:
            action(choice)
            enemy.attack(hero)
        else:
            print("\nEnter a valid choice!\n")
        

        hero.health_bar.draw()
        enemy.health_bar.draw()
        print("\n")



if __name__ == "__main__":
    main()