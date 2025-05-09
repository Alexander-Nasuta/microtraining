# Micropackage

- [microtraining on **Gitlab**](https://git-ce.rwth-aachen.de/alexander.nasuta/jsp-instance-utils)
- [microtraining on **Github**](https://github.com/Alexander-Nasuta/jsp-instance-utils/)
- [microtraining **PyPi**](https://pypi.org/project/microtraining/)
- [microtraining **Documentation**](https://jsp-instance-utils.readthedocs.io/en/latest/)

# About The Project
A minimal example project for publishing Python Software Packages in 2025.

## Development Setup

If you want to check out the code and implement new features or fix bugs, you can set up the project as follows:

### Clone the Repository

clone the repository in your favorite code editor (for example PyCharm, VSCode, Neovim, etc.)

using https:
```shell
git clone https://github.com/Alexander-Nasuta/microtraining.git
```
or by using the GitHub CLI:
```shell
gh repo clone Alexander-Nasuta/microtraining
```

if you are using PyCharm, I recommend doing the following additional steps:

- mark the `src` folder as source root (by right-clicking on the folder and selecting `Mark Directory as` -> `Sources Root`)
- mark the `tests` folder as test root (by right-clicking on the folder and selecting `Mark Directory as` -> `Test Sources Root`)
- mark the `resources` folder as resources root (by right-clicking on the folder and selecting `Mark Directory as` -> `Resources Root`)


### Create a Virtual Environment (optional)

Most Developers use a virtual environment to manage the dependencies of their projects.
I personally use `conda` for this purpose.

When using `conda`, you can create a new environment with the name 'microtraining' following command:

```shell
conda create -n microtraining python=3.11
```

Feel free to use any other name for the environment or a more recent version of python.
Activate the environment with the following command:

```shell
conda activate microtraining
```

Replace `microtraining` with the name of your environment, if you used a different name.

You can also use `venv` or `virtualenv` to create a virtual environment. In that case please refer to the respective documentation.

### Install the Dependencies

To install the dependencies for development purposes, run the following command:

```shell
pip install -r requirements_dev.txt
pip install tox
```

The testing package `tox` is not included in the `requirements_dev.txt` file, because it sometimes causes issues when
using github actions.
Github Actions uses an own tox environment (namely 'tox-gh-actions'), which can cause conflicts with the tox environment on your local machine.

Reference: [Automated Testing in Python with pytest, tox, and GitHub Actions](https://www.youtube.com/watch?v=DhUpxWjOhME).

### Install the Project in Editable Mode

To install the project in editable mode, run the following command:

```shell
pip install -e .
```

This will install the project in editable mode, so you can make changes to the code and test them immediately.

### Run the Tests

This project uses `pytest` for testing. To run the tests, run the following command:

```shell
pytest
```

For testing with `tox` run the following command:

```shell
tox
```

Tox will run the tests in a separate environment and will also check if the requirements are installed correctly.

### Building and Publishing the Project to PyPi

In order to publish the project to PyPi, the project needs to be built and then uploaded to PyPi.

To build the project, run the following command:

```shell
python -m build
```

It is considered good practice use the tool `twine` for checking the build and uploading the project to PyPi.
By default the build command creates a `dist` folder with the built project files.
To check all the files in the `dist` folder, run the following command:

```shell
twine check dist/**
```

If the check is successful, you can upload the project to PyPi with the following command:

```shell
twine upload dist/**
```

### Documentation
This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).



## Contact

If you have any questions or feedback, feel free to contact me via [email](mailto:alexander.nasuta@wzl-iqs.rwth-aachen.de) or open an issue on repository.


# License

Distributed under the MIT License. See `LICENSE.txt` for more information.


