from Model.State import State
from Model.Predicate import Predicate


class Action:
    def __init__(
        self,
        action_name: str,
        positive_preconditions: list[Predicate] | set[Predicate],
        negative_preconditions: list[Predicate] | set[Predicate],
        add_list: list[Predicate] | set[Predicate],
        delete_list: list[Predicate] | set[Predicate],
    ):
        """
        Initializes an Action object.

        Parameters:
        - action_name (str): the name of the action.
        - positive_preconditions (list[Predicate]|set[Predicate]): the positive preconditions for the action.
        - negative_preconditions (list[Predicate]|set[Predicate]): the negative preconditions for the action.
        - add_list (list[Predicate]|set[Predicate]): the list of positive literals added by the action.
        - delete_list (list[Predicate]|set[Predicate]): the list of negative literals deleted by the action.
        """
        self.action_name = action_name
        self.positive_preconditions = set(positive_preconditions)
        self.negative_preconditions = set(negative_preconditions)
        self.add_list = set(add_list)
        self.delete_list = set(delete_list)

    def is_relevant(self, state: State) -> bool:
        """
        Checks if the action is relevant to the given state.

        Parameters:
        - state (State): the state to check.

        Returns:
        - True if the action is relevant to the state, False otherwise.
        """
        ...

    def regress(self, state: State) -> State:
        """
        Regresses the given state with the action effects.

        Parameters:
        - state (State): the state to regress.

        Returns:
        - The new state after regressing with the action effects.
        """
        ...
        return result

    def progress(self, state: State) -> State:
        """
        Progresses the given state with the action effects.

        Parameters:
        - state (State): the state to progress.

        Returns:
        - The new state after progressing with the action effects.
        """
        result_positive_literals = (
            state.positive_literals.union(self.add_list) - self.delete_list
        )

        result = State(self.action_name, result_positive_literals, [])
        return result

    def progress_without_delete(self, state: State) -> State:
        """
        Progresses the given state with the action effects.

        Parameters:
        - state (State): the state to progress.

        Returns:
        - The new state after progressing with the action effects.
        """
        result_positive_literals = state.positive_literals.union(self.add_list)
        result_negative_literals = state.negative_literals - self.add_list

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result

    def is_applicable(self, state: State) -> bool:
        """
        check if this action is applicable to state

        Parameters:
        - state (State): the state to state.

        Returns:
        - True if action is applicable False otherwise
        """
        return self.positive_preconditions.issubset(
            state.positive_literals
        ) and self.negative_preconditions.isdisjoint(state.positive_literals)

    def __str__(self) -> str:
        return (
            f"Action: {self.action_name}"
            + f"\nPositive preconditions: {self.positive_preconditions}"
            + f"\nNegative preconditions: {self.negative_preconditions}"
            + f"\nAdd list: {self.add_list}"
            + f"\nDelete list: {self.delete_list}\n"
        )

    def __repr__(self) -> str:
        return str(self)
