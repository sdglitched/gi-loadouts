from ..rank import Rank
from ..rare import Rare

Secs = {
    Rank.Rank_0: 0,
    Rank.Rank_1: 38 / 182,
    Rank.Rank_2: 65 / 182,
    Rank.Rank_3: 101 / 182,
    Rank.Rank_4: 128 / 182,
    Rank.Rank_5: 155 / 182,
    Rank.Rank_6: 1,
}


Mult = {
    1: {
        Rare.Star_4: {"hp_def": 1.000, "atk": 1.000},
        Rare.Star_5: {"hp_def": 1.000, "atk": 1.000},
    },
    2: {
        Rare.Star_4: {"hp_def": 1.083, "atk": 1.083},
        Rare.Star_5: {"hp_def": 1.083, "atk": 1.083},
    },
    3: {
        Rare.Star_4: {"hp_def": 1.165, "atk": 1.165},
        Rare.Star_5: {"hp_def": 1.166, "atk": 1.166},
    },
    4: {
        Rare.Star_4: {"hp_def": 1.248, "atk": 1.248},
        Rare.Star_5: {"hp_def": 1.250, "atk": 1.250},
    },
    5: {
        Rare.Star_4: {"hp_def": 1.330, "atk": 1.330},
        Rare.Star_5: {"hp_def": 1.333, "atk": 1.333},
    },
    6: {
        Rare.Star_4: {"hp_def": 1.413, "atk": 1.413},
        Rare.Star_5: {"hp_def": 1.417, "atk": 1.417},
    },
    7: {
        Rare.Star_4: {"hp_def": 1.495, "atk": 1.495},
        Rare.Star_5: {"hp_def": 1.500, "atk": 1.500},
    },
    8: {
        Rare.Star_4: {"hp_def": 1.578, "atk": 1.578},
        Rare.Star_5: {"hp_def": 1.584, "atk": 1.584},
    },
    9: {
        Rare.Star_4: {"hp_def": 1.661, "atk": 1.661},
        Rare.Star_5: {"hp_def": 1.668, "atk": 1.668},
    },
    10: {
        Rare.Star_4: {"hp_def": 1.743, "atk": 1.743},
        Rare.Star_5: {"hp_def": 1.751, "atk": 1.751},
    },
    11: {
        Rare.Star_4: {"hp_def": 1.826, "atk": 1.826},
        Rare.Star_5: {"hp_def": 1.835, "atk": 1.835},
    },
    12: {
        Rare.Star_4: {"hp_def": 1.908, "atk": 1.908},
        Rare.Star_5: {"hp_def": 1.919, "atk": 1.919},
    },
    13: {
        Rare.Star_4: {"hp_def": 1.991, "atk": 1.991},
        Rare.Star_5: {"hp_def": 2.003, "atk": 2.003},
    },
    14: {
        Rare.Star_4: {"hp_def": 2.073, "atk": 2.073},
        Rare.Star_5: {"hp_def": 2.088, "atk": 2.088},
    },
    15: {
        Rare.Star_4: {"hp_def": 2.156, "atk": 2.156},
        Rare.Star_5: {"hp_def": 2.172, "atk": 2.172},
    },
    16: {
        Rare.Star_4: {"hp_def": 2.239, "atk": 2.239},
        Rare.Star_5: {"hp_def": 2.256, "atk": 2.256},
    },
    17: {
        Rare.Star_4: {"hp_def": 2.321, "atk": 2.321},
        Rare.Star_5: {"hp_def": 2.341, "atk": 2.341},
    },
    18: {
        Rare.Star_4: {"hp_def": 2.404, "atk": 2.404},
        Rare.Star_5: {"hp_def": 2.425, "atk": 2.425},
    },
    19: {
        Rare.Star_4: {"hp_def": 2.486, "atk": 2.486},
        Rare.Star_5: {"hp_def": 2.510, "atk": 2.510},
    },
    20: {
        Rare.Star_4: {"hp_def": 2.569, "atk": 2.569},
        Rare.Star_5: {"hp_def": 2.594, "atk": 2.594},
    },
    21: {
        Rare.Star_4: {"hp_def": 2.651, "atk": 2.651},
        Rare.Star_5: {"hp_def": 2.679, "atk": 2.679},
    },
    22: {
        Rare.Star_4: {"hp_def": 2.734, "atk": 2.734},
        Rare.Star_5: {"hp_def": 2.764, "atk": 2.764},
    },
    23: {
        Rare.Star_4: {"hp_def": 2.817, "atk": 2.817},
        Rare.Star_5: {"hp_def": 2.849, "atk": 2.849},
    },
    24: {
        Rare.Star_4: {"hp_def": 2.899, "atk": 2.899},
        Rare.Star_5: {"hp_def": 2.934, "atk": 2.934},
    },
    25: {
        Rare.Star_4: {"hp_def": 2.982, "atk": 2.982},
        Rare.Star_5: {"hp_def": 3.019, "atk": 3.019},
    },
    26: {
        Rare.Star_4: {"hp_def": 3.064, "atk": 3.064},
        Rare.Star_5: {"hp_def": 3.105, "atk": 3.105},
    },
    27: {
        Rare.Star_4: {"hp_def": 3.147, "atk": 3.147},
        Rare.Star_5: {"hp_def": 3.190, "atk": 3.190},
    },
    28: {
        Rare.Star_4: {"hp_def": 3.229, "atk": 3.229},
        Rare.Star_5: {"hp_def": 3.275, "atk": 3.275},
    },
    29: {
        Rare.Star_4: {"hp_def": 3.312, "atk": 3.312},
        Rare.Star_5: {"hp_def": 3.361, "atk": 3.361},
    },
    30: {
        Rare.Star_4: {"hp_def": 3.394, "atk": 3.394},
        Rare.Star_5: {"hp_def": 3.446, "atk": 3.446},
    },
    31: {
        Rare.Star_4: {"hp_def": 3.477, "atk": 3.477},
        Rare.Star_5: {"hp_def": 3.532, "atk": 3.532},
    },
    32: {
        Rare.Star_4: {"hp_def": 3.560, "atk": 3.560},
        Rare.Star_5: {"hp_def": 3.618, "atk": 3.618},
    },
    33: {
        Rare.Star_4: {"hp_def": 3.642, "atk": 3.642},
        Rare.Star_5: {"hp_def": 3.704, "atk": 3.704},
    },
    34: {
        Rare.Star_4: {"hp_def": 3.725, "atk": 3.725},
        Rare.Star_5: {"hp_def": 3.789, "atk": 3.789},
    },
    35: {
        Rare.Star_4: {"hp_def": 3.807, "atk": 3.807},
        Rare.Star_5: {"hp_def": 3.875, "atk": 3.875},
    },
    36: {
        Rare.Star_4: {"hp_def": 3.890, "atk": 3.890},
        Rare.Star_5: {"hp_def": 3.962, "atk": 3.962},
    },
    37: {
        Rare.Star_4: {"hp_def": 3.972, "atk": 3.972},
        Rare.Star_5: {"hp_def": 4.048, "atk": 4.048},
    },
    38: {
        Rare.Star_4: {"hp_def": 4.055, "atk": 4.055},
        Rare.Star_5: {"hp_def": 4.134, "atk": 4.134},
    },
    39: {
        Rare.Star_4: {"hp_def": 4.138, "atk": 4.138},
        Rare.Star_5: {"hp_def": 4.220, "atk": 4.220},
    },
    40: {
        Rare.Star_4: {"hp_def": 4.220, "atk": 4.220},
        Rare.Star_5: {"hp_def": 4.307, "atk": 4.307},
    },
    41: {
        Rare.Star_4: {"hp_def": 4.303, "atk": 4.303},
        Rare.Star_5: {"hp_def": 4.393, "atk": 4.393},
    },
    42: {
        Rare.Star_4: {"hp_def": 4.385, "atk": 4.385},
        Rare.Star_5: {"hp_def": 4.480, "atk": 4.480},
    },
    43: {
        Rare.Star_4: {"hp_def": 4.468, "atk": 4.468},
        Rare.Star_5: {"hp_def": 4.567, "atk": 4.567},
    },
    44: {
        Rare.Star_4: {"hp_def": 4.550, "atk": 4.550},
        Rare.Star_5: {"hp_def": 4.653, "atk": 4.653},
    },
    45: {
        Rare.Star_4: {"hp_def": 4.633, "atk": 4.633},
        Rare.Star_5: {"hp_def": 4.740, "atk": 4.740},
    },
    46: {
        Rare.Star_4: {"hp_def": 4.716, "atk": 4.716},
        Rare.Star_5: {"hp_def": 4.827, "atk": 4.827},
    },
    47: {
        Rare.Star_4: {"hp_def": 4.798, "atk": 4.798},
        Rare.Star_5: {"hp_def": 4.914, "atk": 4.914},
    },
    48: {
        Rare.Star_4: {"hp_def": 4.881, "atk": 4.881},
        Rare.Star_5: {"hp_def": 5.001, "atk": 5.001},
    },
    49: {
        Rare.Star_4: {"hp_def": 4.963, "atk": 4.963},
        Rare.Star_5: {"hp_def": 5.089, "atk": 5.089},
    },
    50: {
        Rare.Star_4: {"hp_def": 5.046, "atk": 5.046},
        Rare.Star_5: {"hp_def": 5.176, "atk": 5.176},
    },
    51: {
        Rare.Star_4: {"hp_def": 5.128, "atk": 5.128},
        Rare.Star_5: {"hp_def": 5.263, "atk": 5.263},
    },
    52: {
        Rare.Star_4: {"hp_def": 5.211, "atk": 5.211},
        Rare.Star_5: {"hp_def": 5.351, "atk": 5.351},
    },
    53: {
        Rare.Star_4: {"hp_def": 5.294, "atk": 5.294},
        Rare.Star_5: {"hp_def": 5.438, "atk": 5.438},
    },
    54: {
        Rare.Star_4: {"hp_def": 5.376, "atk": 5.376},
        Rare.Star_5: {"hp_def": 5.526, "atk": 5.526},
    },
    55: {
        Rare.Star_4: {"hp_def": 5.459, "atk": 5.459},
        Rare.Star_5: {"hp_def": 5.614, "atk": 5.614},
    },
    56: {
        Rare.Star_4: {"hp_def": 5.541, "atk": 5.541},
        Rare.Star_5: {"hp_def": 5.702, "atk": 5.702},
    },
    57: {
        Rare.Star_4: {"hp_def": 5.624, "atk": 5.624},
        Rare.Star_5: {"hp_def": 5.790, "atk": 5.790},
    },
    58: {
        Rare.Star_4: {"hp_def": 5.706, "atk": 5.706},
        Rare.Star_5: {"hp_def": 5.878, "atk": 5.878},
    },
    59: {
        Rare.Star_4: {"hp_def": 5.789, "atk": 5.789},
        Rare.Star_5: {"hp_def": 5.966, "atk": 5.966},
    },
    60: {
        Rare.Star_4: {"hp_def": 5.872, "atk": 5.872},
        Rare.Star_5: {"hp_def": 6.054, "atk": 6.054},
    },
    61: {
        Rare.Star_4: {"hp_def": 5.954, "atk": 5.954},
        Rare.Star_5: {"hp_def": 6.142, "atk": 6.142},
    },
    62: {
        Rare.Star_4: {"hp_def": 6.037, "atk": 6.037},
        Rare.Star_5: {"hp_def": 6.230, "atk": 6.230},
    },
    63: {
        Rare.Star_4: {"hp_def": 6.119, "atk": 6.119},
        Rare.Star_5: {"hp_def": 6.319, "atk": 6.319},
    },
    64: {
        Rare.Star_4: {"hp_def": 6.202, "atk": 6.202},
        Rare.Star_5: {"hp_def": 6.407, "atk": 6.407},
    },
    65: {
        Rare.Star_4: {"hp_def": 6.284, "atk": 6.284},
        Rare.Star_5: {"hp_def": 6.496, "atk": 6.496},
    },
    66: {
        Rare.Star_4: {"hp_def": 6.367, "atk": 6.367},
        Rare.Star_5: {"hp_def": 6.585, "atk": 6.585},
    },
    67: {
        Rare.Star_4: {"hp_def": 6.450, "atk": 6.450},
        Rare.Star_5: {"hp_def": 6.673, "atk": 6.673},
    },
    68: {
        Rare.Star_4: {"hp_def": 6.532, "atk": 6.532},
        Rare.Star_5: {"hp_def": 6.762, "atk": 6.762},
    },
    69: {
        Rare.Star_4: {"hp_def": 6.615, "atk": 6.615},
        Rare.Star_5: {"hp_def": 6.851, "atk": 6.851},
    },
    70: {
        Rare.Star_4: {"hp_def": 6.697, "atk": 6.697},
        Rare.Star_5: {"hp_def": 6.940, "atk": 6.940},
    },
    71: {
        Rare.Star_4: {"hp_def": 6.780, "atk": 6.780},
        Rare.Star_5: {"hp_def": 7.029, "atk": 7.029},
    },
    72: {
        Rare.Star_4: {"hp_def": 6.862, "atk": 6.862},
        Rare.Star_5: {"hp_def": 7.119, "atk": 7.119},
    },
    73: {
        Rare.Star_4: {"hp_def": 6.945, "atk": 6.945},
        Rare.Star_5: {"hp_def": 7.208, "atk": 7.208},
    },
    74: {
        Rare.Star_4: {"hp_def": 7.028, "atk": 7.028},
        Rare.Star_5: {"hp_def": 7.297, "atk": 7.297},
    },
    75: {
        Rare.Star_4: {"hp_def": 7.110, "atk": 7.110},
        Rare.Star_5: {"hp_def": 7.387, "atk": 7.387},
    },
    76: {
        Rare.Star_4: {"hp_def": 7.193, "atk": 7.193},
        Rare.Star_5: {"hp_def": 7.476, "atk": 7.476},
    },
    77: {
        Rare.Star_4: {"hp_def": 7.275, "atk": 7.275},
        Rare.Star_5: {"hp_def": 7.566, "atk": 7.566},
    },
    78: {
        Rare.Star_4: {"hp_def": 7.358, "atk": 7.358},
        Rare.Star_5: {"hp_def": 7.656, "atk": 7.656},
    },
    79: {
        Rare.Star_4: {"hp_def": 7.440, "atk": 7.440},
        Rare.Star_5: {"hp_def": 7.746, "atk": 7.746},
    },
    80: {
        Rare.Star_4: {"hp_def": 7.523, "atk": 7.523},
        Rare.Star_5: {"hp_def": 7.836, "atk": 7.836},
    },
    81: {
        Rare.Star_4: {"hp_def": 7.606, "atk": 7.606},
        Rare.Star_5: {"hp_def": 7.926, "atk": 7.926},
    },
    82: {
        Rare.Star_4: {"hp_def": 7.688, "atk": 7.688},
        Rare.Star_5: {"hp_def": 8.016, "atk": 8.016},
    },
    83: {
        Rare.Star_4: {"hp_def": 7.771, "atk": 7.771},
        Rare.Star_5: {"hp_def": 8.106, "atk": 8.106},
    },
    84: {
        Rare.Star_4: {"hp_def": 7.853, "atk": 7.853},
        Rare.Star_5: {"hp_def": 8.196, "atk": 8.196},
    },
    85: {
        Rare.Star_4: {"hp_def": 7.936, "atk": 7.936},
        Rare.Star_5: {"hp_def": 8.286, "atk": 8.286},
    },
    86: {
        Rare.Star_4: {"hp_def": 8.018, "atk": 8.018},
        Rare.Star_5: {"hp_def": 8.377, "atk": 8.377},
    },
    87: {
        Rare.Star_4: {"hp_def": 8.101, "atk": 8.101},
        Rare.Star_5: {"hp_def": 8.467, "atk": 8.467},
    },
    88: {
        Rare.Star_4: {"hp_def": 8.183, "atk": 8.183},
        Rare.Star_5: {"hp_def": 8.558, "atk": 8.558},
    },
    89: {
        Rare.Star_4: {"hp_def": 8.266, "atk": 8.266},
        Rare.Star_5: {"hp_def": 8.649, "atk": 8.649},
    },
    90: {
        Rare.Star_4: {"hp_def": 8.349, "atk": 8.349},
        Rare.Star_5: {"hp_def": 8.739, "atk": 8.739},
    },
    95: {
        Rare.Star_4: {"hp_def": 8.761, "atk": 9.87},
        Rare.Star_5: {"hp_def": 9.195, "atk": 10.184},
    },
    100: {
        Rare.Star_4: {"hp_def": 9.174, "atk": 11.392},
        Rare.Star_5: {"hp_def": 9.652, "atk": 11.629},
    },
}
