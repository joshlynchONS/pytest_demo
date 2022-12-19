# `Making a package`

Why do you need to turn your code into a package?

You don't. However, using your well crafted, modular python functions in other files becomes much easier. Have you ever tried using a function from a different directory. Manoeuvering directories in a python file is often messy and complicated. It is also rarely transferable to other users, making your code harder for others to use. Turning your code into an importable python module cures these issues.

In this example, turning the code into a package allows us to keep the test files in a seperate directory.

## Folder Structure
This repository follows a simple folder structure for clarity, but the govcookiecutter package provides a great starting folder structure to start your package. If you chose to create your own structure, your folder structure should follow a similar style to the structure below:
```
repo
|-- src
|-- |-- __init__.py
|   |-- package
|   |   |-- __init__.py
|   |   |-- module_file.py
|-- tests
|   |-- __init__.py
|   |-- test_func1.py
|   |-- test_func2.py
|-- pyproject.toml
|-- requirements.txt
|-- setup.cfg
|-- setup.py
|-- README.md
```
The main points are:

* The package is contained in a seperate file to the pytests.

* The setup files are in the main directory of the repository.

* Both the package and tests files contain an `__init__.py` file.

It is also a great idea to host the folder structure using git. This allows other members of your team/comunity to contribute to your project.

## Initial Files
As mentioned above, your package and tests files should contain `__init__.py` files. This helps pytest locate the folders, essential for running the pytests.

In the package file you should create your first python script containing your modularised functions.

In the tests file, create your first test file. It's good practice to have a seperate test file for each function you test. The file name must start with `test_` or finish with `_test` for pytest to recognise it. Its also good practice for the rest of the name to be the function you're testing. For example, if you're testing a function called calc_area, the test file should be `test_calc_area.py` or `calc_area_test.py`.

## Setup Files
For the package to be installable, you must have some setup files. There are a few different methods and variations of setup files, this example uses:

* setup.py

* setup.cfg

* requirements.txt

* pyproject.toml

One important thing is the package name in the `setup.cfg` (or `setup.py` if you don't use a `.cfg` file) is the same name as your package. This is essential because this is the name the python installer will use.

You might also question the difference between the setup and the requirements files. The requirements should contain an exact version for each dependency, and the setup should be as general as possible with a wide range of versions for each dependency.

## Install Package
Finally, it is time to install your package. To do this, type `pip install -e .` in the command promt, in your main repository directory. This should install all your package dependencies and finally import an editable version of your package.

Your package being editable is beneficial, because if you make any changes or updates to the package you won't have to reinstall your package everytime.

To check that your package has been installed you can do pip list in the command window to check that your package is listed. Also, if you go to your testing files, you'll see you can now import your package.
