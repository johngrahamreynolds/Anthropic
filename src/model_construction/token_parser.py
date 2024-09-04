from abc import ABC, abstractmethod
from anthropic.types import Message
import os
import subprocess


class TokenParser(ABC):

    """ Abstract base class for parsing Claude's response tokens. To be overwritten by subclasses parsing into specific formats: Latex, Python code, etc. """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def parse_tokens(self, tokens: Message, file_name: str) -> None:
        raise NotImplementedError


class LatexParser(TokenParser):

    """ 
        Class to parse Claude's response tokens containing Latex. 
        We write Claude's Latex response to a tex file then compile it to a PDF using a bash subprocess. 
        TODO: allow for parsing of files that are not only latex - begin parsing of text '\documentclass{article}', end with '\end{document}' or similar
    """
    
    def __init__(self) -> None:
        super().__init__()

    def parse_tokens(self, tokens: Message, file_name: str) -> None:

        latex = tokens.content[0].text  # type: ignore
        
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        latex_dir_path = dir_path + '/latex/'
        
        with open(latex_dir_path + file_name + '.tex', 'w') as file:
            file.write(latex)

        # subprocess.call([f"./latex_compiler.sh"])
        subprocess.check_call(["./latex_compiler.sh", "-d", f"{latex_dir_path}", "-f", f"{file_name}"])


class PythonCodeParser(TokenParser):

    """ Class to parse Claude's response tokens containing Python code. """

    def __init__(self) -> None:
        super().__init__()

    def parse_tokens(self, tokens: Message, file_name: str) -> None:
        pass

