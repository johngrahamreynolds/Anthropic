from src.model_construction import ClaudeModel

if __name__ == "__main__":

    ai_assistant = ClaudeModel('claude-3-5-sonnet-20240620',
                               1000,
                               "You give single sentence answers.")

    response = ai_assistant._query_claude(
        "I'm testing my new API. I want you to respond exactly: \
        'Hello, Brave New AI World.'"
                             )

    print(response.content)
