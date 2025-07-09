from typing import Dict, Any
from langgraph.graph import Graph
from classifier import classify_question
from agents.math_bot import MathBot
from agents.code_bot import CodeBot
from agents.travel_bot import TravelBot

math_bot = MathBot()
code_bot = CodeBot()
travel_bot = TravelBot()

async def ask_question(question: str) -> Dict[str, Any]:
    workflow = Graph()
    
    workflow.add_node("classify", classify_question)
    workflow.add_node("math_agent", math_bot.answer)
    workflow.add_node("code_agent", code_bot.answer)
    workflow.add_node("travel_agent", travel_bot.answer)
    workflow.add_node("response", lambda x: x)
    
    workflow.add_conditional_edges(
        "classify",
        lambda x: x["topic"],
        {
            "math": "math_agent",
            "code": "code_agent",
            "travel": "travel_agent"
        }
    )
    
    workflow.add_edge("math_agent", "response")
    workflow.add_edge("code_agent", "response")
    workflow.add_edge("travel_agent", "response")
    
    workflow.set_entry_point("classify")
    workflow.set_finish_point("response")
    
    app = workflow.compile()
    result = await app.ainvoke({"question": question})
    
    return {
        "agent": result["topic"],
        "answer": result["answer"]
    }