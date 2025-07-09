class TravelBot:
    async def answer(self, input: dict) -> dict:
        question = input["question"]
        return {
            "answer": f"For travel question: '{question}', I recommend checking TripAdvisor for the best options.",
            "topic": "travel"
        }