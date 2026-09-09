### Pet project idea: **DevFlow — Python CLI Project & Issue Manager**

For your `01_general_it` section, I think this is a particularly good project because you can cover **all five topics in one application** instead of making unrelated scripts.

Think of it as a miniature combination of:

**Git + Jira + project manager + developer productivity CLI**

You could run commands such as:

```bash
python main.py project create "ML Recommendation System"
python main.py task add "Implement preprocessing"
python main.py task list
python main.py issue add "CSV parser crashes"
python main.py issue close 3
python main.py git status
python main.py sprint create "Sprint 1"
python main.py report
```

### What the project would contain

| Curriculum topic             | How DevFlow covers it                                             |
| ---------------------------- | ----------------------------------------------------------------- |
| Programming paradigms        | OOP, procedural/imperative code, functional-style operations      |
| Development methodologies    | Projects, sprints, backlog, tasks, priorities, statuses           |
| Git                          | Initialize repos, inspect status, commits, branches               |
| Data structures & algorithms | Queues, stacks, dictionaries, sorting, searching, priority queues |
| O-notation                   | Analyze algorithms used for searching/sorting tasks               |
| Bug tracking                 | Issues with severity, priority, status, assignee and history      |

---

# Suggested architecture

Your current structure could become:

```text
01_general_it/
│
├── 01_cli/
│   ├── main.py
│   ├── commands.py
│   └── README.md
│
├── 02_dsa/
│   ├── stack.py
│   ├── queue.py
│   ├── priority_queue.py
│   ├── searching.py
│   ├── sorting.py
│   └── complexity.md
│
├── 03_tracking/
│   ├── models.py
│   ├── issue_tracker.py
│   ├── task_manager.py
│   └── sprint_manager.py
│
├── 04_git/
│   ├── git_service.py
│   └── git_commands.py
│
├── 05_methodologies/
│   └── agile.md
│
├── data/
│   └── projects.json
│
├── tests/
│   ├── test_dsa.py
│   ├── test_tasks.py
│   └── test_issues.py
│
└── README.md
```

Eventually, I would recommend turning it into a proper Python package:

```text
devflow/
├── cli/
├── core/
├── dsa/
├── git/
├── tracking/
└── storage/
```

---

## 1. Project management

Create projects:

```text
Project:
    id
    name
    description
    created_at
    status
```

Example:

```bash
python main.py project create "UniExam"
```

Output:

```text
Project created successfully.

ID: 1
Name: UniExam
Status: ACTIVE
```

---

## 2. Task management

A task could contain:

```python
Task
 ├── id
 ├── title
 ├── description
 ├── priority
 ├── status
 ├── created_at
 └── deadline
```

Statuses:

```text
BACKLOG
TODO
IN_PROGRESS
REVIEW
DONE
```

Priorities:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Then:

```bash
python main.py task list --priority high
```

---

# 3. Build your own issue tracker

This is particularly useful because your curriculum explicitly contains **Jira / bug tracking systems**.

Example issue:

```text
Issue #17

Title: Login page crashes
Type: Bug
Priority: HIGH
Severity: MAJOR
Status: IN_PROGRESS

Created: 2026-09-09
```

CLI:

```bash
python main.py issue create
python main.py issue list
python main.py issue show 17
python main.py issue close 17
```

This gives you a miniature Jira-like system.

---

# 4. Implement real data structures

Don't just import everything from Python and call it finished.

Implement some structures yourself.

For example:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
```

Use it for:

```text
Undo actions
```

For example:

```bash
task delete 14

undo
```

Internally:

```text
Stack

DELETE TASK #14
       ↓
push(action)
       ↓
undo()
       ↓
pop(action)
```

### Queue

Use a queue for:

```text
Pending tasks
```

### Priority Queue

Use a priority queue for:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

So:

```text
Critical bug
     ↓
High bug
     ↓
Normal task
     ↓
Low task
```

That connects DSA to an actual application instead of creating toy examples.

---

# 5. Algorithms

Implement:

```text
Linear Search
Binary Search
Merge Sort
Quick Sort
```

For example:

```bash
python main.py task sort --priority
```

You can compare:

```text
Algorithm       Complexity

Linear Search   O(n)
Binary Search   O(log n)
Merge Sort      O(n log n)
Quick Sort      O(n log n) average
```

You could even benchmark them:

```text
Dataset: 100,000 tasks

Linear search:
18.4 ms

Binary search:
0.03 ms
```

That makes the project much more academically useful.

---

# 6. Git integration

Use Python's `subprocess`:

```python
subprocess.run(["git", "status"])
```

Then provide commands like:

```bash
python main.py git init
python main.py git status
python main.py git branches
python main.py git log
```

Later:

```bash
python main.py git commit "feat: add task tracker"
```

The application becomes a wrapper around common Git operations.

Do **not** try to recreate Git itself. Learn its concepts while integrating the actual Git executable.

---

# 7. Agile/Scrum functionality

Add:

```text
Project
   │
   ├── Backlog
   │
   ├── Sprint 1
   │    ├── Task
   │    ├── Task
   │    └── Bug
   │
   └── Sprint 2
```

Commands:

```bash
python main.py sprint create "Sprint 1"

python main.py sprint add-task 14

python main.py sprint start 1

python main.py sprint finish 1
```

Then generate:

```text
SPRINT REPORT

Sprint: Sprint 1

Tasks:       15
Completed:   11
Remaining:    4

Completion: 73.3%
```

That directly demonstrates your understanding of Agile rather than merely writing an `agile.md` file.

---

# 8. Programming paradigms

You can deliberately demonstrate several approaches.

### Imperative

```python
tasks = []

for task in tasks:
    if task.priority == "HIGH":
        print(task)
```

### Object-oriented

```python
class TaskManager:
    def add_task(self):
        ...

    def delete_task(self):
        ...
```

### Functional/declarative style

```python
high_priority = filter(
    lambda task: task.priority == "HIGH",
    tasks
)
```

Then explain the differences in:

```text
README.md
```

That would satisfy the curriculum topic much better than implementing random isolated examples.

---

# Development stages

I would build it incrementally.

**Stage 1 — CLI**

```text
project create
project list
project delete
```

**Stage 2 — Tasks**

```text
task add
task update
task delete
task list
```

**Stage 3 — DSA**

```text
Stack
Queue
PriorityQueue
Searching
Sorting
```

**Stage 4 — Bug tracker**

```text
issue create
issue assign
issue resolve
issue close
```

**Stage 5 — Agile**

```text
backlog
sprint
task status
reports
```

**Stage 6 — Git**

```text
git init
git status
git log
git branch
```

**Stage 7 — Testing**

Use:

```text
pytest
```

**Stage 8 — Persistence**

Start with:

```text
JSON
```

and later move to:

```text
SQLite
```

Since you have a separate `03_databases_sql` curriculum section, SQLite integration can eventually serve as a bridge into that module.

---

## The finished portfolio project

I would name it something like:

> **DevFlow — Python CLI Developer Project Management System**

GitHub description:

> A Python-based CLI project management and issue-tracking system built to demonstrate software engineering fundamentals, Git workflows, Agile methodologies, data structures, algorithms, complexity analysis, and multiple programming paradigms.

This project fits your curriculum structure particularly well because it gives your `01_general_it` directory a **single coherent purpose**:

```text
01_general_it
        │
        ↓
      DevFlow
        │
 ┌──────┼─────────┬──────────┐
 ↓      ↓         ↓          ↓
CLI    DSA       Git      Tracking
 │      │         │          │
 ↓      ↓         ↓          ↓
Python Algorithms VCS      Jira
                           concepts
```

And importantly, it is substantial enough to put on GitHub as a real pet project rather than looking like a directory of disconnected educational exercises.
