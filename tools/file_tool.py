import os
from tools.base_tool import BaseTool

class FileTool(BaseTool):

    name = "list_files"
    description = "lists files in the current directory"

    def execute(self, params=None):
        files = os.listdir()
        return files
    