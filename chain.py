import os
from dotenv import load_dotenv
import anthropic
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

def load_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return vectorstore.as_retriever(search_kwargs={"k": 5})

def answer_question(question: str, mode: str = "qa") -> str:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    retriever = load_retriever()
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])
    
    if mode == "brief":
        instruction = """Write a structured policy brief with these exact sections:
        
**Key Finding:** (one sentence summary)

**Evidence:** (what the documents say)

**Recommended Action:** (what policymakers should do)"""
    else:
        instruction = "Answer clearly and mention which part of the documents supports your answer."
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""You are a climate policy research assistant specializing 
in Zimbabwe and Southern Africa climate policy, emissions analysis, 
renewable energy, and sustainability assessment.

Context from documents:
{context}

{instruction}

Question: {question}"""
        }]
    )
    
    return message.content[0].text

if __name__ == "__main__":
    test = answer_question("What are Zimbabwe's main climate commitments?")
    print(test)
    