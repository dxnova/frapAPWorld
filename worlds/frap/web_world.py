from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class FrostRunnerWebWorld(WebWorld):
    game = "FrostRunner"
    theme = "ice"
