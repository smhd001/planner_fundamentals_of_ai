from Planners.ForwardPlanner import ForwardPlanner
from Planners.BackwardPlanner import BackwardPlanner
from Domains.BlockWorld import BlockDomain
from Problems.BlockProblem import Block


# back = BackwardPlanner(LinkRepeatProblem(LinkRepeatDomain(1000)))
# print(back.search())

# back = BackwardPlanner(TireProblem(TireDomain()))
# print(back.search())

from Domains.TileDomain import TileDomain
from Problems.TileProblem import Tiles

# for a in d.entities:
#     print(a)
#     Block(d)

ford = BackwardPlanner(Tiles(TileDomain()))
# ford = ForwardPlanner(Block(BlockDomain(3)))

print(ford.search())

# back = BackwardPlanner(Block(BlockDomain(3)))
# print(back.search())
