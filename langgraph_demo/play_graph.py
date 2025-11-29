from typing_extensions import TypedDict
import random
from typing import Literal
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display


class state(TypedDict):
    graph_info: str


def start_play(state: "state") -> "state":
    print("start Play node has been called")
    return {"graph_info": state["graph_info"] + "start Play node has been called"}


def random_play(state: "state") -> Literal["cricket", "football"]:
    print("random Play node has been called")
    if random.random() < 0.5:
        return "cricket"
    else:
        return "football"


def cricket(state: "state") -> "state":
    print("cricket node has been called")
    return {"graph_info": state["graph_info"] + "cricket node has been called"}


def football(state: "state") -> "state":
    print("football node has been called")
    return {"graph_info": state["graph_info"] + "football node has been called"}


def end_play(state: "state") -> "state":
    print("end Play node has been called")
    return {"graph_info": state["graph_info"] + "end Play node has been called"}


graph = StateGraph(state)
graph.add_node("start_play", start_play)

graph.add_node("cricket", cricket)
graph.add_node("football", football)
graph.add_node("end_play", end_play)

graph.add_edge(START, "start_play")
graph.add_conditional_edges("start_play", random_play)
graph.add_edge("cricket", "end_play")
graph.add_edge("football", "end_play")
graph.add_edge("end_play", END)

graph_builder = graph.compile()

display(Image(graph_builder.get_graph().draw_mermaid_png()))

graph_builder.invoke({"graph_info": ""})