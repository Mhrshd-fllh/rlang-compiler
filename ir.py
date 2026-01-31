class AssignmentIR:
    def __init__(self, target, expr):
        self.target = target      # str
        self.expr = expr          # str


class AlwaysRuleIR:
    def __init__(self):
        self.assignments = []     # list[AssignmentIR]


class WhenRuleIR:
    def __init__(self, actions):
        self.actions = actions    # list[str]
        self.assignments = []     # list[AssignmentIR]


class IRModel:
    def __init__(self):
        self.states = {}          # name -> Type
        self.actions = []         # ['move', 'stop']
        self.always_rules = []    # list[AlwaysRuleIR]
        self.when_rules = []      # list[WhenRuleIR]
