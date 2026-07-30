from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import FrostRunnerWorld

def create_and_connect_regions(world: FrostRunnerWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: FrostRunnerWorld) -> None:
    region_dict = {}

    # 6 chapters, 5 levels per chapter
    for chapter in range(1, 7):
        for level in range(1, 6):
            key = f"chapter_{chapter}_level_{level}"
            name = f"chapter {chapter} level {level}"
            region_dict[key] = Region(name, world.player, world.multiworld)

    # # Regions for insanity levels, for not not implemented
    # if world.options.insanity:
    #     for i in range(1, 7):
    #         key = f"insanity_{i}"
    #         name = f"insanity {i}"
    #         region_dict[key] = Region(name, world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = list(region_dict.values())

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: FrostRunnerWorld) -> None:
    level_names = []
    for chapter in range(1, 7):
        for level in range(1, 6):
            level_names.append(f"chapter {chapter} level {level}")

    # Connect the levels to each other in order
    for i in range(len(level_names) - 1):
        current_name = level_names[i]
        next_name = level_names[i + 1]

        current_region = world.get_region(current_name)
        next_region = world.get_region(next_name)

        entrance_name = f"{current_name} to {next_name}"
        current_region.connect(next_region, entrance_name)