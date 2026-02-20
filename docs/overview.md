# WLM‑World‑Generation‑Runtime — Overview

The **WLM‑World‑Generation‑Runtime** is the execution layer for the WLM World Generation Protocol (WGP).  
It provides the minimal runtime components required to support:

- spatial topology generation  
- temporal timeline construction  
- causal‑system scaffolding  
- narrative‑arc structuring  
- world‑graph assembly  

This runtime is intentionally minimal.  
It is designed to be extended or replaced by downstream systems.

---

## Purpose

The runtime provides:

- a clean Python package  
- stable module boundaries  
- placeholder implementations  
- consistent API surface  
- testable interfaces  
- documentation scaffolding  

It does **not** implement the full world‑generation logic.  
That logic is defined in the **WLM‑World‑Generation‑Protocol** (protocol layer).

---

## Position in the WLM Stack

```
Dimensional Structure → Worlds / Universes / Narratives / Simulations
```

This runtime corresponds to the **seventh layer** of the WLM protocol stack.

---

## Key Modules

- `topology_builder` — spatial structure generation  
- `timeline_builder` — temporal sequence generation  
- `causal_engine` — causal‑rule scaffolding  
- `narrative_engine` — narrative‑arc structuring  
- `world_graph` — final world‑graph assembly  

---

## Status

- Runtime skeleton: complete  
- Placeholder logic: complete  
- Ready for extension: yes  
