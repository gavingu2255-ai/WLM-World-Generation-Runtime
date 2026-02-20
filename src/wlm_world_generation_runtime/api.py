# api.py
```python
"""
Public API for WLM‑World‑Generation‑Runtime.
"""

from .topology_builder import build_topology
from .timeline_builder import build_timeline
from .causal_engine import build_causality
from .narrative_engine import build_narrative
from .world_graph import assemble_world_graph


def generate_world(seed=None) -> dict:
    """
    Orchestrate the full world‑generation runtime pipeline.
    """
    topology = build_topology(seed=seed)
    timeline = build_timeline(seed=seed)
    causality = build_causality(topology, timeline)
    narrative = build_narrative(topology, timeline, causality)
    world_graph = assemble_world_graph(
        topology=topology,
        timeline=timeline,
        causality=causality,
        narrative=narrative,
    )

    return {
        "topology": topology,
        "timeline": timeline,
        "causality": causality,
        "narrative": narrative,
        "world_graph": world_graph,
    }
```
