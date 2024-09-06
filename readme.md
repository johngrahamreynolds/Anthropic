## Anthropic SDK Sandbox

### Overview
This project contains a virtualized development environment utilizing the `anthropic` Python SDK for testing and improving Claude's responses to a multitude of (predominantly scientific) queries across different model versions. It is designed with the VSCode IDE in mind and thereby includes various files related to installing extensions, configuring settings, etc. Feel free to clone this repo and run it in a separate IDE of your choice, deleting or ignoring irrelevant files.

### LaTeX Compilation and PDF Rendering
We implement a Python class, `LatexParser`, capable of reading a full LaTeX token response from Claude into a .tex file before compiling it and creating a PDF that is easy to interpret. 

#### Usage and Creating Custom LaTeX Queries

Users can issue a new query to Claude by creating a file `<choice_of_name>.py` and copying the outline of the .py files in the `src/interactive_model/queries` path relative to the container's working directory. Once created, users should configure the `ClaudeModel` class to take values for the `claude_model`, `max_tokens`, and `system_prompt` parameters. See the `ClaudeModel` docstring for an outline of expected values. Next, simply run the `<choice_of_name>.py` file containing the custom query to Claude, passed as the `query` argument to the `_query_claude()` func. The project code will automagically read Claude's response and return a neatly compiled set of files `<choice_of_name>.tex` and `<choice_of_name>.pdf` in the `src/latex` path. 

See the set of `hello_world_latex.py/.tex/.pdf` and `superstring_theory.py/.tex/.pdf` example files found in both of the aforementioned directories for concrete reference.

#### Notes, Issues, Drawbacks

Currently, caution must be taken when querying Claude. One must carefully engineer both the query and Claude's `system_prompt` parameter to ensure any implementation of the `LatexParser` function receives a response from Claude that is entirely LaTeX. See again the `src/interative_model/queries/hello_world_latex.py` and `src/interative_model/queries/superstring_theory.py` files for an example of a definitive system prompt. An improvement to this project will soon be made to simply pick the LaTeX portion of a response from Claude. This will remove the LaTeX-only response requirement.

A last possible issue is the `max_tokens` parameter. Each of Claude's responses are quantified in terms of the number of "tokens" he produces to adeuquately respond to a given query. If you receive an error indicating that the `max_tokens` value was too small, thereby not allowing Claude to fully print his response to you, simply increase the number. In general, more complex queries result in longer and more complex respones, driving the number of output tokens upwards. A good tactic to fully avoid this problem is to just max out the parameter. Set `max_tokens=10000`.

### Generated Code Execution environment

## Essential First Step
Before executing any queries to Claude, the user must first set set their environment variable `ANTHROPIC_API_KEY` to an active Anthropic API key. 
Simply running `ANTHROPIC_API_KEY=<your-api-key>` inside the Linux container's command line will update the value appropriately. Contact the project owner if you would like to try this out temporarily with a custom API key and he will create one for you.

<!-- ## Project Goals
1. 
2. 


<!-- ## High Level Project Structure
### [`docs/`](./docs)
Documentation on development practices and patterns.

### [`src/`](./src)


### [`tests/`](./tests)

