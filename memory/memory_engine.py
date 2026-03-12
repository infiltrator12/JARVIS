class MemoryEngine:

    def __init__(self):
        self.short_term = {}

    def store(self, key, value):
        self.short_term[key] = value

    def recall(self, key):
        return self.short_term.get(key)

    def clear(self):
        self.short_term = {}

