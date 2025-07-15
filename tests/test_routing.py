import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.classifier import classify_question

async def test_classify_math():
    result = await classify_question({"question": "What is 2+2?"})
    assert result["topic"] == "math"

async def test_classify_code():
    result = await classify_question({"question": "How to write Python function?"})
    assert result["topic"] == "code"

async def test_classify_travel():
    result = await classify_question({"question": "Best places to visit in Paris?"})
    assert result["topic"] == "travel"

    import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.classifier import classify_question

