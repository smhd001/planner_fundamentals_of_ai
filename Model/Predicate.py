from Model.Entity import Entity


class Predicate:
    def __init__(self, name: str, entities: list[Entity]):
        # Initialize a Predicate object
        self.name = name  # Set the name of the predicate
        for ent in entities:
            if not isinstance(ent, Entity):
                raise TypeError(
                    f"all entities should be type of Entity not {type(ent)}"
                )
        self.entities = (
            entities  # Set the list of entities associated with the predicate
        )

    def __hash__(self) -> int:
        # Compute the hash value of the Predicate object
        result = 0
        PRIME = 1073741789  # A prime number for hashing
        result += self.name.__hash__() % PRIME  # Hash the name of the predicate

        # Hash each object in the list of entities
        for obj in self.entities:
            result = (result + (obj.__hash__() % PRIME)) % PRIME

        return result

    def __eq__(self, other) -> bool:
        # Check if two Predicate entities are equal
        if self.name != other.name:
            return False

        if self.__hash__() != other.__hash__():
            return False

        return self.entities == other.entities

    def __str__(self) -> str:
        return self.name + "(" + ",".join([ent.name for ent in self.entities]) + ")"

    def __repr__(self) -> str:
        return str(self)
