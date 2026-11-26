
# 🔬 ResearchMind – Multi-Agent AI Research System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/LangChain-Framework-green" />
  <img src="https://img.shields.io/badge/Groq-LLM%20Inference-orange" />
  <img src="https://img.shields.io/badge/Llama-3.3%2070B-purple" />
  <img src="https://img.shields.io/badge/Tavily-Web%20Search-blue" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit" />
</p>

<p align="center">
  🤖 An AI-powered multi-agent research application that automates web research, content extraction, report generation, and AI-based evaluation.
</p>

---

## 📌 Project Overview

ResearchMind is a multi-agent AI research application that automates topic research and report generation. It combines web search, webpage content extraction, LLM-powered writing, and AI-based critique in an interactive Streamlit application.

Users enter a research topic, run the pipeline, inspect intermediate results, review the generated report and critic feedback, and download the report as a Markdown file.

## ✨ Key Features

- 🔍 Topic-based automated research.
- 🌐 Web search through Tavily Search API.
- 📄 Webpage extraction using Requests and BeautifulSoup.
- 🤖 Specialized Search, Reader, Writer, and Critic components.
- 🧠 LLM-powered report generation using Groq-hosted Llama 3.3 70B.
- 📝 Structured research reports with introduction, key findings, conclusion, and sources.
- 📊 AI-generated report critique with a score out of 10.
- ⚡ Interactive Streamlit interface with pipeline-stage status.
- 🔎 Intermediate search results and scraped content inspection.
- 📥 Downloadable Markdown research reports.

## 🏗️ System Architecture

```text
             👤 User enters a research topic
                         |
                         v
                🌐 Streamlit Application
                         |
                         v
                   🔍 Search Agent
                (Tavily Web Search)
                         |
                         v
                   📄 Reader Agent
             (URL Selection and Scraping)
                         |
                         v
                 📚 Combined Research
                         |
                         v
                   ✍️ Writer Chain
              (Structured Report Draft)
                         |
                         v
                  📝 Generated Report
                         |
                         v
                   🧐 Critic Chain
                (Report Evaluation)
                         |
                         v
              📊 Report + Critic Feedback
                         |
                         v
                🌐 Streamlit Results UI
                         |
                         v
             📥 Download Report as Markdown
```

## 🔄 Research Pipeline

### 1️⃣ 🔍 Search Agent

- Accepts the user's research topic.
- Uses Tavily to retrieve up to five search results.
- Collects titles, URLs, and content snippets.
- Passes search output to the Reader Agent.

### 2️⃣ 📄 Reader Agent

- Chooses a relevant URL from the search results.
- Fetches the webpage using Requests.
- Parses HTML with BeautifulSoup.
- Removes script, style, navigation, and footer elements.
- Extracts readable text for the writing stage.

### 3️⃣ ✍️ Writer Chain

Combines search results and extracted webpage content to generate a structured research report containing:

- 📌 Introduction
- 🔑 Key Findings
- 📝 Conclusion
- 🔗 Sources

### 4️⃣ 🧐 Critic Chain

Reviews the generated report and returns:

- 📊 Score out of 10
- 💪 Strengths
- 🛠️ Areas to Improve
- 🎯 One-line Verdict

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core application development and pipeline orchestration |
| 🦜 LangChain | Building LLM-powered agents and chains |
| ⚡ Groq | LLM inference provider |
| 🧠 Llama 3.3 70B Versatile | Language model used by agents and chains |
| 🔍 Tavily Search API | Web search and information retrieval |
| 🌐 Requests | Sending HTTP requests to webpages |
| 📄 BeautifulSoup4 | HTML parsing and content extraction |
| 🎨 Streamlit | Interactive web application |
| 🔐 Python-dotenv | Loading API keys and environment variables |
| 🖥️ Rich | Formatted terminal output |

## 📂 Repository Structure

```text
Multi-Agent-AI-Research-System/
│
├── 📄 app.py
│   └── Streamlit application and interactive research interface
│
├── 🤖 agents.py
│   └── Search Agent, Reader Agent, Writer Chain, and Critic Chain
│
├── 🔄 pipeline.py
│   └── Sequential research pipeline orchestration
│
├── 🔧 tools.py
│   └── Tavily web search and webpage scraping tools
│
├── 📦 requirements.txt
│   └── Python project dependencies
│
└── 🚫 .gitignore
    └── Files and directories excluded from Git tracking
```

## 🚀 Getting Started

### 📋 Prerequisites

- 🐍 Python installed
- 🔑 Groq API key
- 🔑 Tavily API key

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sarthakmeher/Multi-Agent-AI-Research-System.git
cd Multi-Agent-AI-Research-System
```

### 2️⃣ Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your actual API keys.

🔐 **Security:** Never commit your `.env` file or expose API keys in source code.

### 5️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

🌐 Open the local URL printed in the terminal.

## 🎮 How to Use

1. 🚀 Start the application with `streamlit run app.py`.
2. 🌐 Open the Streamlit URL in your browser.
3. ✍️ Enter a topic in the Research Topic field.
4. ▶️ Click **Run Research Pipeline**.
5. 🔄 Follow the four stages: Search Agent, Reader Agent, Writer Chain, and Critic Chain.
6. 🔎 Inspect search results and extracted webpage content.
7. 📖 Review the generated report and critic feedback.
8. 📥 Download the report as a Markdown file.

### 💡 Example Research Topics

- 🧠 LLM Agents and Their Applications
- 🧬 CRISPR Gene Editing
- ⚡ Fusion Energy Progress

## 💻 Run the Pipeline from the Terminal

The repository also includes a standalone pipeline in `pipeline.py`:

```bash
python pipeline.py
```

⌨️ Enter a research topic when prompted.

## 📊 Output

| Output | Description |
|---|---|
| 🔍 Search Results | Titles, URLs, and snippets returned by web search |
| 📄 Scraped Content | Text extracted from a selected webpage |
| 📝 Research Report | Introduction, key findings, conclusion, and source URLs |
| 🧐 Critic Feedback | Score, strengths, improvement areas, and verdict |
| 📥 Markdown File | Downloadable research report in `.md` format |

## ⚙️ Implementation Notes

- 🧠 The LLM is configured using ChatGroq with the `llama-3.3-70b-versatile` model and temperature set to 0.
- 🔍 Tavily retrieves up to five search results per query.
- 🌐 The webpage scraping function uses an HTTP request timeout and limits extracted text to 3,000 characters.
- 📊 The Streamlit interface displays search output, scraped content, the final report, and critic feedback separately.
- 🔄 `pipeline.py` contains the standalone sequential pipeline, while `app.py` provides the interactive workflow.

## ⚠️ Limitations

- 🌐 Some websites may block scraping or rely on dynamic rendering.
- 📚 Report quality depends on the relevance and reliability of retrieved sources.
- 🤖 Critic feedback is AI-generated and is not independent fact verification.
- 🔑 API usage is subject to Groq and Tavily account limits.
- 🔄 The current workflow is sequential: search, read, write, and critique.

## 🔮 Future Improvements

- 🔍 Retrieve and compare multiple relevant sources.
- 🔗 Improve source verification and citation traceability.
- 🔁 Add retry handling for failed searches and webpage requests.
- 📄 Add PDF and DOCX report export.
- 💾 Store research history.
- 🧪 Add automated tests for individual agents and pipeline stages.
- 📊 Improve error handling and API monitoring.

## 👨‍💻 Author

**Sarthak Meher**

- 🔗 GitHub: [github.com/sarthakmeher](https://github.com/sarthakmeher)
- 📂 Repository: [Multi-Agent-AI-Research-System](https://github.com/sarthakmeher/Multi-Agent-AI-Research-System)

---

<p align="center">
  ⭐ If you find this project useful, consider giving the repository a star!
</p>
