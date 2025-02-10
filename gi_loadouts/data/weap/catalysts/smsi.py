from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Catalyst, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class SunnyMorningSleepIn(Catalyst):
    name: str = "Sunny Morning Sleep-In"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=58.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Bathhouses, Hawks, and Narukami"
    refi_list: List[str] = [
        "Elemental Mastery increases by 120 for 6s after triggering Swirl. Elemental Mastery increases by 96 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 32 for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by (var1) for 6s after triggering Swirl. Elemental Mastery increases by (var2) for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by (var3) for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by (var1) for 6s after triggering Swirl. Elemental Mastery increases by (var2) for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by (var3) for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by (var1) for 6s after triggering Swirl. Elemental Mastery increases by (var2) for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by (var3) for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by (var1) for 6s after triggering Swirl. Elemental Mastery increases by (var2) for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by (var3) for 30s after the wielder's Elemental Burst hits an opponent.."
    ]
    file: str = "smsi"
