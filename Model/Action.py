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

    def progress(self, state: State) -> State:
        """
        Progresses the given state with the action effects.

        Parameters:
        - state (State): the state to progress.

        Returns:
        - The new state after progressing with the action effects.
        """
        ...
        result = State(...)
        return result

    def is_applicable(self, state: State) -> bool:
        """
        check if this action is applicable to state

        Parameters:
        - state (State): the state to state.

        Returns:
        - True if action is applicable False otherwise
        """
        ...

    def __str__(self) -> str:
        return self.action_name
