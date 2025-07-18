import pytest

from gi_loadouts.data.weap.catalysts import CatalystsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Catalyst, Tier, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, tier, levl, batk, seco, valu",
    [
        pytest.param("Magic Guide", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.elemental_mastery, 171, id="data.weap.catalysts: Magic Guide"),
        pytest.param("Dodoco Tales", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.catalysts: Dodoco Tales"),
        pytest.param("Eye of Perception", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.catalysts: Eye of Perception"),
        pytest.param("Sacrificial Fragments", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.elemental_mastery, 201, id="data.weap.catalysts: Sacrificial Fragments"),
        pytest.param("Sacrificial Jade", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.critical_rate_perc, 33.5, id="data.weap.catalysts: Sacrificial Jade"),
        pytest.param("Waveriding Whirl", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.catalysts: Waveriding Whirl"),
        pytest.param("A Thousand Floating Dreams", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.elemental_mastery, 241, id="data.weap.catalysts: A Thousand Floating Dreams"),
        pytest.param("Starcaller's Watch", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.elemental_mastery, 241, id="data.weap.catalysts: Starcaller's Watch"),
        pytest.param("Sunny Morning Sleep-In", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.elemental_mastery, 241, id="data.weap.catalysts: Sunny Morning Sleep-In"),
        pytest.param("Surf's Up", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.catalysts: Surf's Up"),
        pytest.param("Tome of the Eternal Flow", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.catalysts: Tome of the Eternal Flow"),
        pytest.param("Apprentice's Notes", 1, 2, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, id="data.weap.catalysts: Apprentice's Notes"),
        pytest.param("Pocket Grimoire", 2, 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, id="data.weap.catalysts: Pocket Grimoire"),
        pytest.param("Otherworldly Story", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.energy_recharge_perc, 35.6, id="data.weap.catalysts: Otherworldly Story"),
        pytest.param("Thrilling Tales of Dragon Slayers", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.health_points_perc, 32.1, id="data.weap.catalysts: Thrilling Tales of Dragon Slayers"),
        pytest.param("Ash-Graven Drinking Horn", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.catalysts: Ash-Graven Drinking Horn"),
        pytest.param("Blackcliff Agate", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, id="data.weap.catalysts: Blackcliff Agate"),
        pytest.param("Favonius Codex", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.catalysts: Favonius Codex"),
        pytest.param("Frostbearer", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.catalysts: Frostbearer"),
        pytest.param("Fruit of Fulfillment", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.catalysts: Fruit of Fulfillment"),
        pytest.param("Prototype Amber", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.catalysts: Prototype Amber"),
        pytest.param("Ring of Yaxche", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.catalysts: Ring of Yaxche"),
        pytest.param("Solar Pearl", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.catalysts: Solar Pearl"),
        pytest.param("The Widsith", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, id="data.weap.catalysts: The Widsith"),
        pytest.param("Wandering Evenstar", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.catalysts: Wandering Evenstar"),
        pytest.param("Everlasting Moonglow", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.health_points_perc, 45.3, id="data.weap.catalysts: Everlasting Moonglow"),
        pytest.param("Jadefall's Splendor", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.health_points_perc, 45.3, id="data.weap.catalysts: Jadefall's Splendor"),
        pytest.param("Kagura's Verity", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, id="data.weap.catalysts: Kagura's Verity"),
        pytest.param("Lost Prayer to the Sacred Winds", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, id="data.weap.catalysts: Lost Prayer to the Sacred Winds"),
        pytest.param("Memory of Dust", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.catalysts: Memory of Dust"),
        pytest.param("Emerald Orb", 3, 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.elemental_mastery, 85, id="data.weap.catalysts: Emerald Orb"),
        pytest.param("Twin Nephrite", 3, 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.critical_rate_perc, 14.2, id="data.weap.catalysts: Twin Nephrite"),
        pytest.param("Ballad of the Boundless Blue", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.catalysts: Ballad of the Boundless Blue"),
        pytest.param("Flowing Purity", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.catalysts: Flowing Purity"),
        pytest.param("Hakushin Ring", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.catalysts: Hakushin Ring"),
        pytest.param("Mappa Mare", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, id="data.weap.catalysts: Mappa Mare"),
        pytest.param("Oathsworn Eye", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.catalysts: Oathsworn Eye"),
        pytest.param("Royal Grimoire", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.catalysts: Royal Grimoire"),
        pytest.param("Wine and Song", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.catalysts: Wine and Song"),
        pytest.param("Cashflow Supervision", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.catalysts: Cashflow Supervision"),
        pytest.param("Skyward Atlas", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.attack_perc, 30.2, id="data.weap.catalysts: Skyward Atlas"),
        pytest.param("Tulaytullah's Remembrance", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, id="data.weap.catalysts: Tulaytullah's Remembrance"),
        pytest.param("Vivid Notions", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, id="data.weap.catalysts: Vivid Notions"),
        pytest.param("Crane's Echoing Call", 5, 4, "Level 80/90 (Rank 6)", 679, WeaponStatType.attack_perc, 15.1, id="data.weap.catalysts: Crane's Echoing Call"),
    ]
)
def test_catalyst(name: str, rare: int, tier: int, levl: str, batk: int, seco: WeaponStatType, valu: float) -> None:
    """
    Test all weapons of catalyst type for correctness

    :return:
    """
    unit = CatalystsDict[name]()
    assert unit.type == Catalyst().type
    assert len(unit.refinement) == len(unit.refi_list)
    assert len(unit.levl_bind) == 74 if rare in {1, 2} else 96
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    assert unit.rare == getattr(Rare, f"Star_{rare}")
    assert unit.tier == getattr(Tier, f"Tier_{tier}")
    assert round(unit.main_stat.stat_data) == batk
    assert unit.seco_stat.stat_name == seco
    if unit.seco_stat.stat_name != WeaponStatType.none:
        assert verify_accuracy(unit.seco_stat_calc.stat_data, valu, 1.5)
