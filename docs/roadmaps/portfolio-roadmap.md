# OcbLawnMowing portfolio roadmap

## Snapshot
- 90-day evidence: 5 commits, 22 files touched
- Last signal: `36316a2`
- Top modified areas: `docs` (12), `00_agile` (6), `.github` workflow, `.gitignore`
- Stack: .NET
- Docs folder: yes
- Roadmap folder: no
- Features docs: yes
- Tests indexed: no

## Implemented now (V1 baseline)
- Feature documentation covers core gameplay and resource modules in `sub-module-harmony`, `sub-module-resources`, and `sub-module-screens`.
- Core logic and project structure are documented in `lawnmowing-core-logic.md` and `net-core-project-structure.md`.
- External asset references are already tracked in feature files (example-linked pages).
- No visible automated test coverage was indexed from the current scan.

## Gaps identified
- Unity mod/runtime behavior appears mostly documented but not continuously regression-tested.
- No test harness has been tied to Harmony patch points.
- Docs updates can outpace source changes, especially around resources and screens.
- CI artifacts exist but no stable coverage policy is linked from roadmap docs.

## V1 (stability and reliability)
- [ ] Add minimal automated checks for mod load/unload behavior.
- [ ] Add source-of-truth mapping from docs to runtime components for `sub-module-harmony`.
- [ ] Introduce a packaging checklist for dependency/resource changes.
- [ ] Add changelog entries when asset or resource assumptions change.

## V2 (quality and maintainability)
- [ ] Add smoke tests for Harmony hook registration and major screen flows.
- [ ] Separate experimental and shipped feature docs with explicit status markers.
- [ ] Add deterministic asset validation for referenced online resources.
- [ ] Expand CI to build and run a lightweight static quality gate.

## V10 (long-horizon productization)
- [ ] Build a maintainable mod-update workflow for map/asset updates.
- [ ] Add plugin-style architecture for new lawn logic modules.
- [ ] Add dependency governance and versioning policy for external runtime packages.
- [ ] Add an operations-focused runbook with rollback and recovery steps.

## Next steps checklist
- [ ] Create at least one integration test or harness for critical gameplay hooks.
- [ ] Tie `docs` roadmap updates to at least one release candidate.
