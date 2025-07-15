import wolframalpha
from sympy import sympify
import os

class MathBot:
    def __init__(self):
        
        self.api_key = os.getenv("WOLFRAM_API_KEY", "9XTAU5-8TTXRURY68")
        self.client = wolframalpha.Client(self.api_key)
    
    async def answer(self, input: dict) -> dict:
        try:
            
            res = self.client.query(input["question"])
            answer = next(res.results).text
            return {
                "answer": answer,
                "topic": "math",
                "source": "WolframAlpha"
            }
        except:
            
            try:
                expr = sympify(input["question"])
                return {
                    "answer": str(expr.evalf()),
                    "topic": "math",
                    "source": "SymPy"
                }
            except:
                return {"answer": "نتیجه‌ای یافت نشد", "topic": "math"}

from app.config.settings import settings

class MathBot:
    def __init__(self):
        self.client = wolframalpha.Client(settings.WOLFRAM_ALPHA_KEY)

from app.core.config import config

class MathBot:
    def __init__(self):
        self.client = wolframalpha.Client(config.WOLFRAM_KEY)
        self.timeout = config.TIMEOUT