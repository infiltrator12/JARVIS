class BaseTool:

    name = ""
    description = ""

    def execute(self, params=None):
        raise NotImplementedError("Tool must implement execute method.")