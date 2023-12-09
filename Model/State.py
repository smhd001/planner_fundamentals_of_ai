from Model.Predicate import Predicate


class State:
    def __init__(
        self,
        action_name: str,
        positive_literals: list[Predicate] | set[Predicate],
        negative_literals: list[Predicate] | set[Predicate],
    ):
        # Initialize a State object
        self.action_name = action_name  # Set the name of the action
        self.positive_literals = set(
            positive_literals
        )  # Convert positive_literals to a set
        self.negative_literals = set(
            negative_literals
        )  # Convert negative_literals to a set
        self.parent = None

    def entails_from(self, other):
        """check if this entails from other state"""
        is_all_positive = self.positive_literals.issubset(other.positive_literals)
        is_none_negative = self.negative_literals.isdisjoint(other.positive_literals)
        return is_all_positive and is_none_negative

    def build_solution(self) -> list:
        result = []
        state = self
        while state.parent:
            result.append(state.action_name)
            state = state.parent
        result.reverse()
        return result

    def __eq__(self, other) -> bool:
        # Check if two State entities are equal
        return (
            self.positive_literals == other.positive_literals
            and self.negative_literals == other.negative_literals
        )

    def __hash__(self) -> int:
        # Compute the hash value of the State object
        result = 0
        PRIME = 1073741789  # A prime number for hashing

        # Hash each positive literal in the set of positive literals
        for positive_literal in self.positive_literals:
            result = (result + (positive_literal.__hash__() % PRIME)) % PRIME

        # Hash each negative literal in the set of negative literals
        for negative_literal in self.negative_literals:
            result = (result + (negative_literal.__hash__() % PRIME)) % PRIME

        return result

    def __str__(self) -> str:
        return (
            "Action: "
            + self.action_name
            + "\n"
            + "Positive Literals: "
            + ", ".join(
                [str(positive_literal) for positive_literal in self.positive_literals]
            )
            + "\n"
            + "Negative Literals: "
            + ", ".join(
                [str(negative_literal) for negative_literal in self.negative_literals]
            )
            + "\n"
        )
