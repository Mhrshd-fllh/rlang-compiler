class AssignmentIR:
    def __init__(self, target, expr):
        self.target = target      # str
        self.expr = expr          # str

class IfRuleIR:
    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

class AlwaysRuleIR:
    def __init__(self):
        self.statements = [] # List of AssignmentIR or IfRuleIR
        self.assignments = [] # Keep backward compatibility if accessed directly, but usage should change     # list[AssignmentIR]

class WhenRuleIR:
    def __init__(self, actions):
        self.actions = actions    # list[str]
        self.assignments = []     # list[AssignmentIR]

class RewardRuleIR:
    def __init__(self, condition, reward_expr):
        self.condition = condition # str (expr)
        self.reward_expr = reward_expr # str

class StateIR:
    def __init__(self, name, type_enum, domain=None):
        self.name = name
        self.type_enum = type_enum
        self.domain = domain # For discrete: list of strings, For continuous: (min, max)

class IRModel:
    def __init__(self):
        self.states = {}          # name -> StateIR
        self.actions = []         # ['move', 'stop']
        self.always_rules = []    # list[AlwaysRuleIR]
        self.when_rules = []      # list[WhenRuleIR]
        self.rewards = []         # list[RewardRuleIR]
        self.training_config = {} # key -> value

