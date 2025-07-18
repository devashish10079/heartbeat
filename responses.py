# responses.py
import random

def get_response(message: str) -> str:
    lowered_message = message.lower()

    if "breakup" in lowered_message:
        return "Breaking up is tough. Remember to give yourself time to heal. It's okay to feel sad, angry, or confused. Focus on self-care and lean on your support system."
    elif "fight" in lowered_message or "misunderstanding" in lowered_message:
        return "Fights happen. The key is to communicate effectively. Try to understand your partner's perspective and express your own feelings calmly. Use 'I' statements to avoid blame."
    elif "long-distance" in lowered_message:
        return "Long-distance relationships require trust and communication. Schedule regular video calls, send each other surprise gifts, and plan visits. It's the little things that count."
    elif "dating anxiety" in lowered_message:
        return "Dating can be nerve-wracking. Remember to be yourself and that it's okay if it doesn't work out with everyone. Focus on having fun and getting to know new people."
    elif "rejection" in lowered_message or "ghosting" in lowered_message:
        return "Rejection hurts, but it's not a reflection of your worth. It's a part of the dating process. Don't be afraid to put yourself out there again when you're ready."
    elif "compatibility" in lowered_message:
        return "Compatibility is about more than just shared interests. It's about shared values and life goals. Have an open and honest conversation with your partner about what you both want for the future."
    elif "communication" in lowered_message:
        return "Good communication is the foundation of any healthy relationship. Practice active listening, be honest about your feelings, and be willing to compromise."
    elif "trauma" in lowered_message or "toxic" in lowered_message:
        return "Healing from a toxic relationship takes time. Be patient with yourself and consider seeking professional help. You deserve to be in a relationship where you feel safe and respected."
    else:
        return "I'm here for you. Tell me more about what's on your mind. Remember, communication is key in any relationship."

def get_quote() -> str:
    quotes = [
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "You don't marry someone you can live with – you marry someone you cannot live without. - Unknown",
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo"
    ]
    return random.choice(quotes)

def get_vent_response() -> str:
    responses = [
        "I'm listening. Let it all out.",
        "It's okay to feel that way. I'm here for you.",
        "I'm here to support you. Tell me everything.",
        "Your feelings are valid. Don't hesitate to share."
    ]
    return random.choice(responses)
