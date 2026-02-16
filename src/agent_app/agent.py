import os

from langchain_community.chat_models import FakeListChatModel
from langgraph.prebuilt import create_react_agent

# In a real app, you might use ChatOpenAI
# from langchain_openai import ChatOpenAI
from agent_app.tools import (
    add,
    count_chars,
    count_words,
    divide,
    factorial,
    is_prime,
    modulus,
    multiply,
    power,
    remove_vowels,
    replace_string,
    reverse_string,
    reverse_words,
    root,
    subtract,
    to_lower,
    to_upper,
)


def get_tools() -> list:
    """Returns the list of available tools."""
    return [
        add,
        multiply,
        subtract,
        divide,
        power,
        root,
        modulus,
        factorial,
        is_prime,
        reverse_string,
        count_chars,
        to_upper,
        to_lower,
        count_words,
        replace_string,
        reverse_words,
        remove_vowels,
    ]


def get_agent_executor() -> object:
    """Constructs and returns the agent executor (LangGraph)."""
    
    # 1. Load Tools
    tools = get_tools()

    # 2. Setup LLM
    llm = None
    if os.getenv("OPENAI_API_KEY"):
         try:
             from langchain_openai import ChatOpenAI
             llm = ChatOpenAI(temperature=0)
         except ImportError:
             print("langchain_openai not installed, falling back to Fake.")

    if not llm:
        print("Using FakeListChatModel for demo.")
        # Fake responses that mimic tool calling or final answer
        # Note: Functional tool calling with FakeListChatModel is tricky without
        # setting up exact responses that match the tool call schema.
        # For this structure demo, we'll just return a final answer directly.
        llm = FakeListChatModel(
            responses=[
                "I will calculate that for you.", # This will be the "message"
            ]
        )
        # To make it work with create_react_agent, it needs .bind_tools support.
        # FakeListChatModel might not support it fully out of the box in all versions.
        # Use with caution in this demo.

    # 3. Create Agent (LangGraph)
    # create_react_agent automatically binds tools and sets up the graph
    graph = create_react_agent(llm, tools)
    return graph
