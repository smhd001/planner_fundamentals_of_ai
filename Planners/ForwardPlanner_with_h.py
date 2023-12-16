from queue import Queue
from queue import PriorityQueue
from Planners.Planner import Planner
from Model.State import State

"""
result is a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.

frontier is a queue data structure that stores the states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.

visited is a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or all_states again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop

"""


class ForwardPlanner(Planner):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        ...

        return []

    def successor(self, current_state):
        result = []
        for action in self.problem.domain.actions:
            # Check if action is applicable to state
            if action.is_applicable(current_state):
                new_state = action.progress(current_state)
                # Set parent state and action
                new_state.parent = current_state
                result.append(new_state)

        return result

    def idl_heuristic(self, state) -> int:
        return 10000