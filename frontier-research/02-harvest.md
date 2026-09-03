# Phase 2: Multi-Source Data Harvesting

**Purpose:** Ingest data from all acceptable source types with explicit per-source trust weighting, producing a curated, weighted source database for downstream verification.

**Core method:** Source-Agnostic Ingestion with trust weighting.

**Execution pattern:** Parallel sub-sessions, one per source type or region/discipline. Output `raw_data/` + `access/02-source-manifest.json`.

---

## Procedure

1. **Read the trusted source list** from `project-state.json` → `user_constraints.accepted_sources` and the system map from Phase 1 (which variables need evidence).

2. **Ingest per source type.** Support ALL of the following, in parallel where possible:
   - **Academic papers** — ArXiv, IEEE, Nature, ACL, etc.
   - **Codebases** — GitHub / GitLab repositories
   - **Raw datasets** — CSV / JSON data files
   - **Patents** — Google Patents and equivalents
   - **Web / News** — blogs, vendor pages, news

3. **Assign trust weighting.** Tag every source with its type and trust weight. Pre-prints and web sources carry **lower** weight than peer-reviewed or authoritative primary sources:

   | Source Type | Trust Weight |
   |---|---|
   | Peer-reviewed paper / standard / authoritative spec | High |
   | Pre-print (arXiv, no peer review) | Medium (flagged) |
   | Code / reproducible artifact | Medium–High (if reproducible) |
   | Patents | Medium |
   | Raw dataset | Medium–High (validated in Phase 3) |
   | Web / news / vendor page | Low (flagged) |

4. **Preserve source artifacts.** Save a local copy of each ingested source (paper PDF/abstract, code snapshot, dataset file, patent page, web HTML) so Phase 3 verification and later citation have primary access — never rely on a live URL alone.

5. **Write `access/02-source-manifest.json`** — one entry per source: id, type, trust weight, local_copy path, ephemeral flags (pre-print, vendor, etc.).

6. **Apply the Calculations First guardrail** if any harvesting step requires unit conversion or aggregation math — derive it explicitly, do not assert a number.

---

## Output: access/02-source-manifest.json

```json
{
  "source_manifest": [
    {
      "source_id": "SRC-001",
      "type": "paper",
      "trust_weight": "high",
      "ephemeral": false,
      "local_copy": "raw_data/papers/SRC-001.pdf"
    },
    {
      "source_id": "SRC-002",
      "type": "preprint",
      "trust_weight": "medium",
      "ephemeral": true,
      "local_copy": "raw_data/papers/SRC-002-abstract.html"
    },
    {
      "source_id": "SRC-003",
      "type": "web",
      "trust_weight": "low",
      "ephemeral": true,
      "local_copy": "raw_data/web/SRC-003.html"
    }
  ]
}
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `access/02-source-manifest.json` exists and covers every source type needed for the topic
2. ✅ Every source has a `type`, `trust_weight`, and `local_copy` path
3. ✅ Source coverage matches the variables/boundaries defined in the Phase 1 system map (no variable lacking evidence)
4. ✅ Pre-prints and web sources are explicitly flagged as lower-trust
5. ✅ All source artifacts are preserved locally (no dependency on live URLs)
6. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT skip the trust weighting — it is essential for Phase 3 triangulation and Phase 5 stress-testing
- Do NOT ignore accepted_sources in `project-state.json` — harvest only within the user's trusted source list
- Do NOT rely on live URLs alone; always save a local copy
- Do NOT proceed to Phase 3 before the source manifest is complete
