# API Reference

This document describes the public API of the **WLM‑World‑Generation‑Runtime**.

---

# `generate_world(seed: str | None = None) → dict`

```python
def generate_world(seed=None) -> dict:
    """
    Generate a minimal structural world representation.
    """
```

## Description

Runs the full world‑generation pipeline:

1. Generate spatial topology  
2. Construct timeline  
3. Build causal system  
4. Generate narrative arcs  
5. Assemble world graph  

---

## Return Format (MVP)

```json
{
  "topology": {},
  "timeline": [],
  "causality": [],
  "narrative": [],
  "world_graph": {}
}
```

---

# Internal Modules

These modules are not part of the public API but are stable entry points for extension.

### `build_topology(seed=None) → dict`
Generate spatial structure.

### `build_timeline(seed=None) → list`
Generate temporal sequence.

### `build_causality(topology, timeline) → list`
Generate causal rules.

### `build_narrative(topology, timeline, causality) → list`
Generate narrative arcs.

### `assemble_world_graph(...) → dict`
Assemble the final world graph.
