from dataclasses import dataclass


@dataclass
class Entity:
    name: str
    type: str

    def __hash__(self) -> int:
        result = 0
        PRIME = 1073741789  # A prime number for hashing
        result += hash(self.name) % PRIME  # Hash the name of the predicate
        result += hash(self.type) % PRIME  # Hash the name of the predicate
        return result
