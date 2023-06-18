# Speech-to-Text

A project to learn speech-to-voice APIs and automatic report making using:
- Python 3.10.1
- *FILL IN API*

---

## Virtual environment

### Y though?

Python is bad at managing dependencies, especially when everything is run at a global level. We use virtual environments to get around this

### Virtual environment setup

Virtual environment created according to [this guide](https://realpython.com/python-virtual-environments-a-primer/)

1. Setup a virtual environment:
    - `python -m venv venv`
2. Activate it:
    - `source venv/bin/activate`
    - if successful you terminal should look like this: `(venv) $`

3. Install packages using `python -m pip install -r requirements.txt`
    - This should automatically install all relevant packages

4. Run program

5. Deactivate virtual environment with `deactivate`


### How to generate `requirements.txt`

1. Initiate virtual environment according to previous section 

2. Run `python -m pip freeze > requirements.txt`

### Further reading in package management

`venv` isn't deterministic and we may encounter errors in the future. This is an alternative is used:

- [Poetry - Python packaging and dependency management made easy](https://python-poetry.org/)

To start a poetry shell, use:

- `poetry shell`

To deactivate and exit the shell, use:

- `exit`

To only deactivate the virtual environsment without leaving the shell, use:

- `deactivate`

To run a single script with poetry, use:

- `poetry run python you_script.py`

---

## Useful development plugins

- Python related:
    - [Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager)
    - [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- Git (gud):
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    - [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
    - [GitLens - Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- General QoL:
    - [TODO Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
    - [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
    - [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
    - [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)
- MongoDB
    - [MongoDB for VS Code](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode)

- Styling
    - Uses ESLint and Prettier