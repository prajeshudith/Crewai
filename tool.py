import os

from langchain.tools import tool


class FileTools:

    @tool("Write File with content")
    def write_file(data: str):
        """Useful to write a file to a given path with a given content. 
           The input to this tool should be a pipe (|) separated text 
           of length two, representing the full path of the file, 
           including the ./lore/, and the written content you want to write to it.
        """
        try:
            content = data
            path = "test.txt"
            if not path.startswith("./lore"):
                path = f"./lore/{path}"
            with open(path, "w") as f:
                f.write(content)
            return f"File written to {path}."
        except Exception:
            return "Error with the input format for the tool."