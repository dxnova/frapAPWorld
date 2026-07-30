from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import FrostRunnerWorld

ITEM_NAME_TO_ID = {
    "Progressive Level" : 1,
    "Snowflake" : 2,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Progressive Level": ItemClassification.progression,
    "Snowflake": ItemClassification.filler
}

class FrostRunnerItem(Item):
    game = "FrostRunner"

def get_random_filler_item_name(world: FrostRunnerWorld) -> str:
    return "Snowflake"

def create_item_with_correct_classification(world: FrostRunnerWorld, name: str) -> FrostRunnerItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return FrostRunnerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: FrostRunnerWorld) -> None:
    itempool: list[Item] = []
    for _ in range(29):
        world.create_item("Progressive Level")

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool