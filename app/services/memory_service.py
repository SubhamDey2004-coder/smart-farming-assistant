# In-memory conversation storage

conversation_memory = {}


def get_conversation_history(farmer_id: str):

    if farmer_id not in conversation_memory:
        conversation_memory[farmer_id] = []

    return conversation_memory[farmer_id]


def add_to_conversation(
    farmer_id: str,
    role: str,
    content: str
):

    if farmer_id not in conversation_memory:
        conversation_memory[farmer_id] = []

    conversation_memory[farmer_id].append({
        "role": role,
        "content": content
    })

    # Keep only latest 6 messages
    conversation_memory[farmer_id] = (
        conversation_memory[farmer_id][-6:]
    )