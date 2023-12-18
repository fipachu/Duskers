TITLE = """\
+===========================================================================================+
  ######*   ##*  ##*  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*  ##*  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ######*    #####*   ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*         ##*     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ##*         ##*     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                                (Survival ASCII Strategy Game)
+===========================================================================================+\
"""
HUB = """\
__________(LOG)__________________________________________________(LOG)__________
+==============================================================================+
{}
+==============================================================================+
| Titanium: {:<67}|
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+\
"""
DRONE = """\
 $()$()$ 
$$.....$$
 $$$$$$$ 
$$$...$$$
$~$$$$$~$\
"""
# This should really be a tuple of structs, buy it's already a dictionary and I just
# wanna get it done
UPGRADES = {
    "1": {
        "name": "Titanium Scan",
        "price": 250,
        "description": "You can now see how much titanium you can get from each found location.",
    },
    "2": {
        "name": "Enemy Encounter Scan",
        "price": 500,
        "description": "You will now see how likely you will encounter an enemy at each found location.",
    },
}
ITEMS = {
    "3": {
        "name": "New Robot",
        "price": 1000,
        "description": "You now have an additional robot.",
    }
}

UPGRADE_MENU = f"""\
                       |================================|
                       |          UPGRADE STORE         |
                       |                         Price  |
                       | [1] {UPGRADES["1"]["name"]:<20} {UPGRADES["1"]["price"]:>4}  |
                       | [2] {UPGRADES["2"]["name"]:<20} {UPGRADES["2"]["price"]:>4}  |
                       | [3] {ITEMS["3"]["name"]:<20} {ITEMS["3"]["price"]:>4}  |
                       |                                |
                       | [Back]                         |
                       |================================|\
"""
MENU = """\
                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|\
"""
SAVED = """\
                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|\
"""
LOADED = """\
                        |==============================|
                        |    GAME LOADED SUCCESSFULLY  |
                        |==============================|\
"""
GAME_OVER = """\
                        |==============================|
                        |          GAME OVER!          |
                        |==============================|\
"""

COMMAND = "Your command: "
NAME = "Enter your name: "
GREETING = "Greetings, commander {}!"
INVALID_INPUT = "Invalid input"
COMING_SOON = "Coming SOON!"

LOCATIONS = (
    "Nomad's_Remembrance,"
    "Silent_Voyager,"
    "Forgotten_Odyssey,"
    "Celestial_Serenity,"
    "Astral_Tranquility,"
    "Stargazer's_Lament,"
    "Quiet_Eclipse_Retreat,"
    "Lunar_Echo_Haven,"
    "Solitary_Starlight_Sanctum,"
    "Nebula's_Embrace,"
    "Orbital_Twilight_Refuge,"
    "Seraphic_Solitude_Station,"
    "Cosmic_Whispers_Outpost,"
    "Starshard_Refuge,"
    "Ethereal_Zenith_Retreat,"
    "Spice_Harvest_Echo,"
    "Leviathan's_Last_Watch,"
    "Oceania_Echo_Outpost,"
    "Ceres_Mirage_Wrecks,"
    "Room_101,"
    "Echo_Chamber,"
    "Tycho_Tranquility_Station,"
)
