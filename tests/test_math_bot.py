import sys
import os
# اضافه کردن مسیر پروژه به sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app.agents.math_bot import MathBot

@pytest.mark.asyncio
async def test_math_bot():
    bot = MathBot()
    response = await bot.answer({"question": "2+2"})
    assert response["topic"] == "math"
    assert "4" in response["answer"]