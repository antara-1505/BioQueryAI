# BioQueryAI

## AI-powered Biomedical Literature Query Engine

BioQueryAI is an intelligent biomedical search and analysis system that retrieves the latest research from PubMed and other scientific sources in real-time, processes it using AI-based embeddings, and provides users with context-aware answers to biomedical questions.

Built with Streamlit, LangChain, and PubMed API integration, BioQueryAI helps researchers, students, and analysts quickly extract insights from complex biological and clinical literature.

<h2>🚀 Project Overview</h2>

Traditional PubMed searches return a list of papers, but understanding them takes hours.
BioQueryAI solves this by combining AI-powered natural language querying with automated literature retrieval, enabling users to:
      Search biomedical questions in plain English
      Retrieve live PubMed data dynamically
      Extract, summarize and analyze research insights instantly
      Visualize or export results for downstream analysis

The system leverages:
      LLM embeddings for semantic understanding
      Streamlit for an interactive user interface
      Real-time PubMed API calls for live literature retrieval

<h2>🧠 Core Features</h2>
Feature          	                Description
🔍 Live PubMed Retrieval    	  Fetches the most recent papers and abstracts directly using the PubMed API.
🧬 AI-Powered Semantic Search  	Understands biomedical queries contextually using embeddings.
📄 Automated Summarization	    Generates concise summaries of retrieved abstracts.
⚡ Real-Time Query Interface	  User-friendly Streamlit app for instant search and display.
🧩 Modular Architecture	        Easily extendable to other biomedical databases or local corpora.


<h2>🏗️ Tech Stack</h2>
Frontend: Streamlit
Backend: Python (FastAPI optional)
AI Engine: LangChain + OpenAI embeddings
Data Source: PubMed API
Containerization: Docker

<h2>🧰 Installation </h2>
<h4>1️⃣ Clone the repository</h4>
git clone https://github.com/antara-1505/BioQueryAI.git
cd BioQueryAI

<h4>2️⃣ Create a virtual environment</h4>
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

<h4>3️⃣ Install dependencies</h4>
pip install -r requirements.txt

<h4>4️⃣ Run the app locally</h4>
python -m streamlit run app/main.py


or equivalently (used in Docker):

CMD ["streamlit", "run", "app/main.py"]

<h2>🐳 Docker Setup</h2>
<h4>Build the image</h4>
docker build -t bioquery-ai .

<h4>Run the container</h4>
docker run -p 8501:8501 bioquery-ai

<h2>🧪 Example Query</h2>

Input:
“What are the latest CRISPR-based therapies for sickle cell disease?”

BioQueryAI Output:
Retrieves top PubMed papers published recently
Extracts key abstract insights
Summarizes mechanisms, results and limitations

<h2>📚 Future Enhancements</h2>

Integration with BioRxiv and ClinicalTrials.gov
PDF paper ingestion and summarization
Fine-tuned biomedical embedding model
Research trend visualization dashboard

👩‍🔬 Author
Antara Shaw




