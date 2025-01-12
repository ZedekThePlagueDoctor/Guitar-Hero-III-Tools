gh3_to_gha = {
    77: 0,
    78: 1,
    79: 56,
    80: 82,
    81: 39,
    82: [44, 45],
    83: [59, 60, 61, 62],
    84: 35,
    85: 36,
    86: 35,
    87: 47,
    88: 29,
    89: 22,
    90: 40,
    91: 44,
    92: [19, 20],
    93: 34,
    94: [51, 52],
    95: 38,
    96: 35,
    97: 15,
    98: 56,
    99: [31, 32],
    100: [17, 18],
    101: [42, 43],
    102: [69, 70],
    103: [26, 27],
    104: 28,
    105: [72, 73, 74, 75],
    106: 72,
    107: 73,
    108: 74,
    109: 75,
    110: 46,
    111: 60,
    112: 59,
    113: 61,
    114: [64, 65],
    115: 85,
    116: 84,
    117: 57,
}

gha_to_gh3 = {
    # Enable Changes
    0: 77,
    1: 78,
    # Rhythm Cameras
    3: 79,
    4: 79,
    5: 79,
    6: 79,
    7: 84,
    8: 86,
    # Bassist Cameras
    10: 97,
    11: 97,
    12: 97,
    13: 97,
    14: 84,
    15: 86,
    # Drummer Cameras
    17: 100,
    18: 100,
    19: 92,
    20: 92,
    21: 89,
    22: 89,
    # Singer Cameras
    24: 101,
    25: 101,
    26: 103,
    27: 103,
    28: 104,
    29: 88,
    # Guitarist Cameras
    31: 99,
    32: 99,
    33: 93,
    34: 94,
    35: 95,
    36: 85,
    # Guitarist Special
    38: 95,
    39: 81,
    40: 81,
    # Stage Cameras
    42: 101,
    43: 102,
    44: 91,
    45: 82,
    46: 87,
    47: 110,
    # Mid Cameras
    49: 85,
    50: 85,
    51: 94,
    52: 94,
    53: 85,
    54: 85,
    # Longshot Cameras
    56: 91,
    57: 117,
    # Zoom Cameras
    59: 112,
    60: 111,
    61: 113,
    62: 113,
    # Pan Cameras
    64: 114,
    65: 114,
    # Dolly Cameras
    67: 101,
    68: 101,
    69: 102,
    70: 102,
    # Special Cameras
    72: 106,
    73: 107,
    74: 108,
    75: 109,
    # Mocap Cameras
    77: 106,
    78: 107,
    79: 108,
    80: 109,
    # Audience Cameras
    82: 80,
    # Boss Battle Cameras
    84: 116,
    85: 115,
    # Singer Closeups
    87: 104,
    88: 104,
    89: 104,
    # Stagediver
    91: 117,
}

anim_struct = {
    "guitar": {},
    "bass": {},
    "drum": {},
    "vocals": {}
}

allowed_anims_gh3 = [
    "band_playsimpleanim",
    "band_playanim",
    "band_playidle",
    "band_playfacialanim",
    "band_setstrumstyle",
    "band_changestance",
    "band_stopstrumming",
    "band_enablearms",
    "band_disablearms",
    "band_setposition",
    "band_disablemovement",
    "band_enablemovement",
    "band_walktonode",
    "band_turntoface",
    "band_rotatetofacenode",
    "band_facenode",
    "band_faceaudience",
    "band_playattackanim",
    "band_playresponseanim",
    "bassist_should_use_guitarist_commands",
    "crowd_startlighters",
    "crowd_stoplighters",
    "crowd_stagediver_hide",
    "crowd_stagediver_jump"
]

allowed_anims_gha = [
    "band_forcetostance",
    "band_movetonode",
    "band_movetostartnode"
]

gha_play_anims = ["BackPlay", "Somersault"]
gha_anim_swaps = {
    "kneesolo": "solo",
    "somersault": "special",
    "backplay": "jump",
    "joeperryspin": "special",
}