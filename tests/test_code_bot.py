import pytest
from app.agents.code_bot import CodeBot

@pytest.mark.asyncio
async def test_stackoverflow_search():
    bot = CodeBot()
    results = await bot.search_stackoverflow("python factorial")
    assert isinstance(results, list)
    if results:  # اگر API جواب داد
        assert all("title" in item and "url" in item for item in results)

@pytest.mark.asyncio
async def test_code_bot_answer():
    bot = CodeBot()
    response = await bot.answer({"question": "how to use lambda in python"})
    assert response["topic"] == "code"
    assert isinstance(response["answer"], (list, str))