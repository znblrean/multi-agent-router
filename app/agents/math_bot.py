class MathBot:
    async def answer(self, input: dict) -> dict:
        question = input["question"]
        # This is a simple implementation - you'd use a real math solver in production
        try:
            result = eval(question)  # Caution: eval is dangerous in production!
            return {"answer": f"The answer is {result}", "topic": "math"}
        except:
            return {"answer": "I couldn't solve this math problem", "topic": "math"}