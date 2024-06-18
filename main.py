import tiktoken
import streamlit as st

prompt = """You are an American English conversation instructor whose native language is English. Please provide feedback on English diaries written by students.
Check the diaries for correct grammar, absence of spelling errors, and natural-sounding English.
Please reply with the correction results in the following format. The parts indicated by {} are the areas you need to correct. Please leave the other parts unchanged and reply as they are.

<h2 class="wp-block-heading">Automatic Correction Results by AI</h2>
The correction results are as follows:
<h3 class="wp-block-heading">Overall Comments</h3>
{Write feedback or comments to the student about the content of the diary in English from the perspective of an English conversation teacher.}
<h3 class="wp-block-heading">Revised Diary</h3>
{Please write the entire revised diary in English here.}
<h3 class="wp-block-heading">Explanation of Corrections</h3>
{Please provide explanations for the corrections in English. Make the explanations clear and easy to understand, including relevant knowledge and native customs to help beginner English learners in their future studies.}
"""


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


st.title("Token Counter")

input = st.text_area(label="Enter a prompt", value=prompt, height=300)
selected_model = st.selectbox(
    "Select a model",
    [
        "gpt-4",
        "gpt-3.5-turbo",
        "text-embedding-ada-002",
        "text-embedding-3-small",
        "text-embedding-3-large",
        "text-davinci-002",
        "text-davinci-003",
        "davinci",
    ],
)

if st.button("Count Tokens"):
    tokens = num_tokens_from_string(input, selected_model)
    st.write(f"Number of tokens: {tokens}")
