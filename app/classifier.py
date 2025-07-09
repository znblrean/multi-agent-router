from typing import Dict

async def classify_question(input: Dict) -> Dict:
    question = input["question"].lower()
    
    if "python" in question or "code" in question or "program" in question:
        return {"topic": "code"}
    elif "travel" in question or "trip" in question or "visit" in question:
        return {"topic": "travel"}
    elif "math" in question or "calculate" in question or any(op in question for op in ["+", "-", "*", "/"]):
        return {"topic": "math"}
    else:
        return {"topic": "code"}  # default to code