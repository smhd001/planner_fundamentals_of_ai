from Domains.Domain import Domain
from Model.State import State


class Problem:
    def __init__(self, domain: Domain):
        # Initialize a Problem object with a specified domain
        self.domain = domain  # Store the domain for the problem
        self._initial_state: State = None
        self.goal_state: State = None

    @property
    def initial_state(self):
        return self._initial_state

    @initial_state.setter
    def initial_state(self, state: State):
        if state.negative_literals:
            raise ValueError("Initial state can't have negative literals")
        self._initial_state = state
