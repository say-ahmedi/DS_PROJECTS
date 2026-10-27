# Project and roadmap assessment

Assessment date: 27 October 2026. Scope: the local repository at this date. This is a static review of files and saved notebook state; it is not a full notebook execution audit.

## Executive assessment

This repository is an early-stage Data Engineer / Data Science learning portfolio. It has a broad curriculum, a small interactive Python CLI project, exploratory statistics and linear algebra notebooks, and a separate Math for ML track. The strongest evidence of implementation is in the CLI and a handful of notebooks. The planned database, warehouse, cloud, ML, deep learning, NLP, computer vision, time-series, and MLOps sections have no files. There is no integrated data or ML platform yet.

The key management issue is that `roadmap.md` is a poorly converted certificate and skills matrix, not a dependable progress tracker. Its `100.00%` entry is in a skills/importance table and should not be interpreted as implementation completion. `README.md` contains a much clearer proposed project sequence, but it also mixes plans, examples, and a claim that `01_cli` is complete. That claim needs a narrower definition: the CLI implements interactive project CRUD in memory, but not the task/issue/Git/sprint/persistence scope described elsewhere.

## Observed progress

| Area | Evidence | Assessment |
| --- | --- | --- |
| General IT | `01_general_it/01_cli/main.py` and `commands.py` implement an interactive create/list/show/update/delete flow for projects. | Functional learning prototype; broader DevFlow plan remains unimplemented. |
| Mathematics and statistics | 68 notebook paths in `02_maths_statistics`; 7 have code cells, 58 have no code cells, and 3 are zero-byte files. | Substantial topic outline and some exercises, but file count overstates completed practice. |
| Math for ML | 15 notebooks in `99_math_for_ml`; 2 contain code cells and 13 contain no code cells. Two linear algebra labs include many executed cells. | Active early implementation; most of this track is scaffolded. |
| Python data analysis | 3 notebooks with code cells in `06_python_data_analysis/00_python`. | Basic language work exists; the EDA and dashboard projects described in `README.md` are not present. |
| Database through MLOps | `03`, `04`, `05`, and `07` through `12` top-level directories have zero files. | Planned only. |

These counts measure repository evidence, not mastery or validated completion. Saved notebook outputs show prior execution, but do not establish that every notebook runs cleanly from a fresh kernel. The three zero-byte notebooks are invalid notebook files.

## Technical architecture

The repository is organized by curriculum stage (`01` through `12`) plus `99_math_for_ml`. It uses Markdown for instructions, Jupyter notebooks for explanations and exercises, and Python scripts for DevFlow. No project-wide Python package, dependency manifest, automated test suite, or CI configuration is present.

The executable CLI has two layers: `main.py` reads commands in a loop and dispatches to `Commands`; `commands.py` owns project operations and data. Storage is a class-level dictionary, so state is shared among `Commands` instances in one process and lost when the process exits. IDs and counters are instance attributes after first increment, which can diverge from the shared dictionary. The entry point runs on import, reducing testability. Command parsing uses repeated `split()` calls and silently ignores many unsupported inputs.

The notebooks are organized as course-style learning units. That works for concept exploration, but there is no reproducible environment or automated notebook validation. The separate `02_maths_statistics` and `99_math_for_ml` tracks overlap in linear algebra and statistics; their distinct roles are not documented in a central index.

## Roadmap analysis

`roadmap.md` contains a certificate supplement, a recommended study-plan/skills matrix, and weighted topics covering general IT, mathematics, databases, DWH/ETL, cloud, Python, ML/DL, time series, NLP, and CV. The subject coverage is broad and relevant to the stated Data Engineer / Data Science direction. The matrix is useful as a source syllabus, but it lacks per-topic status, evidence links, owner, date, prerequisites, acceptance criteria, and a definition of done.

The Markdown conversion is damaged: extremely wide and broken tables, `#DIV/0` formula remnants, `#RANGE!` links, and `file:///` references to a temporary Windows path. This makes the document hard to review and unsuitable as the canonical progress record. The `100.00%` at line 215 appears alongside aggregate skill weights, not completed work.

`README.md` adds two partially competing portfolio plans: an eight-project shortlist and a later twelve-section project table. It gives a useful learning sequence and project outcomes, but the breadth can cause repeated projects before core skills are validated. The stated next target of `01_general_it/02_dsa` does not exist. The `99_math_for_ml/01_needed_first/01_linear_algebra/README.md` refers to `ACCEPTANCE_CRITERIA.md` and `04_capstone_transaction_similarity.ipynb`, neither of which exists. The README's final `01_cli = COMPLETE` label therefore needs a scope-specific qualification.

## Strengths

1. Clear curriculum breadth from programming and mathematics to data engineering and ML production.
2. Practical project ideas and explicit learning outcomes in the root README and module notes.
3. A working interactive CLI prototype gives a concrete software engineering starting point.
4. The Math for ML linear algebra module articulates useful acceptance criteria, such as shape checks, assertions, fresh-kernel execution, and written interpretation.
5. Some statistics and linear algebra notebooks contain code and saved outputs, demonstrating hands-on work beyond a pure topic list.

## Weaknesses and risks

1. **Progress cannot be audited from the roadmap.** It mixes certificate material, topic weights, and plans without verified completion evidence.
2. **Scaffolding can be mistaken for delivery.** Most notebook paths lack code cells, three are zero-byte files, and nine of the twelve numbered areas have no files.
3. **DevFlow scope is inconsistent.** The implemented project manager supports in-memory project CRUD; the broader task/issue/Git/sprint system and JSON persistence are aspirational.
4. **CLI data behavior needs correction.** Shared class state and per-instance counters can cause inconsistent IDs; updates can partially change name/description before rejecting an invalid status; list prints the header once per project.
5. **Reproducibility is weak.** There is no dependency lock/manifest, automated test suite, CI, or verified fresh-kernel run for notebooks.
6. **Documentation maintenance is weak.** The malformed roadmap, broken local links, missing acceptance/capstone files, and overlapping math tracks make the next step harder to identify.
7. **Repository hygiene needs attention.** A compiled Python cache file is tracked, while `.gitignore` does not cover common notebook checkpoints and Python caches. An `.env` file is present locally and ignored; its contents were not inspected.

## Recommended next steps, in priority order

### 1. Establish one trustworthy progress index

Keep the original skills matrix as a reference, but replace its progress role with a concise table: topic, target artifact, status (`planned`, `in progress`, `verified`), acceptance criteria, evidence link, and last verified date. Only use `verified` after code/notebook execution and review. Define whether a file is a note, scaffold, exercise, or completed deliverable. Link the root README to this index and avoid duplicate portfolio plans.

### 2. Close the current learning loop before expanding scope

Finish the current Math for ML linear algebra unit: resolve the missing acceptance checklist and capstone reference, complete the third notebook and capstone if still intended, and execute each completed notebook from a fresh kernel. Repair or remove the three zero-byte statistics notebooks. Mark existing markdown-only notebooks as planned rather than completed. This produces a measurable, reviewable milestone.

### 3. Tighten DevFlow to its actual learning objective

Either define `01_cli` as a finished *interactive CRUD exercise* or implement the promised persistence and task/issue scope. For a small, high-value technical pass: move project state and ID allocation into instance initialization; validate all update input before mutation; make command parsing explicit with usage/error feedback; guard the entry point; and add a few behavior tests for create, invalid status, update, delete, and persistence if added. Avoid enlarging DevFlow just to satisfy every aspirational feature in the General IT essay.

### 4. Make the repository reproducible

Add a small Python dependency manifest with a supported Python version and setup instructions. Add a notebook validation command or CI job for a selected set of completed notebooks, keeping long/network-dependent lessons outside the default gate. Ignore `__pycache__/`, `*.pyc`, and `.ipynb_checkpoints/`; remove the tracked cache file in a separate cleanup change.

### 5. Reduce and sequence the portfolio

Choose one major artifact per stage, with explicit prerequisites and exit criteria. A practical order is: Python/CLI and DSA basics; probability/statistics/linear algebra; SQL; a reproducible EDA project; a single tabular ML project; then DWH/cloud or NLP specialization as career priorities dictate. Reuse the best project for deployment and MLOps rather than starting a new toy application. Treat the eight-project list as a possible portfolio target, not a requirement to build all eight before demonstrating depth.

## Verification and limits

I inspected the repository tree, roadmap and README text, CLI source, notebook JSON structure and saved execution metadata, and recent Git history. Python AST parsing succeeded for both CLI scripts. I did not execute the notebooks end-to-end, install dependencies, use external data, or infer learning completion from file names alone. Existing working-tree changes in `roadmap.md`, one math notebook, and `image/` were left untouched.
