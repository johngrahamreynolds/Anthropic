import anthropic
from anthropic.types import Message
from typing import Literal

# TODO scope this to be both 1) implemented from an ABC and 2) disposable

# from abc import ABC, abstractmethod

# class ClaudeModel(ABC):
#     @abstractmethod
#     def get_claude(self) -> None:
#         pass

# class _ClaudeModel(ClaudeModel):


class ClaudeModel:

    """
    This class instantiates a specific Claude AI assistant dependent upon
    model versioning, query scaling limitations, and a chosen fundamental
    system prompt. Once the AI assistant is created, users can query the
    preconstructed model using text. Intelligent, careful prompt engineering
    will optimize responses.

    - The `claude_model` parameter must be one the available strings mappping
    to a particular Claude model: see below for the currently accepted values

    - The `max_tokens` parameter sets the maximum number of tokens generated
    by each response from Claude

    - An optional `system_prompt` paramter can be passed to engineer the
    assistance one chooses to receive from Claude (make Claude a poet,
    restrict verbosity, etc.).
    """

    def __init__(self,
                 claude_model: Literal['claude-3-5-sonnet-20240620',
                                       'claude-3-opus-20240229',
                                       'claude-3-sonnet-20240229',
                                       'claude-3-haiku-20240307',
                                       'claude-2.1',
                                       'claude-2.0',
                                       'claude-instant-1.2'],
                 max_tokens: int,
                 system_prompt: str
                 ) -> None:

        self.system_prompt = system_prompt
        self.max_tokens = max_tokens
        self.claude_model = claude_model

    def _query_claude(self, query: str) -> Message:

        claude_client = anthropic.Anthropic()

        message = claude_client.messages.create(
            model=self.claude_model,
            max_tokens=1000,
            temperature=0,
            system=self.system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": query
                        }
                    ]
                }
            ]
        )

        return message
