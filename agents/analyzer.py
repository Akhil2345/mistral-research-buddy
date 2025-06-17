from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from llm import get_llm

def get_analyzer_agent() -> Runnable:
    prompt = PromptTemplate.from_template(
        "Extract the important keywords from this question:\n\n{question}"
    )
    llm = get_llm()  # Uses Mistral
    return prompt | llm
