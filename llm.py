from langchain_community.llms import Ollama

def get_llm(model: str = "mistral"):
    return Ollama(model=model)
