from typing import List, Dict, Optional, Any


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Dict[str, Any]]
    weapon: Dict[str, Any]
    potion: Optional[Dict[str, Any]]
    hp: int
    power: int
    protection: int

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[Dict[str, Any]]] = None,
        weapon: Optional[Dict[str, Any]] = None,
        potion: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon or {"power": 0}
        self.potion = potion
        self.hp = hp
        self.power = power
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a.get("protection", 0) for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.get("effect", {}).items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.protection)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0

    def battle_results(self) -> Dict[str, int]:
        return {self.name: self.hp}

    def __repr__(self) -> str:
        return (f"<Knight {self.name}: HP={self.hp}, "
                f"Power={self.power}, Protection={self.protection}>")


def battle(knights: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    knights: List[Knight] = [Knight(**knights[name]) for name in
                             ["lancelot", "arthur", "mordred", "red_knight"]]

    # Prepare knights for battle
    for knight in knights:
        knight.prepare_for_battle()

    lancelot, arthur, mordred, red_knight = knights

    # Battle sequence
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # results
    results: Dict[str, int] = {}
    for knight in knights:
        results.update(knight.battle_results())

    return results
