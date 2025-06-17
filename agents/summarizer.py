from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from llm import get_llm

def get_summarizer_agent() -> Runnable:
    prompt = PromptTemplate.from_template(
        "Summarize the following search results in a few key points:\n\n{search_results}"
    )
    llm = get_llm()
    return prompt | llm
