import json
from agents.analyzer import get_analyzer_agent
from agents.searcher import get_search_agent
from agents.summarizer import get_summarizer_agent
from agents.synthesizer import get_synthesizer_agent
from utils.pdf_exporter import export_to_pdf

# Step 1: Get agents
analyzer = get_analyzer_agent()
searcher = get_search_agent()
summarizer = get_summarizer_agent()
synthesizer = get_synthesizer_agent()

# Memory log
memory = []

def autonomous_loop(user_goal):
    print(f"🎯 Goal: {user_goal}")
    memory.append({"step": 0, "goal": user_goal})

    # Step 2: Task Breakdown
    task = analyzer.invoke({"question": user_goal})
    memory.append({"step": 1, "task_breakdown": task})
    print(f"\n🧠 Task Breakdown: {task}")

    # Step 3: Search
    search_results = searcher.invoke(task)
    memory.append({"step": 2, "search_results": search_results})
    print(f"\n🔍 Search Results:\n{search_results}")

    # Step 4: Summarize
    summary = summarizer.invoke({"search_results": search_results})
    memory.append({"step": 3, "summary": summary})
    print(f"\n📝 Summary:\n{summary}")

    # Step 5: Reflect + Synthesize
    final_answer = synthesizer.invoke({
        "question": user_goal,
        "summary": summary
    })
    memory.append({"step": 4, "final_answer": final_answer})

    print(f"\n✅ FINAL REPORT:\n{final_answer}")

    # Save memory to file
    with open("agent_log.json", "w") as f:
        json.dump(memory, f, indent=2)

if __name__ == "__main__":
    question = input("🤖 What should I work on today?\n> ")
    autonomous_loop(question)
export_to_pdf(memory)
