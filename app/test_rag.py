from app.services.rag_service import (
    retrieve_relevant_context
)

query = "Which farmer has low water availability?"

results = retrieve_relevant_context(query)

for result in results:

    print("\n")
    print("Farmer ID:", result["farmer_id"])
    print(result["content"])
    print("=" * 80)