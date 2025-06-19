# 🧠 Local AI Research Assistant – Your Offline Research Copilot

**Private. Multi-Agent. LangChain‑Powered.**  
A fully local system that breaks down complex topics into clean, summarized research using Mistral + LangChain — all running on your machine, no API needed.

> 📚 Built for devs, researchers & students who want ChatGPT‑style research — fully offline and customizable.

---

## ✨ What It Does

✅ Accepts a research topic or technical question  
✅ Breaks it down into multiple sub-queries  
✅ Searches local files or online (optional)  
✅ Summarizes and trims noisy content  
✅ Synthesizes a final, simplified response

---

## 🔁 Example Workflow

1. 💬 You enter a topic: “How do ZK-SNARKs work?”  
2. 🧠 Analyzer breaks it into 3–5 sub-topics  
3. 🔍 Searcher fetches local or online content  
4. ✂️ Summarizer condenses each one  
5. 🧪 Synthesizer writes the final output

---

## 🧱 Tech Stack

- 🧩 **LangChain**  
- 🦙 **Mistral LLM** via [Ollama](https://ollama.com)  
- 🐍 **Python 3.10+**

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/local_ai_searcher.git
cd local_ai_searcher

# 2. Create & activate environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Mistral via Ollama
ollama run mistral

# 5. Run the Research Assistant
python main.py


