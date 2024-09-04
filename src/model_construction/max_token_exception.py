class MaxTokenException(Exception):
    def __init__(self, max_tokens: int) -> None:
        super().__init__(f"The current value 'max_tokens = {max_tokens}' was too small to receive the entirety of Claude's answer. \
                         Increase the value for max_tokens or simplify your query. More complex queries require more tokens.")
    