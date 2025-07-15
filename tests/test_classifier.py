import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app.classifier import classify_question

@pytest.mark.asyncio
async def test_classifier():
    # تست سوالات ریاضی
    math_res = await classify_question({"question": "حاصل ۲ به توان ۳"})
    assert math_res["topic"] == "math"
    
    # تست سوالات کدنویسی
    code_res = await classify_question({"question": "تعریف تابع در پایتون"})
    assert code_res["topic"] == "code"
    
    # تست سوالات سفر
    travel_res = await classify_question({"question": "هتل‌های تهران"})
    assert travel_res["topic"] == "travel"