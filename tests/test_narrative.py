# test_narrative.py
```python
from wlm_world_generation_runtime.narrative_engine import build_narrative


def test_build_narrative_returns_list():
    result = build_narrative({}, [], [])
    assert isinstance(result, list)
```
