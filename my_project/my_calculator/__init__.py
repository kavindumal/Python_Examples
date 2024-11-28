"""
This __init__.py file is used to mark a directory as a Python package. 
When a directory contains an __init__.py file, it can be imported as a module in Python. 
This file can also be used to execute initialization code for the package or to set the __all__ variable,
which defines the public interface of the package.

Common uses of __init__.py include:
- Initializing package-level variables or data structures.
- Importing specific classes, functions, or submodules to make them available at the package level.
- Setting up package-level logging or configuration.
- Defining the __all__ variable to control what is imported when a user imports the package using the 'from package import *' syntax.

Example:
    # Importing a submodule

    # Importing a specific class from a submodule

    # Defining the public interface of the package
    __all__ = ['MyClass', 'another_function']
"""