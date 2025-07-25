# ✅ Submission: Ops Tech Builder – Python + AI Integration Challenge

This is my solution to the technical challenge. The code is organized into the following parts:

## ✅ What I Implemented

### 📦 Part 1: LLM API Endpoint
- Implemented using FastAPI (`api/main.py`)
- Accepts a JSON `{ "text": "..." }` and returns `{ "summary": "..." }` from GPT-3.5-turbo
- API key is loaded via `.env` using `dotenv`

### 📂 Part 2: Excel/CSV Parser
- Parses `.csv` or `.xlsx` files with flexible headers and inconsistent values
- Cleans up entries like `"N/A"`, `"??"`, `-500`, missing PO numbers
- Outputs a JSON list (`parser/parser.py`)

### 🧠 Part 3: Prompt Comparison
- Uses OpenAI API to compare prompt outputs
- Example prompt: extract names, dates, locations from a paragraph
- Script: `prompts/compare_prompts.py


### 🧮 Part 4 (Optional): SQL Query
- SQL query to get top 5 vendors by total approved payments in last 30 days
- File: `sql/top_vendor.sql`

### How to run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Create a .env file:
```
OPENAI_API_KEY=your_openai_key_here
```
3. Run FastAPI server:
```
uvicorn api.main:app --reload
```
4. Run scripts:
```
Parser: python parser/parser.py
Prompt comparison: python prompts/compare_prompts.py
```


# 🛠 Ops Tech Builder – Python + AI Integration Challenge

Welcome! This short technical challenge is designed to evaluate your ability to work with Python, APIs, and structured data — the core of our day-to-day automation and integration work. We’re less focused on flashy frontends, and more interested in clean, working backend logic.

---

## 🔍 About the Role

This test simulates what you’ll be doing in the role:
- Building API endpoints that call AI models (e.g., OpenAI, Claude)
- Parsing Excel/CSV documents for real-world operations
- Thinking clearly about how to process, transform, and extract useful information
- Comparing prompt performance across different LLMs

---

## ✅ What You’ll Build

### 📦 Part 1: LLM API Endpoint (30 mins)
- Build a Flask or FastAPI app with one POST endpoint: `/summarize`
- Accepts input like: `{ "text": "some input" }`
- Calls the OpenAI API (real or mocked)
- Returns only: `{ "summary": "..." }`
- **Bonus**: Allow switching between OpenAI and Claude via a parameter

---

### 📂 Part 2: Excel/CSV Parser (20 mins)
- Write a script or API that:
  - Accepts a `.csv` or `.xlsx` file (simulate it if needed)
  - Extracts key fields (e.g., PO Number, Vendor, Amount)
  - Returns a clean JSON list
  - Handles missing headers and odd formatting

---

### 🧠 Part 3 (Bonus): Prompt Comparison (10 mins)
- Write one or two prompts that extract names, dates, and locations from a paragraph
- Run the same prompts on GPT and Claude (or describe expected differences)
- Briefly explain how you’d normalize the outputs

---

## 🛠 Optional Add-on (Part 4): SQL Query (5 mins)
Write a SQL query:
> Given a table `invoices(id, vendor, amount, status, created_at)`,  
> return the top 5 vendors by **total amount paid** in the last 30 days.

---

## 📤 Submission Instructions
1. Fork this repo or upload your scripts to a public GitHub repo
2. Organize into folders: `/api`, `/parser`, `/prompts`, `/sql`
3. Submit your repo link via the Google Form
4. Optionally record a Loom video to walk through your thought process

---

## 🧪 Evaluation Criteria
- Python fluency and code clarity
- Ability to work with files and external APIs
- Understanding of prompt design and LLM output handling
- Practical logic and documentation
- Bonus for flexibility, abstraction, or multi-model support

---

### Tech You'll Likely Use
- Python (Flask or FastAPI, Pandas, OpenAI API)
- Excel/CSV handling (openpyxl, csv, pandas)
- Optional SQL (Postgres dialect preferred)
- Mock or real AI model access

We look forward to seeing how you approach real-world automation problems!


