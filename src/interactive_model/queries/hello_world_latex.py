from src.model_construction import ClaudeModel, LatexParser, MaxTokenException
import os

if __name__ == "__main__":

    """ 
        1) update ANTHROPIC_API_KEY environment variable 
        2) choose the 3 free parameters which characterize the model you query; see the ClaudeModel docstring for accepted values 
    """

    ai_assistant = ClaudeModel(claude_model='claude-3-5-sonnet-20240620',
                               max_tokens=100,
                               system_prompt="You give single sentence answers always formatted as a Latex document.")

    response = ai_assistant._query_claude(
        "I'm testing my new API. I want you to respond exactly: \
        'Hello, Brave New AI World. My name is ____ (fill in the blank).'"
                             )
    
    if response.stop_reason == "max_tokens":
        raise MaxTokenException(ai_assistant.max_tokens)
    
    latex_parser = LatexParser()
    output_file = os.path.basename(__file__)
    latex_parser.parse_tokens(response, output_file[:-3])
