from Planners.ForwardPlanner import ForwardPlanner
from Domains.BlockWorld import BlockDomain
from Problems.BlockProblem import Block


forward = ForwardPlanner(Block(BlockDomain(3)))
print(forward.search())
