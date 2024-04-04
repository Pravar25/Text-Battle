from weapon import fists
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"\n{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")



class Hero(Character):
    def __init__(self,
                 name: str,
                 health = int
                 ) -> None:
        
        super().__init__(name = name, health = health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color = "green")

    def drop(self) -> None:
        if self.weapon == fists: return
        
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon

    def equip(self, weapon) -> None:
        if self.weapon.value == weapon.value: return

        if self.weapon.value == self.default_weapon.value:
            self.weapon = weapon
            print(f"\n{self.name} equipped a {self.weapon.name}!")
            return
        
        print("Dropping current weapon to equip new weapon next turn")
        self.drop()

        


class Enemy(Character):
    def __init__(self,
                 weapon,
                 name: str,
                 health = int,
                 ) -> None:
        
        super().__init__(name = name, health = health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color = "red")