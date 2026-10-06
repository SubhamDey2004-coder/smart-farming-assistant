# AI-Powered Personalized Smart Farming Assistant

A backend-focused agricultural advisory system that combines farmer-specific data, rule-based recommendations, semantic retrieval, and local LLM inference to provide contextual farming guidance.

## Problem

Generic agricultural advice does not always account for a farmer's soil, crop, weather, irrigation, nutrient, or pest context. This project explores a personalized advisory workflow that combines structured data with retrieved agricultural knowledge.

## Architecture

```text
Farmer Query
     ↓
FastAPI API
     ↓
Farmer Context Retrieval
     ↓
Recommendation Engine
     ↓
RAG Retrieval (FAISS)
     ↓
Conversation Memory
     ↓
Prompt Construction
     ↓
Ollama Local LLM
     ↓
Structured Response
```

## Core Features

- Farmer-specific contextual recommendations
- Natural-language conversational interface
- Rule-based recommendation engine
- Retrieval-Augmented Generation
- Local LLM inference through Ollama
- Sentence Transformer embeddings
- FAISS vector search
- Conversational memory
- Structured JSON API responses
- SQLite persistence with SQLAlchemy

## Recommendation Areas

The current design covers areas such as:

- Irrigation
- Soil health
- Fertilizer recommendations
- Crop suitability
- Pest-risk analysis

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Embeddings | Sentence Transformers |
| Vector database | FAISS |
| LLM runtime | Ollama |
| Language | Python |
| API docs | Swagger / OpenAPI |

## Project Structure

```text
smart-farming-assistant/
├── app/
│   ├── api/
│   ├── core/
│   ├── data/
│   ├── models/
│   ├── rag/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   ├── init_db.py
│   └── load_data.py
├── requirements.txt
├── README.md
└── smart_farming.db
```

## Run Locally

### 1. Create an environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama and pull a local model

For example:

```bash
ollama run phi3:latest
```

### 4. Initialize the database

```bash
python -m app.init_db
```

### 5. Load farmer data

```bash
python -m app.load_data
```

### 6. Build the embedding index

```bash
python -m app.rag.embeddings.create_embeddings
```

### 7. Start the API

```bash
uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Example

A request can provide a farmer identifier and a natural-language question:

```json
{
  "farmer_id": "F006",
  "query": "How can I improve my farm productivity?"
}
```

The service returns structured recommendations together with reasoning based on the available farmer context.

## Engineering Focus

This project demonstrates how structured business/domain data can be combined with RAG and local LLM inference rather than relying on an LLM alone.

## Future Improvements

- Weather API integration
- Multilingual voice interaction
- Image-based disease detection
- Yield prediction
- Market-price forecasting
- Government-scheme recommendations
- IoT sensor integration
- PostgreSQL and Docker deployment

## Author

**Subham Dey**
