import tiktoken

prompt = """You are an American English conversation instructor whose native language is English.
Please provide feedback on English diaries written by students.
"""


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


tokens = num_tokens_from_string(prompt, "gpt-4")
print(f"Number of tokens: {tokens}")
