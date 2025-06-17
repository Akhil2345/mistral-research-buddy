from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.runnables import Runnable

def get_search_agent() -> Runnable:
    search = DuckDuckGoSearchRun()
    return search
