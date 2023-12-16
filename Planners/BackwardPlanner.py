from queue import Queue
from Model.State import State

from Planners.Planner import Planner

"""
result is a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.

frontier is a queue data structure that states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.

visited is a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or all_states again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop

"""


class BackwardPlanner(Planner):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        result = []
        frontier = Queue()
        visited = set()
        initial = self.problem.initial_state

        # Check if initial state is already reached
        if self.problem.goal_state.initial_test(initial):
            return result

        # Add goal state to frontier and visited set
        frontier.put(self.problem.goal_state)
        visited.add(self.problem.goal_state)

        while not frontier.empty():
            current_state = frontier.get()

            # Generate predecessor states
            predecessor_states = self.predecessor(current_state)

            for predecessor_state in predecessor_states:
                # If goal state(here initial) is found, build solution and return
                if predecessor_state.initial_test(initial):
                    s = predecessor_state.build_solution()
                    s.reverse()
                    return s

                # Add predecessor state to frontier and visited set
                if predecessor_state not in visited:
                    frontier.put(predecessor_state)
                    visited.add(predecessor_state)

        return result

    def predecessor(self, current_state) -> list[State]:
        result = []

        # Generate predecessor states for each action in domain

        return result

    def build_solution(self, state):
        result = []

        # Build solution by tracing back parent states from goal state
        while state.parent:
            result.append(state.action_name)
            state = state.parent

        return result
