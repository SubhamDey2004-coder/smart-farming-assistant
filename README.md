# 🌾 AI-Powered Personalized Smart Farming Assistant

An AI-powered agricultural advisory system that provides personalized farming recommendations using farmer-specific contextual data, Retrieval-Augmented Generation (RAG), and local Large Language Models (LLMs).

---

# 🚀 Project Overview

This project is designed to help farmers receive intelligent, personalized, and explainable farming guidance based on:

- Soil health
- Crop conditions
- Weather-related parameters
- Irrigation conditions
- Nutrient levels
- Pest history
- Crop growth stage
- Water availability
- Previous yield data

The system combines:

- FastAPI Backend
- SQLite Database
- SQLAlchemy ORM
- Ollama Local LLM
- Sentence Transformer Embeddings
- FAISS Vector Database
- Conversational Memory
- Rule-Based Recommendation Engine
- RAG Architecture

---

# 🧠 Core Features

## ✅ Personalized Farming Recommendations
Provides farmer-specific agricultural advice.

## ✅ Conversational AI Assistant
Supports natural language farming queries.

## ✅ Local AI Inference
Uses Ollama with local LLMs like:
- Phi3 Mini
- Llama3
- Mistral

## ✅ RAG-Based Contextual Reasoning
Uses semantic retrieval with embeddings and FAISS.

## ✅ Intelligent Recommendation Engine
Performs:
- Irrigation analysis
- Soil health analysis
- Fertilizer recommendations
- Crop suitability analysis
- Pest-risk analysis

## ✅ Conversational Memory
Maintains multi-turn conversation continuity.

## ✅ Structured JSON Responses
Frontend-friendly API responses.

---

# 🏗️ System Architecture

```text
Farmer Query
      ↓
FastAPI Backend
      ↓
Farmer Database Retrieval
      ↓
Recommendation Engine
      ↓
Conversation Memory
      ↓
LLM Prompt Construction
      ↓
Ollama Local LLM
      ↓
Structured AI Response
```

---

# ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Vector DB | FAISS |
| Embeddings | Sentence Transformers |
| LLM Runtime | Ollama |
| AI Model | Phi3 Mini / Llama3 |
| Language | Python |
| API Testing | Swagger UI |

---

# 📂 Project Structure

```text
smart-farming-assistant/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── farmer_routes.py
│   │       └── chat_routes.py
│   │
│   ├── core/
│   │   ├── database.py
│   │   └── dependencies.py
│   │
│   ├── data/
│   │   └── farmers.csv
│   │
│   ├── models/
│   │   └── farmer_model.py
│   │
│   ├── rag/
│   │   ├── documents/
│   │   ├── embeddings/
│   │   └── vector_store/
│   │
│   ├── schemas/
│   │   ├── farmer_schema.py
│   │   └── chat_schema.py
│   │
│   ├── services/
│   │   ├── rag_service.py
│   │   ├── llm_service.py
│   │   ├── recommendation_service.py
│   │   └── memory_service.py
│   │
│   ├── main.py
│   ├── init_db.py
│   └── load_data.py
│
├── requirements.txt
├── README.md
└── smart_farming.db
```

---

# 📦 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SubhamDey2004-coder/smart-farming-assistant.git
cd smart-farming-assistant
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download and install:

https://ollama.com

---

## 5️⃣ Pull AI Model

```bash
ollama run phi3:latest
```

---

## 6️⃣ Initialize Database

```bash
python -m app.init_db
```

---

## 7️⃣ Load Farmer Dataset

```bash
python -m app.load_data
```

---

## 8️⃣ Create Embeddings & FAISS Index

```bash
python -m app.rag.embeddings.create_embeddings
```

---

## 9️⃣ Run Backend Server

```bash
uvicorn app.main:app --reload
```

---

# 📘 API Documentation

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 💬 Example Chat Request

## Request

```json
{
  "farmer_id": "F006",
  "query": "How can I improve my farm productivity?"
}
```

---

## Response

```json
{
  "farmer_id": "F006",
  "recommendations": [
    "Frequent light irrigation is recommended.",
    "Add organic compost to improve soil fertility."
  ],
  "reason": "Low soil moisture and low organic carbon are affecting productivity."
}
```

---

# 🔮 Future Scope

- Weather API Integration
- Multilingual Voice Assistant
- Disease Detection using Images
- Yield Prediction
- Market Price Forecasting
- Government Scheme Recommendations
- IoT Sensor Integration
- PostgreSQL Deployment
- Dockerization

---

# 👨‍💻 Author

Subham Dey

---

# ⭐ Project Highlights

- Hybrid AI + Rule-Based System
- Personalized Agricultural Intelligence
- Local Offline AI Inference
- Retrieval-Augmented Generation (RAG)
- Scalable Backend Architecture
- Frontend-Ready Structured APIs

---