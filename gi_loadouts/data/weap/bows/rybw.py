from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RoyalBow(Bow):
    name: str = "Royal Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Focus"
    refi_list: list[str] = [
        "Upon dealing damage to an opponent, increases CRIT Rate by 8%. Max 5 stacks. A CRIT hit removes all existing stacks.",
        "Upon dealing damage to an opponent, increases CRIT Rate by 10%. Max 5 stacks. A CRIT hit removes all existing stacks.",
        "Upon dealing damage to an opponent, increases CRIT Rate by 12%. Max 5 stacks. A CRIT hit removes all existing stacks.",
        "Upon dealing damage to an opponent, increases CRIT Rate by 14%. Max 5 stacks. A CRIT hit removes all existing stacks.",
        "Upon dealing damage to an opponent, increases CRIT Rate by 16%. Max 5 stacks. A CRIT hit removes all existing stacks.",
    ]
    file: str = "rybw"
