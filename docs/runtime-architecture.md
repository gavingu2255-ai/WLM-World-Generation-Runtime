# Runtime Architecture

The **WLM‑World‑Generation‑Runtime** is organized into five core modules, each responsible for a distinct stage of the world‑generation pipeline.

```
Seed
  ↓
Topology Generation
  ↓
Timeline Construction
  ↓
Causal‑System Scaffolding
  ↓
Narrative‑Arc Structuring
  ↓
World‑Graph Assembly
```

---

## Module Breakdown

### 1. `topology_builder`
Generates spatial structure for the world.  
MVP implementation returns an empty dict.

### 2. `timeline_builder`
Constructs a temporal sequence of events or eras.

### 3. `causal_engine`
Builds causal rules and causal relationships between world elements.

### 4. `narrative_engine`
Generates narrative arcs and story‑level scaffolding.

### 5. `world_graph`
Assembles the final world graph from all components.

---

## Orchestration Flow

The `generate_world()` API coordinates all modules:

```
topology = build_topology(seed)
timeline = build_timeline(seed)
causality = build_causality(topology, timeline)
narrative = build_narrative(topology, timeline, causality)
world_graph = assemble_world_graph(...)
```

---

## Design Principles

- **Minimal** — only the runtime skeleton  
- **Deterministic** — same seed → same world  
- **Composable** — modules can be replaced independently  
- **Transparent** — all structures are inspectable  
- **Extensible** — downstream systems can plug in real logic  
