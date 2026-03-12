import json
import os

class PersistentMemory:

    def __init__(self, filename="memory.json"):
        self.filename = filename
        self.data = {}

        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.data = json.load(f)

    def store(self, key, value):
        self.data[key] = value
        self._save()
        print(f"[Memory] stored {key} = {value}")

    def recall(self, key):
        return self.data.get(key)

    def clear(self):
        self.data = {}
        self._save()

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=2)