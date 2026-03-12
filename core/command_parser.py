class CommandParser:

    def parse(self, text):

        text = text.lower()

        if "last result" in text:
            return {
                "tool": "memory_recall",
                "params": {"key": "last_result"}
            }

        if "file" in text:
            return {
                "tool": "list_files",
                "params": {}
            }
        return None

