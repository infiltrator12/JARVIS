from tools.system_tool import SystemTool

class JarvisCore:

    def __init__(self):
        self.system = SystemTool()

    def process(self, user_input):

        if "files" in user_input:
            return self.system.list_files()

        return "Command not recognized."