# test_timeline.py
```python
from wlm_world_generation_runtime.timeline_builder import build_timeline


def test_build_timeline_returns_list():
    result = build_timeline(seed="test")
    assert isinstance(result, list)
```
