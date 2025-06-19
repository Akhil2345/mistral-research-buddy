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


# 🧪 Step 1: Clone the Repo
git clone https://github.com/yourusername/local_ai_searcher.git
cd local_ai_searcher

# 🐍 Step 2: Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 📦 Step 3: Manual Install (If needed)
pip install langchain langchain-community

# 🦙 Step 4: Start Mistral LLM Locally
ollama run mistral


---

## ⚙️ Setup

### 🧪 Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/local_ai_searcher.git
cd local_ai_searcher


🐍 Step 2: Create Virtual Environment & Activate
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🦙 Step 4: Run Mistral via Ollama
bash
Copy
Edit
ollama run mistral
🚀 How It Works
🔧 Agent	🧠 Role Description
🧠 Analyzer	Breaks user query into actionable steps
🌍 Searcher	Grabs relevant context (local/web/etc.)
✂️ Summarizer	Trims and filters for core info
🧪 Synthesizer	Assembles final readable output

Agents talk to each other using LangChain chains — building up clean, local, smart output 🔥

🔮 Roadmap
 Basic agent pipeline (Analyzer → Synthesizer)

 Add PDF/URL input support

 Add long-context chunk handling

 Export results to Notion, PDF

 Streamlit frontend UI

👤 Author
Made with 💙 by Akhil
Feel free to fork, use, or extend — PRs welcome!


