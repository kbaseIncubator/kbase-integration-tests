# `pipenv`

This project uses [`poetry`](https://python-poetry.org), a relatively new to KBase projects. Traditionally KBase Python projects have used virtual environments, `pip`, and a `requirements.txt` file listing the project dependencies.

`poetry` does not work too differently, but has different installation instructions. Internally, `poetry` does create and use a virtual environment and uses `pip` for dependency management.

`poetry` stores dependency information in a pair of configuration files.

Poetry has its own config file named `poetry.toml` which is used to control poetry's behavior. We use it to instruct poetry to create a virtual environment within the project folder. (This is disabled in the image build which places dependencies in the system.)

The second file `pyproject.toml` is a new standard Python file for describing a project, including the task of `requirements.txt`, to describe the dependencies and their versions.

A third file, `poetry.lock` is created when dependencies or added, and should be updated whenever pyproject.toml is updated, e.g. when adding a new dependency.

The lock file is one of the keys to success with poetry (or Pipenv for that matter.) It describes all dependencies and their precise versions as installed. When dependencies are installed with poetry, it consults the lockfile if it exists, and ignores pyproject.toml.

## Setting up `poetry` on your host machine

Note that when using a docker workflow, it is not really "necessary" to use poetry directly, unless one is updating dependencies.

However, since most developers will surely be using an editor or IDE which supports intellisense, api lookup, identification of unavailable imports, etc. it is important to set up poetry for local development.

## Using `poetry` on macOs

This section describes how to get `poetry` up and running on macOS. These instructions were developed and tested on macOS Monterey.

### Installation

#### Python

There is more than one way to get Python on your mac (one should probably not use the built-in python for development). This is one way to install Python from MacPorts:

```sh
sudo port install python312
sudo port select --set python python312
sudo port select --set python3 python312

sudo port install py312-pip
sudo port select --set pip pip312
sudo port select --set pip3 pip312
```

#### Poetry

Poetry recommends that it be installed as a standalone executable. This is because poetry has its own dependencies, installing it inside the same virtual environment your dependencies are running in will cause it to be involved in dependency resolution. poetry prefers to be installed out-of-the-way.

Poetry provides a command line based installation script (which itself requires python...)

```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.8.2
```

> see [installation instructions](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

> You may omit the `--version 1.8.2` to install the latest version; the version cited
> here should match the Dockerfile at the project root.

This will install poetry in `$HOME/.lock/bin/poetry`. The poetry binary will be added to your path in your zsh profile, and you may add it to the current terminal with the suggested command:

You can test it with

```shell
poetry --version
```

which should return something like:

```shell
Poetry version 1.8.2
```

### Usage

#### Installation of packages and activation

Once poetry is installed, using it is dead easy.

First, we need to install the project dependencies and create a virtual environment. To do this, from the project directory:

```shell
poetry install
```

Once packages are installed, you can activate the virtual environment, if you need to:

```shell
poetry shell
```

#### Using with PyCharm

PyCharm is a Python-oriented IDE from JetBrains. Other tools will probably work similarly, but this captures my workflow.

In order to have PyCharm recognize the installed packages, you will need to inform it that you are using poetry.

To do so:

- open the PyCharm preferences(PyCharm -> Preferences on macOS)
- Navigate to **Project: sample_service** > **Python Interpreter**
  ![PyCharm Preferences](pycharm-interpreter-none.png)
- Click the gear button at the right of the Python Interpreter input, which shows **<No Interpreter>**
- Select the **Add** menu item.
- From the dialog, select **Poetry Environment**, and then, if not already selected, **Existing Environment**. You should see the **Interpreter** field already populated
  ![PyCharm Preferences](pycharm-interpreter-poetry.png)
- Click the **OK** button
- After the dialog closes, the packages table will display "Loading...". After a few seconds, you should see a list of all packages you had earlier installed via "poetry install".
  ![PyCharm Preferences](pycharm-interpreter.png)
- That's it!

### Removing the virtual environment and packages

The poetry virtual environment is installed in the `.venv` directory within the project directory. You may leave this virtual environment in place while the project is active - it has no effect on any other virtual environment or global usage of Python.

However, when you are finished or if you simply want to remove the virtual environment for any other reason (e.g. debugging and you want a clean virtual environment):

```shell
rm -rf .venv
```

> Poetry has a built-in command for removing a virtual environment, but it currently does not seem to work with locally installed environments (poetry by default installs virtual environments in your user directory).
