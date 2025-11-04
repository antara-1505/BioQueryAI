# app/llama3_client.py
from dotenv import load_dotenv; load_dotenv()
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("LLAMA3_API_KEY")
)

def query_llama3(prompt: str, temperature: float = 0.7, max_tokens: int = 512):
    """
    Send prompt to NVIDIA Llama-3.1 Nemotron-Nano-8B-v1 model.
    Returns: generated text string
    """
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-nano-vl-8b-v1",  # text inference model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        top_p=0.9,
        max_tokens=max_tokens,
        stream=True
    )

    full_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            full_response += chunk.choices[0].delta.content
    print()  # newline after stream
    return full_response

# Example usage
if __name__ == "__main__":
    answer = query_llama3("Summarize recent advances in mRNA vaccine delivery.")
    print("\n\nFinal Answer:\n", answer)
