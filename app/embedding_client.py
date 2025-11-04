# app/embedding_client.py
from dotenv import load_dotenv; load_dotenv()
from openai import OpenAI
import os

load_dotenv()

# Set your NVIDIA API Key as an environment variable before running:
# export NGC_API_KEY="your_api_key_here"
api_key=os.getenv("EMBEDDING_API_KEY")

if not api_key:
    raise ValueError("API key not found! Please check your .env file or environment variables.")


client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)
def get_embedding(text: str, input_type: str="query"):
    """
    Generate embeddings for a given text using NVIDIA Retrieval Embedding NIM.
    Returns: list of floats
    """
    response = client.embeddings.create(
        model="nvidia/nv-embedcode-7b-v1",  # use correct embedding NIM model
        input=text,
        extra_body={"input_type": input_type}
    )
    return response.data[0].embedding

# Example usage:
# if __name__ == "__main__":
#     text = "CRISPR applications in neurodegenerative diseases"
#     emb = get_embedding(text)
#     print(f"Embedding length: {len(emb)} | first 10 dims: {emb[:10]}")

if __name__ == "__main__":
    query = "CRISPR applications in neurodegenerative diseases"
    emb = get_embedding(query, input_type="query")  # for questions
    print(f" Embedding length: {len(emb)}")
    print(emb[:8])
