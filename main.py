from agents.analyzer import get_analyzer_agent
from agents.searcher import get_search_agent
from agents.summarizer import get_summarizer_agent
from agents.synthesizer import get_synthesizer_agent

if __name__ == "__main__":
    question = input("🔍 Ask me a question: ")

    analyzer = get_analyzer_agent()
    searcher = get_search_agent()
    summarizer = get_summarizer_agent()
    synthesizer = get_synthesizer_agent()

    # Step 1: Extract keywords
    keywords = analyzer.invoke({"question": question})
    print(f"\n🧠 Keywords Extracted: {keywords}")

    # Step 2: Search
    search_results = searcher.invoke(keywords)
    print(f"\n🔎 Raw Search Results:\n{search_results}")

    # Step 3: Summarize
    summary = summarizer.invoke({"search_results": search_results})
    print(f"\n📝 Summary:\n{summary}")

    # Step 4: Synthesize Final Answer
    final_answer = synthesizer.invoke({
        "question": question,
        "summary": summary
    })
    print(f"\n🤖 AI Response:\n{final_answer}")
