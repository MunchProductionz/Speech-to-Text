# Speech-to-Text

A project to learn speech-to-voice APIs and automatic report making using:
- Python 3.10.1
- Whisper AI (OpenAI)

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


### Packages

If using pip, install the following packages:

- `whisper`
- `openai`
- `openai-whisper`
- `ffmpeg`

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


## Whisper AI

### Usage

Whisper AI has multiple models, having a trade-off between speed and quality. A good balance can be found using the `Medium` model.

### Installing Whisper AI

Follow this guide to install Whisper AI:

- `https://pypi.org/project/openai-whisper/`

Proceed to start the virtual environment and add the whisper package. When using pip, write:

- `pip install -U openai-whisper`

Make sure you have `ffmpeg` installed on your computer, if not, download the latest version of `ffmpeg` (use the first link) and follow the guides (second and third link) to add the `ffmpeg' binary to your PATH environment variable:

- `https://ffmpeg.org/download.html`
- `https://www.youtube.com/watch?v=5xgegeBL0kw`
- `https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/`

Proceed to install `ffmpeg` as a Python package using:

- `pip install ffmpeg`

When using Windows, ensure that you have Chocolatey installed. If not, follow this guide:

- `https://chocolatey.org/install`

### Large Files

There are 2 files that are too big for GitHub (above 100 MB), and we therefore need to use Git LFS. Start by following this guide:

- `https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage`

When using a virtual environment, 2 files are too big for GitHub. Get around this by discarding the following changes before committing:

- `dnnl.lib`
- `torch_cpu.dll`

Follow this guide to use Git LFS:

- `https://www.youtube.com/watch?v=9HCsSD5PMSk`

Use Git to open the repository and use:

1. `git lfs track "FILE.NAME`
2. `git lfs push --all origin main`
3. `git add .`
4. `git commit -m "COMMIT MESSAGE"`
5. `git push -u origin master`

### Updating Whisper AI

To update the package to the latest version of this repository, please run:

- `pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git`

---

### Testing

## Test files

The repository contains a test file named `test.m4a`. The actual text can be found on the follow websit under the title `"Why tunnels?"`:

- `https://www.boringcompany.com/`


## Useful development plugins

- Python related:
    - [Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager)
    - [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- Git (gud):
    - [Git LFS](https://git-lfs.com/)
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    - [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
    - [GitLens - Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- General QoL:
    - [TODO Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
    - [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
    - [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
    - [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)
- Whisper AI (OpenAI)
    - [Whisper AI](https://pypi.org/project/openai-whisper/)

- Styling
    - Uses ESLint and Prettier