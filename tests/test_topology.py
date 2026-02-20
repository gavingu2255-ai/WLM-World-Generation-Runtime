# test_topology.py
```python
from wlm_world_generation_runtime.topology_builder import build_topology


def test_build_topology_returns_dict():
    result = build_topology(seed="test")
    assert isinstance(result, dict)
```
