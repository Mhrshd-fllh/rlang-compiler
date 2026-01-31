from enum import Enum


class Type(Enum):
    UNKNOWN = 0
    CONTINUOUS = 1
    DISCRETE = 2
    ACTION = 3


class Symbol:
    def __init__(self, name, symbol_type, domain=None):

        self.name = name
        self.type = symbol_type
        self.domain = domain  # e.g. ["Patrol", "Chase", "Recharge"]


class SymbolTable:
    def __init__(self):
        # name -> Symbol
        self.symbols = {}
        self.always_statements = []
        self.when_statements = []

        # --- implicit runtime symbols ---
        # current action selected by the agent in step()
        self.add_implicit_action()

    def add_implicit_action(self):
        self.symbols["action"] = Symbol("action", Type.ACTION)


    def add(self, name, symbol_type, domain=None):
        if name in self.symbols:
            raise Exception(f"خطای معنایی: '{name}' قبلاً تعریف شده است.")
        self.symbols[name] = Symbol(name, symbol_type, domain)

    def get(self, name):
        return self.symbols.get(name)


    def add_action(self, name):
        self.add(name, Type.ACTION)

    def is_action_defined(self, name):
        sym = self.get(name)
        return sym is not None and sym.type == Type.ACTION


    def is_valid_discrete_value(self, var_name, value):
        sym = self.get(var_name)
        if sym is None or sym.type != Type.DISCRETE:
            return False
        return sym.domain is not None and value in sym.domain
