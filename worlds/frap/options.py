from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Insanity(Toggle):
    display_name = "Enable insanity levels? (not implemented yet)"
@dataclass
class FrostRunnerOptions(PerGameCommonOptions):
    insanity: Insanity