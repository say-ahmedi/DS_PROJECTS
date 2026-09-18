For your `01_cli` folder, keep it to just these two files:

```text
01_cli/
├── main.py
└── commands.py
```

The folder as a whole should solve one main problem:

> **Allow a user to interact with DevFlow through a command-line interface instead of directly opening or modifying Python files.**

### `main.py`

**Problem it should solve:**
DevFlow needs a clear entry point that receives and understands what the user wants to do from the terminal.

Its purpose is to act as the **front door of the application**. The user should be able to launch DevFlow and express an action such as creating, listing, showing, updating, or deleting something.

The final result should be that a user can interact with DevFlow through understandable terminal commands, and the program can identify the requested action correctly.

So after finishing `main.py`, you should be able to say:

> **Solved problem:** DevFlow now has a usable command-line entry point that understands user commands and passes them into the application.

---

### `commands.py`

**Problem it should solve:**
Once DevFlow understands what the user wants, the application needs a place responsible for handling that requested action.

Its purpose is to connect the user's CLI request with the appropriate DevFlow operation.

For example, conceptually, a user may request:

```text
Create a project
List projects
Delete a project
Show a project
```

`commands.py` should represent the layer that handles those requests.

The final result should be that each recognized user action produces the expected application behavior and an understandable result.

So after finishing `commands.py`, you should be able to say:

> **Solved problem:** DevFlow can now take recognized CLI requests and execute the corresponding application actions.

---

The distinction is therefore simple:

| File            | Problem                                                 | Purpose                         | Final result                            |
| --------------- | ------------------------------------------------------- | ------------------------------- | --------------------------------------- |
| `main.py`     | How does DevFlow understand what the user asks for?     | Receive and interpret CLI input | User commands are correctly recognized  |
| `commands.py` | What should DevFlow do after understanding the request? | Handle the requested operation  | Correct application action is performed |

Your completed `01_cli` module should ultimately demonstrate this workflow:

```text
User gives command
        ↓
DevFlow understands request
        ↓
DevFlow selects correct action
        ↓
Action is executed
        ↓
User receives a clear result
```

So the **final purpose of the entire `01_cli` folder** is:

> **Provide a complete terminal-based interaction layer for DevFlow, where users can issue commands and receive meaningful results without interacting with the internal modules directly.**

You can consider `01_cli` completed when it proves that DevFlow has a functional command-line interface from **user request → recognized command → executed action → visible result**.
