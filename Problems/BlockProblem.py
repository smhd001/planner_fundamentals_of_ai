from Domains.Domain import Domain
from Model.Predicate import Predicate
from Problems.Problem import Problem
from Model.State import State
from Model.Entity import Entity


class Block(Problem):
    def __init__(self, domain: Domain):
        super().__init__(domain)
        Block1 = Entity("Block1", "Block")
        Block2 = Entity("Block2", "Block")
        Block3 = Entity("Block3", "Block")
        Table = Entity("Table", "Table")

        on_3_table = Predicate("On", [Block3, Table])
        on_2_3 = Predicate("On", [Block2, Block3])
        on_1_2 = Predicate("On", [Block1, Block2])
        clear_1 = Predicate("Clear", [Block1])
        on_2_table = Predicate("On", [Block2, Table])
        self.initial_state = State(
            "",
            [
                on_3_table,
                on_2_3,
                on_1_2,
                clear_1,
            ],
            [],
        )

        on_3_2 = Predicate("On", [Block3, Block2])
        on_1_3 = Predicate("On", [Block1, Block3])

        self.goal_state = State("", [on_2_table, on_3_2, on_1_3, clear_1], [])
        # self.goal_state = State("", [on_1_table, on_2_3, clear_1,clear_2], [])
