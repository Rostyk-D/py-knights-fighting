from typing import Dict
from models import Knight


def battle(knights: Dict[str, Dict]) -> Dict[str, int]:
    knights = [Knight(**knights[name]) for name in
               ["lancelot", "arthur", "mordred", "red_knight"]]

    for knight in knights:
        knight.prepare_for_battle()

    lancelot, arthur, mordred, red_knight = knights

    # 1. Lancelot vs Mordred
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # 2. Arthur vs Red Knight
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    results: Dict[str, int] = {}
    for knight in knights:
        results.update(knight.battle_results())

    return results
