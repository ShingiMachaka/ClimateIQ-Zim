# 🇿🇼 ClimateIQ Zimbabwe

An AI-powered climate policy research assistant built for Zimbabwe policymakers, government agencies and NGOs.

## What it does
ClimateIQ allows users to query a curated library of official Zimbabwe and international climate documents using natural language. It returns structured answers and policy briefs grounded in the actual documents.

## Document library
Curated from official Zimbabwe government documents and international 
climate frameworks including IPCC reports, UNFCCC submissions, 
UNDP and UNEP publications.

## Built with
- Python
- Anthropic Claude API
- LangChain
- ChromaDB
- Streamlit
- HuggingFace Embeddings

## How to run locally
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies with `pip install -r requirements.txt`
4. Add your Anthropic API key to a `.env` file
5. Add your PDF documents to the `data/` folder
6. Run `python ingest.py` to build the vector database
7. Run `streamlit run app.py` to launch the app

## Built by
Shingi Machaka — MS Business Analytics & AI, American University (Kogod School of Business)
