from Model.Entity import Entity
from inspect import signature
from itertools import permutations


class PostInitMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.post_init()  # Automatically call post_init after the instance has been created.
        return instance


class Domain(metaclass=PostInitMeta):
    action_schemas = {}

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
        for sc in self.action_schemas[self.__class__.__name__]:
            sig = signature(sc)
            first = True
            for comb in permutations(self.entities, len(sig.parameters) - 1):
                action = sc(self, *comb)
                if action:
                    self.actions.append(action)
                    if first:
                        # print(action)
                        first = False
        # for ac in self.actions:
        #     print(ac)
        #     print()
        self.actions = list(set(self.actions))

    @classmethod
    def schema(cls, func):
        subclass = func.__qualname__.split(".")[0]
        cls.action_schemas.setdefault(subclass, []).append(func)
        return func
