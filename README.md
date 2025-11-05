🧬 ##BioQueryAI

AI-powered Biomedical Literature Query Engine

BioQueryAI is an intelligent biomedical search and analysis system that retrieves the latest research from PubMed and other scientific sources in real-time, processes it using AI-based embeddings, and provides users with context-aware answers to biomedical questions.

Built with Streamlit, LangChain, and PubMed API integration, BioQueryAI helps researchers, students, and analysts quickly extract insights from complex biological and clinical literature.

🚀 Project Overview

Traditional PubMed searches return a list of papers, but understanding them takes hours.
BioQueryAI solves this by combining AI-powered natural language querying with automated literature retrieval, enabling users to:

Search biomedical questions in plain English

Retrieve live PubMed data dynamically

Extract, summarize, and analyze research insights instantly

Visualize or export results for downstream analysis

The system leverages:

LLM embeddings for semantic understanding

Streamlit for an interactive user interface

Real-time PubMed API calls for live literature retrieval

🧠 Core Features
Feature	Description
🔍 Live PubMed Retrieval	Fetches the most recent papers and abstracts directly using the PubMed API.
🧬 AI-Powered Semantic Search	Understands biomedical queries contextually using embeddings.
📄 Automated Summarization	Generates concise summaries of retrieved abstracts.
⚡ Real-Time Query Interface	User-friendly Streamlit app for instant search and display.
🧩 Modular Architecture	Easily extendable to other biomedical databases or local corpora.
🏗️ Tech Stack

Frontend: Streamlit

Backend: Python (FastAPI optional)

AI Engine: LangChain + OpenAI embeddings

Data Source: PubMed API

Containerization: Docker

🧰 Installation
1️⃣ Clone the repository
git clone https://github.com/antara-1505/BioQueryAI.git
cd BioQueryAI

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app locally
python -m streamlit run app/main.py


or equivalently (used in Docker):

CMD ["streamlit", "run", "app/main.py"]

🐳 Docker Setup
Build the image
docker build -t bioquery-ai .

Run the container
docker run -p 8501:8501 bioquery-ai

🧪 Example Query

Input:

“What are the latest CRISPR-based therapies for sickle cell disease?”

BioQueryAI Output:

Retrieves top PubMed papers published recently

Extracts key abstract insights

Summarizes mechanisms, results, and limitations

📚 Future Enhancements

Integration with BioRxiv and ClinicalTrials.gov

PDF paper ingestion and summarization

Fine-tuned biomedical embedding model

Research trend visualization dashboard

👩‍🔬 Author

Antara Shaw
Bioinformatics & AI Researcher
