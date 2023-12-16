from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate
from Model.Entity import Entity


class BlockDomain(Domain):
    def __init__(self, number_of_blocks: int):
        super().__init__("Block Domain")
        self.number_of_blocks = number_of_blocks
        for i in range(1, self.number_of_blocks + 1):
            block_string = f"Block{i}"
            self.entities.append(Entity(block_string, "Block"))
        self.table = Entity("Table", "Table")
        self.entities.append(self.table)

    @Domain.schema
    def move_action(self, b, x, y):
        if b.name == "Table" or y.name == "Table":
            return None
        move_action_name = f"Move({b.name},{x.name},{y.name})"
        on_b_x = Predicate("On", [b, x])
        clear_block_b = Predicate("Clear", [b])
        clear_block_y = Predicate("Clear", [y])

        on_b_y = Predicate("On", [b, y])
        clear_x = Predicate("Clear", [x])

        return Action(
            move_action_name,
            [on_b_x, clear_block_b, clear_block_y],
            [],
            [on_b_y, clear_x],
            [on_b_x, clear_block_y],
        )

    @Domain.schema
    def move_to_table(self, b, x):
        if b.type == "Table" or x.type == "Table":
            return None
        move_action_name = f"MoveToTable({b.name},{x.name})"
        on_b_x = Predicate("On", [b, x])
        clear_block_b = Predicate("Clear", [b])

        on_b_table = Predicate("On", [b, self.table])
        clear_x = Predicate("Clear", [x])

        return Action(
            move_action_name,
            [on_b_x, clear_block_b],
            [],
            [on_b_table, clear_x],
            [on_b_x],
        )
