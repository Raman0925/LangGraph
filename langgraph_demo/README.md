## Hands-on LangGraph Playground

This folder contains a **hands-on LangGraph experiment**, where we learn LangGraph concepts by building a simple, stateful graph step by step.

### What this graph does

- **State type**: Uses a `TypedDict` called `state` that carries a single field: `graph_info: str`.
- **Nodes**:
  - `start_play(state)`: logs and appends a message that the start node was called.
  - `cricket(state)`: logs and appends a message about the cricket node.
  - `football(state)`: logs and appends a message about the football node.
  - `end_play(state)`: logs and appends a message that the end node was called.
- **Graph**:
  - A `Graph()` instance (from LangGraph) wires these nodes together into an executable flow.

> The idea is to **understand LangGraph by building a tiny, playful "game graph"** where each node represents a step in the game (start, choose sport, end).

---

### Learning goals

- **Understand graph state**:
  - How a `TypedDict` (here, `state`) defines the structure of data passed between nodes.
  - How each node reads from and returns updates to the state.
- **Understand nodes**:
  - Writing pure Python functions as LangGraph nodes.
  - Printing/logging from nodes to see execution order.
- **Understand the graph object**:
  - Creating a `Graph()` instance.
  - (Next steps) Adding nodes and edges in a structured way.

---

### How to run (conceptual)

> The exact run script may evolve, but at a high level you will:

1. **Initialize state**:
   - e.g. `{"graph_info": ""}`.
2. **Invoke the graph**:
   - Call the graph with the initial state.
3. **Inspect the result**:
   - Check the final `graph_info` string to see which nodes ran and in what order.

As you continue learning, you can:

- Add **conditional routing** (e.g., choose between `cricket` and `football`).
- Integrate **LLM calls** into nodes.
- Explore **checkpoints**, **persistence**, and more advanced LangGraph features.

---

### Next steps for this folder

- Document how the `Graph()` is wired (edges, entry node, end node) once that code is added.
- Add example run scripts (e.g., `run_game_graph.py`) for quick experiments.
- Extend this simple game graph into more complex LangGraph workflows as you learn new concepts.
