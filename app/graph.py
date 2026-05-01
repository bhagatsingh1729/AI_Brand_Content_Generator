from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import json

from app.prompts import content_prompt, router_prompt

# ---------------- STATE ----------------
class AgentState(TypedDict):
    input_data: dict
    model_choice: str
    final_output: dict


# ---------------- ROUTER NODE ----------------
def router_node(state: AgentState):
    llm = ChatOpenAI(model="gpt-4o-mini")

    messages = router_prompt.format_messages(**state["input_data"])
    response = llm.invoke(messages)

    try:
        parsed = json.loads(response.content)
        model = parsed.get("selected_model", "gpt-4o-mini")
    except:
        model = "gpt-4o-mini"

    return {
        **state,
        "model_choice": model
    }


# ---------------- CONTENT NODE ----------------
def content_node(state: AgentState):
    model_name = state["model_choice"]

    llm = ChatOpenAI(model=model_name)

    messages = content_prompt.format_messages(**state["input_data"])
    response = llm.invoke(messages)

    try:
        parsed = json.loads(response.content)
    except:
        parsed = {
            "content": response.content,
            "content_type": "text",
            "tone_used": "unknown",
            "strategy_used": "unknown"
        }

    return {
        **state,
        "final_output": parsed
    }


# ---------------- GRAPH ----------------
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("router", router_node)
    builder.add_node("generator", content_node)

    builder.set_entry_point("router")
    builder.add_edge("router", "generator")
    builder.add_edge("generator", END)

    return builder.compile()


graph = build_graph()