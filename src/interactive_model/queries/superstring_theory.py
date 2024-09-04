from src.model_construction import ClaudeModel
from src.model_construction import LatexParser
from src.model_construction import MaxTokenException
import os

if __name__ == "__main__":

    """ 
        1) update ANTHROPIC_API_KEY environment variable 
        2) choose the 3 free parameters which characterize the model you query; see the ClaudeModel docstring for accepted values 
    """
    
    ai_assistant = ClaudeModel('claude-3-5-sonnet-20240620',
                               2500,
                               "You are an AI assistant with expertise in high-energy theoretical physics including string theory, general relativity, \
                               quantum field theory, and more. You compile all relevant mathematical formulas into an efficient and beautiful format using LaTeX. \
                               Your answers are consistent only of LaTeX code."
                            )

    
    response = ai_assistant._query_claude(
        "Give me the action for superstring theory including all ghost fields. \
        Show in a step-by-step derivation, thinking carefully through each step, how one acquires the relevant equations of motion by using the principle of least action. \
        Display the results in an easy-to-read LaTeX compiled format. Include this query word for word at the top of LaTeX document for comparative reference. \
        max_tokens = 2500."
                             )
    
    if response.stop_reason == "max_tokens":
        raise MaxTokenException(ai_assistant.max_tokens)
        
    latex_parser = LatexParser()
    output_file = os.path.basename(__file__)
    latex_parser.parse_tokens(response, output_file[:-3])
