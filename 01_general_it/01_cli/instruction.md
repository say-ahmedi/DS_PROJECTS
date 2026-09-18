For this first project, I would keep the scope deliberately small. The purpose of `01_cli` should be to prove that you understand **program flow, separation of responsibilities, data structures, validation, CRUD operations, error handling, and basic software design** before adding databases, APIs, Django, or other infrastructure.

## 1. What are you actually building?

Your final project should be:

> **DevFlow CLI — a terminal-based project/task management application.**

A user starts DevFlow from the terminal and manages small development projects without editing Python source files directly.

Conceptually:

```text
┌───────────────────────────────────────────────────────────┐
│                       DEVFLOW CLI                         │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  devflow> create                                          │
│  Project name: NLP Learning                               │
│  Description: Learn basic NLP                             │
│  Status: planned                                          │
│                                                           │
│  ✓ Project #1 created successfully                        │
│                                                           │
│  devflow> list                                            │
│                                                           │
│  ID   Name            Status                              │
│  1    NLP Learning    planned                             │
│                                                           │
│  devflow> show 1                                          │
│                                                           │
│  Project #1                                              │
│  Name: NLP Learning                                       │
│  Description: Learn basic NLP                             │
│  Status: planned                                          │
│                                                           │
│  devflow> update 1                                        │
│  ✓ Project updated                                        │
│                                                           │
│  devflow> delete 1                                        │
│  ✓ Project deleted                                        │
│                                                           │
│  devflow> exit                                            │
│  Goodbye.                                                 │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

That is enough for `01_cli`.

You are **not** trying to create the final DevFlow product yet.

---

# 2. The core problem

Without a CLI, your application is essentially this:

```text
User
  ↓
opens Python files
  ↓
changes variables manually
  ↓
runs Python
  ↓
gets some result
```

That is not how real users should interact with an application.

Your CLI introduces an interface:

```text
                    DEVFLOW

User
 │
 │  "create"
 ▼
┌───────────────┐
│    main.py    │
│               │
│ Understand    │
│ the request   │
└───────┬───────┘
        │
        │ create
        ▼
┌───────────────┐
│ commands.py   │
│               │
│ Perform the   │
│ operation     │
└───────┬───────┘
        │
        │ result
        ▼
┌───────────────┐
│   Terminal    │
│               │
│ ✓ Created     │
└───────────────┘
```

That architectural separation is the most important lesson of the project.

---

# 3. Final folder

Keep exactly the structure you proposed:

```text
01_cli/
├── main.py
└── commands.py
```

For this learning stage, I would **not add**:

```text
models.py
database.py
services.py
utils.py
config.py
requirements.txt
```

You will eventually need structures like these in larger applications, but adding them here would hide the fundamental lesson behind unnecessary architecture.

---

# 4. The conceptual DevFlow object

You need something for the CLI to manage.

Use a simple concept:

> **Project**

A project can conceptually contain:

| Field       | Example                 | Purpose                     |
| ----------- | ----------------------- | --------------------------- |
| ID          | `1`                   | Unique identifier           |
| Name        | `NLP Learning`        | Human-readable project name |
| Description | `Study classical NLP` | Explains the project        |
| Status      | `planned`             | Current state               |
| Priority    | `medium`              | Importance                  |

You could simplify it even further to:

```text
ID
Name
Description
Status
```

That is enough.

Do not turn this into Jira yet.

---

# 5. What commands should exist?

Your final CLI should understand seven commands.

| Command    | Meaning                    |
| ---------- | -------------------------- |
| `create` | Create a project           |
| `list`   | Display all projects       |
| `show`   | Display one project        |
| `update` | Modify an existing project |
| `delete` | Delete a project           |
| `help`   | Explain available commands |
| `exit`   | Close DevFlow              |

These cover the main CRUD operations:

```text
CREATE
   ↓
Create

READ
   ↓
List
Show

UPDATE
   ↓
Update

DELETE
   ↓
Delete
```

CRUD is one of the most important recurring patterns in software development.

You will see exactly the same concept later in:

```text
CLI applications
      ↓
REST APIs
      ↓
Django applications
      ↓
Databases
      ↓
Web applications
```

For example:

```text
CLI:

create project
show project
update project
delete project


API:

POST   /projects
GET    /projects/1
PATCH  /projects/1
DELETE /projects/1
```

Different interface, same underlying idea.

---

# 6. What should `main.py` actually be responsible for?

Think of `main.py` as:

> **Input + routing + application lifecycle**

It should not know how project creation works internally.

Its job is to understand:

```text
What did the user request?
```

Imagine:

```text
devflow> delete 4
```

`main.py` conceptually sees:

```text
INPUT
  │
  ▼
"delete 4"
  │
  ▼
Command = delete
Argument = 4
```

It then determines:

```text
Command = delete

        ↓

Which handler is responsible?

        ↓

delete operation in commands.py
```

So the flow becomes:

```text
                    main.py

┌─────────────────────────────────────┐
│ User enters command                 │
│                                     │
│            ↓                        │
│                                     │
│ Read input                          │
│                                     │
│            ↓                        │
│                                     │
│ Separate command from arguments     │
│                                     │
│            ↓                        │
│                                     │
│ Recognize command                   │
│                                     │
│            ↓                        │
│                                     │
│ Select appropriate operation        │
└────────────────┬────────────────────┘
                 │
                 ▼
             commands.py
```

---

# 7. What should NOT be inside `main.py`?

This distinction is important.

Avoid turning `main.py` into something like:

```text
main.py

parse CLI
create project
delete project
update project
search projects
format projects
store projects
validate projects
calculate IDs
manage statuses
...
```

Then `main.py` becomes responsible for everything.

Instead:

```text
main.py
│
├─ Start application
├─ Read user input
├─ Interpret command
├─ Route command
└─ Print/coordinate result
```

While:

```text
commands.py
│
├─ Create project
├─ List projects
├─ Show project
├─ Update project
└─ Delete project
```

This teaches you **separation of concerns**.

---

# 8. What should `commands.py` solve?

`commands.py` answers another question:

> Now that I know what the user wants, how do I perform it?

For example:

```text
main.py
recognizes:

"delete 4"

        ↓

commands.py receives:

delete project #4
```

`commands.py` then has to reason conceptually:

```text
Does project #4 exist?
        │
        ├── NO
        │    ↓
        │  Return:
        │  "Project not found."
        │
        └── YES
             ↓
           Remove project
             ↓
           Return:
           "Project deleted."
```

That is application logic.

---

# 9. The complete architecture

Your first project can therefore be mentally modeled like this:

```text
                    USER
                     │
                     │
                     ▼
              ┌──────────────┐
              │   Terminal   │
              └──────┬───────┘
                     │
                     │ command
                     ▼
┌────────────────────────────────────────┐
│                main.py                 │
│                                        │
│  Input                                 │
│    ↓                                   │
│  Parsing                               │
│    ↓                                   │
│  Validation of command structure       │
│    ↓                                   │
│  Routing                               │
└───────────────────┬────────────────────┘
                    │
                    │ recognized operation
                    ▼
┌────────────────────────────────────────┐
│              commands.py               │
│                                        │
│  Create                                │
│  Read                                  │
│  Update                                │
│  Delete                                │
│                                        │
│  Manage project data                   │
│  Validate operation                    │
└───────────────────┬────────────────────┘
                    │
                    │ result
                    ▼
              ┌──────────────┐
              │   Terminal   │
              └──────────────┘
```

That is your entire architecture.

---

# 10. How should data work?

Because this is your **first CLI learning project**, do not worry about databases yet.

Use an in-memory data structure conceptually.

For example:

```text
Projects
│
├── Project 1
│      ├── id
│      ├── name
│      ├── description
│      └── status
│
├── Project 2
│      ├── id
│      ├── name
│      ├── description
│      └── status
│
└── Project 3
       ├── id
       ├── name
       ├── description
       └── status
```

This gives you an opportunity to practice your **Data Structures** learning objective.

You can later decide whether projects should conceptually be stored using a list or a dictionary.

For example, consider the difference:

```text
LIST

[
 Project 1,
 Project 2,
 Project 3
]
```

Finding project `3` may require searching through projects.

Conceptually:

```text
Project 1 → not it
Project 2 → not it
Project 3 → found
```

That teaches you why some operations are approximately:

```text
O(n)
```

A dictionary-like structure conceptually gives:

```text
1 → Project 1
2 → Project 2
3 → Project 3
```

Then:

```text
projects[3]
```

can conceptually behave closer to average:

```text
O(1)
```

Now your CLI project is also reinforcing your data structures coursework.

---

# 11. I recommend making it an interactive CLI

Since you specifically want only:

```text
main.py
commands.py
```

I would make this first version an **interactive terminal program**.

The user starts DevFlow once:

```text
DevFlow CLI
Type "help" for available commands.

devflow>
```

Then the application remains running:

```text
devflow> create

...

devflow> list

...

devflow> show 1

...

devflow> update 1

...

devflow> delete 1

...

devflow> exit
```

This is particularly useful for this stage because your project data can remain in memory while the application runs.

Otherwise:

```text
Start application
↓
Create project
↓
Program exits
↓
Memory disappears
```

which would force you to introduce persistent storage before you are ready.

Persistence should be a later project.

---

# 12. How each operation should work

### Create

```text
User
 │
 │ create
 ▼
main.py
 │
 │ recognizes CREATE
 ▼
commands.py
 │
 ├─ Ask/receive name
 ├─ Ask/receive description
 ├─ Ask/receive status
 │
 ▼
Validate
 │
 ├── invalid → error message
 │
 └── valid
      ↓
Create project
      ↓
Assign ID
      ↓
Store project
      ↓
Success message
```

Expected result:

```text
✓ Project #1 created successfully.
```

---

### List

```text
User
 │
 │ list
 ▼
main.py
 │
 ▼
commands.py
 │
 ▼
Retrieve projects
 │
 ├── empty
 │     ↓
 │   "No projects found."
 │
 └── projects exist
       ↓
    Display projects
```

Result:

```text
ID    NAME              STATUS
1     NLP Learning      planned
2     UniExam           active
3     Portfolio         completed
```

---

### Show

```text
show 2
  │
  ▼
Parse ID
  │
  ▼
Find project #2
  │
  ├── Not found
  │     ↓
  │   Error
  │
  └── Found
        ↓
     Display details
```

Result:

```text
Project #2

Name: UniExam
Description: Online examination platform
Status: active
Priority: high
```

---

### Update

```text
update 2
    │
    ▼
Find project
    │
    ├── missing → error
    │
    └── exists
          ↓
       Ask what should change
          ↓
       Validate new values
          ↓
       Update project
          ↓
       Confirmation
```

---

### Delete

This operation should teach you validation.

```text
delete 2
   │
   ▼
Does #2 exist?
   │
   ├── NO → Project not found
   │
   └── YES
         ↓
      Confirm deletion?
         │
         ├── no → Cancel
         │
         └── yes
               ↓
            Delete
               ↓
            Success
```

---

# 13. Error handling is part of the project

Do not consider your CLI complete if it works only when the user behaves perfectly.

You should deliberately test bad input.

Your application needs understandable responses to situations such as:

| User input         | Expected behavior          |
| ------------------ | -------------------------- |
| `hello`          | Unknown command            |
| `show`           | Project ID required        |
| `show abc`       | Invalid ID                 |
| `show 999`       | Project not found          |
| `delete 999`     | Project not found          |
| Empty command      | Do not crash               |
| Empty project name | Reject it                  |
| Invalid status     | Explain allowed statuses   |
| `help`           | Show command documentation |
| `exit`           | Terminate cleanly          |

A good CLI behaves like this:

```text
devflow> sho 1

Unknown command: "sho"

Did you mean:
    show <id>

Type "help" to see available commands.
```

The important principle is:

> User mistakes should normally produce useful feedback, not Python exceptions.

---

# 14. Think about command states

You can restrict status to a small set:

```text
planned
active
completed
```

This gives you a valuable validation problem.

Instead of accepting:

```text
status = whatever
```

the application follows a rule:

```text
          STATUS
            │
     ┌──────┼───────┐
     ▼      ▼       ▼
 planned  active  completed
```

Something such as:

```text
banana
```

is rejected.

That teaches you an important principle:

> Data entering an application should be validated at its boundary.

---

# 15. Your development process

I would build `01_cli` in approximately this order:

1. **Define the CLI contract.** Decide exactly what `create`, `list`, `show`, `update`, `delete`, `help`, and `exit` mean, what arguments they require, and what success/error responses should look like.
2. **Design your project data.** Decide which fields a project has and which fields are required. Keep this intentionally small.
3. **Establish `main.py`.** Make it responsible for starting DevFlow, accepting input, recognizing commands, extracting arguments, and selecting the correct operation.
4. **Establish `commands.py`.** Make it responsible for actual CRUD behavior and management of the project's in-memory data.
5. **Implement one vertical workflow at a time.** Do not attempt all commands simultaneously. Conceptually complete `create → visible result`, then `list → visible result`, then `show`, `update`, and `delete`.
6. **Add validation and error cases.** Test invalid IDs, missing arguments, unknown commands, invalid status values, empty fields, and operations on nonexistent projects.
7. **Improve terminal feedback.** Messages should explain both what succeeded and what failed without exposing internal Python details unnecessarily.
8. **Refactor responsibilities.** Check whether `main.py` contains business logic or whether `commands.py` contains CLI parsing logic. Move responsibilities back to the correct layer.
9. **Manually test the complete user journey.** Start DevFlow, create several projects, list them, inspect one, update it, delete one, test invalid input, request help, and exit normally.
10. **Commit the completed milestone.** At this point, your project should demonstrate a fully usable CLI layer rather than merely individual functions.

---

# 16. What programming principles are you learning?

This small project actually touches quite a lot of your roadmap.

### Separation of concerns

```text
main.py
    ↓
CLI concerns

commands.py
    ↓
application operations
```

One component should not be responsible for everything.

---

### Single Responsibility Principle

A function responsible for creating something should not simultaneously:

```text
parse arbitrary commands
print the help menu
delete projects
start the application
```

Functions should have clearly defined responsibilities.

---

### KISS

**Keep It Simple.**

You do not need:

```text
Django
FastAPI
PostgreSQL
Docker
Redis
Celery
React
```

to learn CLI design.

Your entire application can be:

```text
terminal
   ↓
main.py
   ↓
commands.py
```

---

### DRY

If the same project lookup logic appears everywhere, notice that repetition.

For example:

```text
show → find project
update → find project
delete → find project
```

That should make you think:

> "I am repeating the same concept."

You do not need to overengineer the solution immediately, but you should learn to recognize duplication.

---

### Fail gracefully

Applications should expect bad input.

```text
Bad input
    ↓

NOT:

Traceback...
IndexError...
ValueError...

BUT:

Invalid project ID.
```

---

# 17. Imperative vs declarative programming

Your syllabus mentions:

> Programming paradigms — imperative and declarative.

This project will primarily teach **imperative programming**.

You explicitly describe the sequence:

```text
Read input
↓
Parse command
↓
Validate input
↓
Find project
↓
Modify data
↓
Display result
```

You are telling the computer **how** to perform the process step by step.

That is imperative thinking.

Later, when you use SQL:

```text
Give me all active projects
```

you are closer to declarative programming because you describe **what result you want**, while the database decides how to retrieve it.

So:

```text
01_cli
   ↓
excellent imperative-programming exercise

future database project
   ↓
good opportunity for declarative thinking
```

---

# 18. Data structures and O-notation

Your `Data structures, algorithms, O-notation` topic can also be connected naturally.

Suppose you have:

```text
10 projects
```

Searching sequentially is trivial.

Suppose you have:

```text
1,000,000 projects
```

Now your choice of data structure matters.

You should start asking questions such as:

```text
How do I store projects?

How do I retrieve one by ID?

How expensive is searching?

How expensive is insertion?

How expensive is deletion?
```

You don't need sophisticated algorithms here.

The important learning outcome is understanding that:

> Data structure selection affects how efficiently operations can be performed.

---

# 19. Git should be part of the project

Since your Git competency target is relatively high, don't develop everything and make one giant commit.

A sensible history might conceptually look like:

```text
refactor: build foundation for the first CLI project

feat: add CLI command parsing

feat: add project creation command

feat: add project listing command

feat: add project detail command

feat: add project update command

feat: add project deletion command

feat: add CLI input validation

refactor: separate command handling from CLI routing

docs: document DevFlow CLI commands
```

This gives you practice with real incremental development.

---

# 20. Development methodology

Even though this is tiny, apply a lightweight iterative process.

Think:

```text
Requirement
    ↓
Small implementation
    ↓
Test
    ↓
Review
    ↓
Refactor
    ↓
Next requirement
```

Rather than:

```text
Plan enormous application
        ↓
Write everything
        ↓
Hope it works
```

You can treat each command as a tiny user story:

```text
As a DevFlow user,
I want to create a project,
so that I can track development work.
```

Then:

```text
As a DevFlow user,
I want to list my projects,
so that I can see what I am working on.
```

This connects directly to Agile thinking.

---

# 21. Jira / bug tracking practice

You rated yourself around `1` here, so this project is a good place to introduce issue tracking without overcomplicating it.

You could conceptually create tasks such as:

```text
DEV-1 — Create CLI entry point
DEV-2 — Implement create command
DEV-3 — Implement list command
DEV-4 — Implement show command
DEV-5 — Implement update command
DEV-6 — Implement delete command
DEV-7 — Add CLI validation
DEV-8 — Improve error messages
```

And a bug:

```text
BUG-1

Title:
CLI crashes when show receives a non-numeric ID

Expected:
User receives "Invalid project ID."

Actual:
Application crashes with ValueError.
```

That is already enough to understand the fundamental reason bug trackers exist.

---

# 22. Your project's complete user journey

Your final demonstration should look approximately like this:

```text
                START
                  │
                  ▼
        ┌─────────────────┐
        │  Launch DevFlow │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Show CLI prompt │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Receive command │◄───────────────┐
        └────────┬────────┘                │
                 │                         │
                 ▼                         │
        ┌─────────────────┐                │
        │ Parse command   │                │
        └────────┬────────┘                │
                 │                         │
                 ▼                         │
          Valid command?                   │
             /      \                      │
           NO        YES                   │
           │          │                    │
           ▼          ▼                    │
      Show error   Select handler          │
           │          │                    │
           │          ▼                    │
           │     Execute operation         │
           │          │                    │
           │          ▼                    │
           │     Show result               │
           │          │                    │
           └──────────┴────────────────────┘
                       │
                    "exit"?
                    /    \
                  NO      YES
                  │        │
                  └──      ▼
                         END
```

That is the system you are building.

---

# 23. What would make the project incomplete?

Do **not** mark `01_cli` complete merely because this works:

```text
devflow> create
```

The project is incomplete if:

```text
✓ create works

✗ invalid commands crash

✗ update doesn't work

✗ IDs aren't handled correctly

✗ deleting nonexistent projects crashes

✗ help is missing

✗ responsibilities are mixed

✗ users receive confusing output
```

Functional completeness matters more than adding features.

---

# 24. Definition of Done

I would mark `01_cli` finished only when all of these statements are true:

| Requirement                 | Expected result                  |
| --------------------------- | -------------------------------- |
| Application launches        | CLI prompt appears               |
| `help` works              | Commands are explained           |
| `create` works            | Valid project is created         |
| `list` works              | Existing projects appear         |
| `show <id>` works         | Correct project is displayed     |
| `update <id>` works       | Project changes are visible      |
| `delete <id>` works       | Correct project is removed       |
| Invalid command             | Helpful error                    |
| Missing ID                  | Helpful error                    |
| Invalid ID                  | Helpful error                    |
| Missing project             | Helpful error                    |
| Invalid status              | Rejected correctly               |
| `exit` works              | Application shuts down cleanly   |
| `main.py`                 | Handles CLI interaction/routing  |
| `commands.py`             | Handles project operations       |
| No unnecessary architecture | Only two source files            |
| Code is understandable      | Clear names and responsibilities |
| Git history                 | Work is committed incrementally  |

---

# 25. What should the final project prove?

When you finish, you should be able to explain your project without talking about Python syntax:

> **DevFlow CLI is a terminal interface for managing development projects. `main.py` acts as the application entry point and interprets user commands, while `commands.py` executes the requested project operations. The application supports creating, listing, viewing, updating, and deleting projects, validates invalid input, and provides clear terminal feedback. Project data is kept in memory because this stage focuses on CLI architecture rather than persistence.**

That explanation shows much more understanding than saying:

> "I made two Python files."

The important architecture is:

```text
┌─────────┐
│  USER   │
└────┬────┘
     │
     │ command
     ▼
┌───────────────┐
│    main.py    │
│               │
│ CLI Interface │
│ Parsing       │
│ Routing       │
└───────┬───────┘
        │
        │ operation
        ▼
┌───────────────┐
│ commands.py   │
│               │
│ Business      │
│ Operations    │
│ Data handling │
└───────┬───────┘
        │
        │ result
        ▼
┌───────────────┐
│   Terminal    │
│               │
│ User feedback │
└───────────────┘
```

And your learning progression becomes:

```text
01_cli
  ↓
CLI interaction + CRUD + data structures
  ↓
02_persistence
  ↓
Save data permanently
  ↓
03_database
  ↓
SQL/database design
  ↓
04_api
  ↓
Expose operations through HTTP
  ↓
larger DevFlow application
```

That progression is particularly useful because **the CRUD concepts you learn in this tiny two-file CLI will later reappear almost unchanged at the service, database, REST API, and web-application layers.** The interface changes; the underlying software-engineering concepts remain the same.
