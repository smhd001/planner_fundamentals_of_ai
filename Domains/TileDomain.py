from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate
from Model.Entity import Entity


class TileDomain(Domain):
    def __init__(self):
        super().__init__("8Tile Domain")
        self.Tile0 = Entity("Tile0", "Empty")
        self.entities.append(self.Tile0)
        for i in range(1, 9):
            tile_string = f"Tile{i}"
            # define self.tile1, self.tile2, etc.
            setattr(self, tile_string, Entity(tile_string, "Tile"))
            self.entities.append(Entity(tile_string, "Tile"))
        for row in range(1, 4):
            for col in range(1, 4):
                pos_string = f"p{row}{col}"
                # define self.p11, self.p12, etc.
                setattr(self, pos_string, Entity(pos_string, "Position"))
                self.entities.append(Entity(pos_string, "Position"))

    @Domain.schema
    def move_up(self, tile, pos):
        if pos.name[1] == "1" or pos.type != "Position" or tile.type != "Tile":
            return None
        x = int(pos.name[1])
        y = int(pos.name[2])
        # definitions
        new_pos_name = f"p{x-1}{y}"
        new_pos = Entity(new_pos_name, "Position")
        move_action_name = f"MoveUp {tile.name} to {new_pos.name}"

        # preconditions
        tile_on_pos = Predicate("On", [tile, pos])
        empty_on_empty = Predicate("On", [self.Tile0, new_pos])

        # results
        tile_to_empty = Predicate("On", [tile, new_pos])
        empty_to_pos = Predicate("On", [self.Tile0, pos])

        return Action(
            move_action_name,
            [tile_on_pos, empty_on_empty],
            [],
            [tile_to_empty, empty_to_pos],
            [tile_on_pos, empty_on_empty],
        )

    @Domain.schema
    def move_down(self, tile, pos):
        return Action(...)

    @Domain.schema
    def move_left(self, tile, pos):
        return Action(...)

    @Domain.schema
    def move_right(self, tile, pos):
        return Action(...)
