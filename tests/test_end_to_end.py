# test_end_to_end.py
```python
from wlm_world_generation_runtime import generate_world


def test_generate_world_pipeline_runs():
    world = generate_world(seed="test")
    assert isinstance(world, dict)
    assert "topology" in world
    assert "timeline" in world
    assert "causality" in world
    assert "narrative" in world
    assert "world_graph" in world
```
