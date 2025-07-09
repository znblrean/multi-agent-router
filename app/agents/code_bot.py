class CodeBot:
    async def answer(self, input: dict) -> dict:
        question = input["question"]
        return {
            "answer": f"For Python coding question: '{question}', you should check the official Python documentation.",
            "topic": "code"
        }