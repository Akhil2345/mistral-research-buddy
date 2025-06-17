from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from llm import get_llm

def get_synthesizer_agent() -> Runnable:
    prompt = PromptTemplate.from_template(
        "You are a helpful AI assistant.\n\n"
        "User asked: {question}\n\n"
        "Here's what we found:\n{summary}\n\n"
        "Now respond with a helpful and clear answer."
    )
    llm = get_llm()
    return prompt | llm
