from typing_extensions import TypedDict

class state(TypedDict):
    graph_info:str

def start_play(state:State):
    print("start Play node has been called")
    return {"graph_info": state["graph_info"] + "start Play node has been called"}

def cricket(state:State):
    print("cricket node has been called")
    return {"graph_info": state["graph_info"] + "cricket node has been called"}

def football(state:State):
    print("football node has been called")
    return {"graph_info": state["graph_info"] + "football node has been called"}

def end_play(state:State):
    print("end Play node has been called")
    return {"graph_info": state["graph_info"] + "end Play node has been called"}

graph = Graph()