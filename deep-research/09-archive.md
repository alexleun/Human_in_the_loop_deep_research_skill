# Phase 9: Archive

**Who drives:** LLM (prepares), Human (approves)

**Purpose:** Close the change and preserve research output for future work.

## Pre-Archive Checklist

Before archiving, confirm:

- [ ] All tasks in the change are marked complete
- [ ] All artifacts are marked `done` in `openspec status --json`
- [ ] All code (scripts, notebooks) has been run and produces zero errors
- [ ] Last parity verification passed (if bilingual output exists)
- [ ] HTML structure validation passed (div balance check on all pages)
- [ ] Encoding scan complete — zero U+FFFD occurrences and no `??` degradation across all HTML files
- [ ] Date freshness audit passed — all footers, hero meta lines, and file timestamps match the current project epoch
- [ ] Cross-artifact consistency verified — every new finding/data point appears in all relevant output artifacts (report chapters, synthesis, dashboard, knowledge base)
- [ ] Knowledge base sources are cached in `knowledge-base/sources/`
- [ ] Source index (`sources_index.md`) is complete
- [ ] Research outputs are seeded into knowledge graph (if applicable)

**If any items are incomplete:** Flag to the human. The archive can proceed with warnings if the human confirms.

## Archive Mechanism

Run `/opsx-archive` to invoke the openspec archive skill. This will:

1. Verify artifact and task completion
2. Assess delta spec sync state (compare change specs against main specs)
3. Prompt you for sync decisions if delta specs exist
4. Move the change directory to `openspec/changes/archive/YYYY-MM-DD-<name>/`
5. Display a completion summary

**Important:** Phase 9 of this skill and the `/opsx-archive` command are the **same thing**. The deep-research skill's Phase 9 prepares the context; `/opsx-archive` executes the move. Use them together, not separately.

## The Archive Is Not Dead Storage

Future researchers can:
- Re-examine notebooks with new data
- Challenge conclusions with new perspectives
- Extend analysis to new sub-topics
- All sources remain for fact-checking
- Old figures are versioned with `_v1`, `_v2` suffixes — never deleted
