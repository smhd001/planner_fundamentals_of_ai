from Model.Entity import Entity
from inspect import signature
from itertools import permutations


class PostInitMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.post_init()  # Automatically call post_init after the instance has been created.
        return instance


class Domain(metaclass=PostInitMeta):
    action_schemas = []

    def __init__(self, name: str):
        # Initializes a new instance of the Domain class with a given name
        self.name = name
        self.entities = []
        self.actions = []

    def post_init(self):
        # check if type of all entities is Entity
        if not self.entities:
            raise ValueError("entities is empty")

        for ent in self.entities:
            if not isinstance(ent, Entity):
                raise TypeError(
                    f"all entities should be type of Entity not {type(ent)}"
                )
        # define actions
        for sc in self.action_schemas:
            sig = signature(sc)
            for comb in permutations(self.entities, len(sig.parameters)):
                action = sc(*comb)
                if action:
                    self.actions.append(action)
        # print("entities defiend are",self.entities)
        # print("action defiend are")
        # for a in self.actions:
        #     print(a,end=' ')

    @classmethod
    def schema(cls, func):
        """this is a decorator to define schemas"""
        cls.action_schemas.append(func)
        return func
