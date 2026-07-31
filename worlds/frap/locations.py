from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

import json
import os

if TYPE_CHECKING:
    from .world import FrostRunnerWorld



class FrostRunnerLocation(Location):
        game = "FrostRunner"

locations_data = [
    {"LocationID": 1, "Chapter": "Prologue", "ChapterID": 1, "Level": "Pemphredo", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 2, "Chapter": "Prologue", "ChapterID": 1, "Level": "Pemphredo", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 3, "Chapter": "Prologue", "ChapterID": 1, "Level": "Lamia", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 4, "Chapter": "Prologue", "ChapterID": 1, "Level": "Lamia", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 5, "Chapter": "Prologue", "ChapterID": 1, "Level": "Lycaon", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 6, "Chapter": "Prologue", "ChapterID": 1, "Level": "Lycaon", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 7, "Chapter": "Prologue", "ChapterID": 1, "Level": "Atlas", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 8, "Chapter": "Prologue", "ChapterID": 1, "Level": "Atlas", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 9, "Chapter": "Prologue", "ChapterID": 1, "Level": "Chimera", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 10, "Chapter": "Prologue", "ChapterID": 1, "Level": "Chimera", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 11, "Chapter": "Ring", "ChapterID": 2, "Level": "Mormo", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 12, "Chapter": "Ring", "ChapterID": 2, "Level": "Mormo", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 13, "Chapter": "Ring", "ChapterID": 2, "Level": "Centaur", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 14, "Chapter": "Ring", "ChapterID": 2, "Level": "Centaur", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 15, "Chapter": "Ring", "ChapterID": 2, "Level": "Ampelos", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 16, "Chapter": "Ring", "ChapterID": 2, "Level": "Ampelos", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 17, "Chapter": "Ring", "ChapterID": 2, "Level": "Aphrodite", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 18, "Chapter": "Ring", "ChapterID": 2, "Level": "Aphrodite", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 19, "Chapter": "Ring", "ChapterID": 2, "Level": "Siren", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 20, "Chapter": "Ring", "ChapterID": 2, "Level": "Siren", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 21, "Chapter": "Ice", "ChapterID": 3, "Level": "Deino", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 22, "Chapter": "Ice", "ChapterID": 3, "Level": "Deino", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 23, "Chapter": "Ice", "ChapterID": 3, "Level": "Rhea", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 24, "Chapter": "Ice", "ChapterID": 3, "Level": "Rhea", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 25, "Chapter": "Ice", "ChapterID": 3, "Level": "Pegasus", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 26, "Chapter": "Ice", "ChapterID": 3, "Level": "Pegasus", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 27, "Chapter": "Ice", "ChapterID": 3, "Level": "Hydra", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 28, "Chapter": "Ice", "ChapterID": 3, "Level": "Hydra", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 29, "Chapter": "Ice", "ChapterID": 3, "Level": "Gorgon", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 30, "Chapter": "Ice", "ChapterID": 3, "Level": "Gorgon", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 31, "Chapter": "Tether", "ChapterID": 4, "Level": "Empousa", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 32, "Chapter": "Tether", "ChapterID": 4, "Level": "Empousa", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 33, "Chapter": "Tether", "ChapterID": 4, "Level": "Dryad", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 34, "Chapter": "Tether", "ChapterID": 4, "Level": "Dryad", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 35, "Chapter": "Tether", "ChapterID": 4, "Level": "Echion", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 36, "Chapter": "Tether", "ChapterID": 4, "Level": "Echion", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 37, "Chapter": "Tether", "ChapterID": 4, "Level": "Cyclops", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 38, "Chapter": "Tether", "ChapterID": 4, "Level": "Cyclops", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 39, "Chapter": "Tether", "ChapterID": 4, "Level": "Marsyas", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 40, "Chapter": "Tether", "ChapterID": 4, "Level": "Marsyas", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 41, "Chapter": "Fling", "ChapterID": 5, "Level": "Enyo", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 42, "Chapter": "Fling", "ChapterID": 5, "Level": "Enyo", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 43, "Chapter": "Fling", "ChapterID": 5, "Level": "Eos", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 44, "Chapter": "Fling", "ChapterID": 5, "Level": "Eos", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 45, "Chapter": "Fling", "ChapterID": 5, "Level": "Aegeus", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 46, "Chapter": "Fling", "ChapterID": 5, "Level": "Aegeus", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 47, "Chapter": "Fling", "ChapterID": 5, "Level": "Cadoc", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 48, "Chapter": "Fling", "ChapterID": 5, "Level": "Cadoc", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 49, "Chapter": "Fling", "ChapterID": 5, "Level": "Nomios", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 50, "Chapter": "Fling", "ChapterID": 5, "Level": "Nomios", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 51, "Chapter": "Chain", "ChapterID": 6, "Level": "Thoon", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 52, "Chapter": "Chain", "ChapterID": 6, "Level": "Thoon", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 53, "Chapter": "Chain", "ChapterID": 6, "Level": "Phoebe", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 54, "Chapter": "Chain", "ChapterID": 6, "Level": "Phoebe", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 55, "Chapter": "Chain", "ChapterID": 6, "Level": "Harpy", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 56, "Chapter": "Chain", "ChapterID": 6, "Level": "Harpy", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 57, "Chapter": "Chain", "ChapterID": 6, "Level": "Heracles", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 58, "Chapter": "Chain", "ChapterID": 6, "Level": "Heracles", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 59, "Chapter": "Chain", "ChapterID": 6, "Level": "Demeter", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 60, "Chapter": "Chain", "ChapterID": 6, "Level": "Demeter", "LevelID": 5, "Category": "Clear"},

    {"LocationID": 61, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Achilles", "LevelID": 1, "Category": "Collectable"},
    {"LocationID": 62, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Achilles", "LevelID": 1, "Category": "Clear"},
    {"LocationID": 63, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Manticore", "LevelID": 2, "Category": "Collectable"},
    {"LocationID": 64, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Manticore", "LevelID": 2, "Category": "Clear"},
    {"LocationID": 65, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Basilisk", "LevelID": 3, "Category": "Collectable"},
    {"LocationID": 66, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Basilisk", "LevelID": 3, "Category": "Clear"},
    {"LocationID": 67, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Aesop", "LevelID": 4, "Category": "Collectable"},
    {"LocationID": 68, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Aesop", "LevelID": 4, "Category": "Clear"},
    {"LocationID": 69, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Unicorn", "LevelID": 5, "Category": "Collectable"},
    {"LocationID": 70, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Unicorn", "LevelID": 5, "Category": "Clear"},
    {"LocationID": 71, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Kachina", "LevelID": 6, "Category": "Collectable"},
    {"LocationID": 72, "Chapter": "INSANITY", "ChapterID": 0, "Level": "Kachina", "LevelID": 6, "Category": "Clear"},
]

LOCATION_NAME_TO_ID = {}
for loc in locations_data:
    formatted_name = f"{loc['ChapterID']}-{loc['LevelID']}: {loc['Level']} {loc['Category']}"
    LOCATION_NAME_TO_ID[formatted_name] = loc["LocationID"]

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    result = {}
    for name in location_names:
        result[name] = LOCATION_NAME_TO_ID.get(name)

    return result


def create_all_locations(world: FrostRunnerWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: FrostRunnerWorld) -> None:
    locations_by_region = {}

    for location in locations_data:
        chapter_id = location["ChapterID"]
        level_id = location["LevelID"]
        level_name = location["Level"]
        category = location["Category"]

        location_name = f"{chapter_id}-{level_id}: {level_name} {category}"

        # # used in the future when insanity levels get added, replace the code directly below
        # if chapter_id == 0:
        #     if not world.options.insanity:
        #         continue  # Skip adding these locations if the player turned insanity off
        #     region_name = f"insanity {level_id}"
        # else:
        #     region_name = f"chapter {chapter_id} level {level_id}"
        #
        # if region_name not in locations_by_region:
        #     locations_by_region[region_name] = []
        region_name = f"chapter {chapter_id} level {level_id}"
        if region_name not in locations_by_region:
            locations_by_region[region_name] = []
        #

        locations_by_region[region_name].append(location_name)

    for region_name, location_names in locations_by_region.items():
        region = world.get_region(region_name)

        location_dict_with_ids = get_location_names_with_ids(location_names)

        region.add_locations(location_dict_with_ids, FrostRunnerLocation)


def create_events(world: FrostRunnerWorld) -> None:
    return