from src.model_construction import ClaudeModel

if __name__ == "__main__":

    """ update ANTHROPIC_API_KEY environment variable """

    # we must bump the maximum number of tokens for complex queries like that below

    ai_assistant = ClaudeModel('claude-3-5-sonnet-20240620',
                               1500,
                               "You are an AI assistant with expertise in high-energy theoretical physics including string theory, general relativity, \
                               quantum field theory, and more. You compile all relevant mathematical formulas into an efficient and beautiful format using LaTeX.")

    response = ai_assistant._query_claude(
        "Give me the action for superstring theory including all ghost fields. \
        Show in a step-by-step derivation, thinking carefully through each step, how one acquires the relevant equations of motion by using the principle of least action. \
        Display the results in an easy-to-read LaTeX compiled format. Include this query word for word at the top of LaTeX document for comparative reference. \
        max_tokens = 1500."
                             )

    print(response.content)
