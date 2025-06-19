# 🚀 Local AI Research Assistant — Offline, Private & Smart 🛡️🧑‍💻

Your personal offline AI research team powered by ✨ **LangChain** + 🦙 **Mistral via Ollama**.  
Run intelligent agents that analyze, search, summarize, and synthesize — all 100% locally.

> 🏁 Think of it like having your own **AI research lab** on your laptop — no API keys, no cloud, no limits.

---

## 🌟 Project Goals

🎯 Build a **Multi-Agent Local AI Research Assistant** with:

- 🧩 Framework: `LangChain`  
- 🦙 LLM: Local `Mistral` via Ollama  
- 🤖 Agents:  
  🔍 `Analyzer` → 🌐 `Searcher` → ✂️ `Summarizer` → 🧠 `Synthesizer`

---

## 📂 Folder Structure

```bash
local_ai_searcher/
├── agents/
│   ├── analyzer.py
│   ├── searcher.py
│   ├── summarizer.py
│   └── synthesizer.py
├── main.py
├── llm.py
└── requirements.txt

# ⚙️ Setup Instructions
🧪 Step 1: Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/local_ai_searcher.git
cd local_ai_searcher

# 🐍 Step 2: Create Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install langchain langchain-community
# 🦙 Step 3: Start Mistral Locally (Ollama)
bash
Copy
Edit
ollama run mistral
# 🧠 Step 4: Create llm.py
python
Copy
Edit
# llm.py
from langchain_community.llms import Ollama

def get_llm(model="mistral"):
    return Ollama(model=model)

#🔧 How It Works
Each agent handles a specific part of the research process:

# Agent	Role
🔍 Analyzer	Parses your query & decides what’s needed
🌐 Searcher	Fetches relevant knowledge context
✂️ Summarizer	Condenses large texts into core ideas
🧠 Synthesizer	Produces structured, readable output

# 🛣️ Roadmap
Feature	Status
Agent folder setup	✅ Completed
LangChain + Mistral wired	✅ Completed
Analyzer Agent	🚧 In Progress
Other Agents (3 total)	🔜 Coming Soon
Streamlit UI (optional)	🔜 Planned
Export to PDF/Notion	🔜 Planned

# 💡 Ideal Use Cases
✅ Researching complex technical topics
✅ Summarizing papers, docs, or articles
✅ Generating structured reports from raw info
✅ Offline academic or enterprise use-cases

🤝 Contribute
Got cool agent ideas? Want to add new features like voice input or frontend UI?
PRs are welcome, bhai! Let’s build it together 💙

# 👤 Author
Made by Akhil
📫 DM for collabs, feedback, or memes 😄

# 📜 License
This project is licensed under the MIT License — use it, remix it, improve it!
