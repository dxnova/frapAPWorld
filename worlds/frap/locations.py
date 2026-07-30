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


base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "locations.json")

with open(json_path, "r") as file:
    locations_data = json.load(file)

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