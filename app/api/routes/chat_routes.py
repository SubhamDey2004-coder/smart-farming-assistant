from fastapi import APIRouter, HTTPException
import json

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from app.services.rag_service import (
    get_farmer_profile,
    get_farmer_object
)

from app.services.llm_service import (
    generate_llm_response
)

from app.services.recommendation_service import (
    analyze_irrigation,
    analyze_soil_health,
    analyze_fertilizer,
    analyze_crop_suitability,
    analyze_pest_risk
)

from app.services.memory_service import (
    get_conversation_history,
    add_to_conversation
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
def farmer_chat(request: ChatRequest):

    # Get farmer object
    farmer = get_farmer_object(
        request.farmer_id
    )

    if not farmer:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    # Get farmer profile
    farmer_profile = get_farmer_profile(
        request.farmer_id
    )

    # Recommendation Engine
    irrigation_advice = analyze_irrigation(farmer)

    soil_advice = analyze_soil_health(farmer)

    fertilizer_advice = analyze_fertilizer(farmer)

    crop_advice = analyze_crop_suitability(farmer)

    pest_advice = analyze_pest_risk(farmer)

    recommendation_text = "\n".join(
        irrigation_advice +
        soil_advice +
        fertilizer_advice +
        crop_advice +
        pest_advice
    )

    # Get conversation memory
    conversation_history = get_conversation_history(
        request.farmer_id
    )

    history_text = ""

    for message in conversation_history:

        history_text += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n"
        )

    # Build Prompt
    prompt = f"""
    You are an expert AI agricultural assistant.

    Your job is to provide:
    - practical farming advice
    - concise recommendations
    - personalized guidance

    STRICT RULES:
    - Focus ONLY on the farmer profile.
    - Never mention other farmers.
    - Never invent information.
    - Keep recommendations concise.
    - Do NOT ask follow-up questions.
    - Return ONLY valid JSON.
    - Do NOT return markdown.
    - Do NOT return explanations outside JSON.

    JSON FORMAT:
    {{
        "recommendations": [
            "recommendation 1",
            "recommendation 2"
        ],
        "reason": "short explanation"
    }}

    Farmer Profile:
    {farmer_profile}

    Recommendation Engine Output:
    {recommendation_text}

    Previous Conversation:
    {history_text}

    Current Farmer Question:
    {request.query}
    """

    # Generate LLM response
    response = generate_llm_response(prompt)

    # Parse JSON safely
    try:

        parsed_response = json.loads(response)

    except Exception:

        parsed_response = {
            "recommendations": [
                "Unable to generate structured recommendation."
            ],
            "reason": "Model response formatting error."
        }

    # Save user message
    add_to_conversation(
        request.farmer_id,
        "user",
        request.query
    )

    # Save assistant response
    add_to_conversation(
        request.farmer_id,
        "assistant",
        str(parsed_response)
    )

    return {
        "farmer_id": request.farmer_id,
        "recommendations": parsed_response.get(
            "recommendations",
            []
        ),
        "reason": parsed_response.get(
            "reason",
            ""
        )
    }