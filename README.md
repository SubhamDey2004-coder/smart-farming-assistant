# AI-Powered Personalized Smart Farming Assistant

A backend-focused agricultural advisory system that combines farmer-specific structured data, rule-based recommendations, semantic retrieval, conversation memory, and local LLM inference.

## What it does

Given a farmer ID and a natural-language question, the API:

1. Loads the farmer's structured profile from SQLite.
2. Generates recommendations for irrigation, soil health, fertilizer, crop suitability, and pest risk.
3. Maintains a short in-memory conversation history.
4. Uses a local Ollama model to turn the structured context into a concise response.
5. Exposes the workflow through FastAPI.

The repository also includes a FAISS-based embedding workflow for farmer-profile retrieval.

## Architecture

~~~text
Farmer Query
     ↓
FastAPI
     ↓
Farmer Profile (SQLite)
     ↓
Rule-Based Recommendation Engine
     ↓
Conversation Memory
     ↓
Prompt Construction
     ↓
Ollama Local LLM
     ↓
Structured JSON Response
~~~

## Core Features

- Farmer-specific contextual recommendations
- Irrigation, soil, fertilizer, crop-suitability, and pest-risk rules
- FAISS semantic retrieval workflow
- Sentence Transformer embeddings
- Local LLM inference with Ollama
- Short conversation memory per farmer
- SQLite persistence with SQLAlchemy
- CRUD API for farmer records
- Swagger / OpenAPI documentation

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Embeddings | Sentence Transformers |
| Vector store | FAISS |
| LLM runtime | Ollama |
| Data processing | Pandas |
| Language | Python |

## Project Structure

~~~text
smart-farming-assistant/
├── app/
│   ├── api/routes/
│   ├── core/
│   ├── data/
│   │   └── farmers.csv
│   ├── models/
│   ├── rag/
│   │   ├── documents/
│   │   ├── embeddings/
│   │   └── vector_store/
│   ├── schemas/
│   ├── services/
│   ├── init_db.py
│   ├── load_data.py
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
~~~

Generated FAISS files are intentionally ignored by Git and should be rebuilt locally.

## Run Locally

### 1. Create an environment

~~~bash
python -m venv .venv
~~~

Windows:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

### 2. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 3. Start Ollama

Make sure Ollama is running and the `phi3` model is available:

~~~bash
ollama run phi3
~~~

### 4. Initialize SQLite

~~~bash
python -m app.init_db
~~~

### 5. Load the sample farmer dataset

~~~bash
python -m app.load_data
~~~

### 6. Build the FAISS index

~~~bash
python -m app.rag.embeddings.create_embeddings
~~~

### 7. Start the API

~~~bash
uvicorn app.main:app --reload
~~~

API documentation:

~~~text
http://127.0.0.1:8000/docs
~~~

## API

### Farmers

- `GET /farmers/` — list farmers
- `GET /farmers/{farmer_id}` — retrieve a farmer
- `POST /farmers/` — create a farmer
- `PUT /farmers/{farmer_id}` — update a farmer
- `DELETE /farmers/{farmer_id}` — delete a farmer

### Chat

`POST /chat/`

Example:

~~~json
{
  "farmer_id": "F006",
  "query": "How can I improve my farm productivity?"
}
~~~

The response contains the farmer ID, generated recommendations, and a short reason.

## Engineering Focus

This project demonstrates a hybrid advisory architecture rather than relying on an LLM alone:

- Structured domain data provides farmer-specific context.
- Deterministic rules produce interpretable recommendations.
- FAISS + Sentence Transformers provide semantic retrieval.
- Conversation memory preserves recent context.
- Ollama provides natural-language generation.
- FastAPI exposes the system as a reusable backend service.

## Limitations

- The current weather values are stored in the sample farmer dataset rather than fetched live.
- Conversation memory is in-process and resets when the application restarts.
- The LLM depends on a locally running Ollama instance.
- FAISS artifacts must be rebuilt after changing the farmer dataset.
- The recommendation rules are a prototype and should not replace professional agricultural advice.

## Future Improvements

- Live weather API integration
- Multilingual and voice interaction
- Image-based crop disease detection
- Yield prediction
- Market-price forecasting
- IoT sensor integration
- PostgreSQL and Docker deployment

## Author

**Subham Dey**
