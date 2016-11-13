INCOR
=====

INstant COde Runner runs the programs present in the mentioned directory instantaneously as and when changes are saved.

| Version | Quality | Docs |
|------|--------|-------|
|[![PyPI version](https://badge.fury.io/py/incor.svg)](https://badge.fury.io/py/incor) | [![Code Health](https://landscape.io/github/lakshmanaram/Incor/master/landscape.svg?style=flat)](https://landscape.io/github/lakshmanaram/Incor/master) | [![Documentation Status](https://readthedocs.org/projects/incor/badge/?version=latest)](http://incor.readthedocs.io/en/latest/?badge=latest)

Requirements
------------

-   python&gt;=2.7
-   watchdog&gt;=0.8.2
-   psutil&gt;=4.3.0

Getting Started
---------------
Install it using pip

```sourceCode
sudo pip install incor
```

**Or**

Clone this repository to get started.

``` sourceCode
git clone https://github.com/lakshmanaram/Incor.git
```

And install it.

``` sourceCode
python setup.py install
```

You can also install it for development.

``` sourceCode
python setup.py develop
```

How to Use
----------

Navigate to the folder where you want the files to be compiled and executed instantly and type this in the terminal

``` sourceCode
incor
```

Or else you can run it directly with the path of the directory.

``` sourceCode
incor /path/to/the/directory
```

General template for running incor.

``` sourceCode
incor /optional/path/to/the/directory [<option> <value> ...]
```

Using Templates
---------------

You can also add some template files in the directory where incor runs. The template files should be of the form 'template.(some_extension)' for example 'template.c' or 'template.py'.
Whenever a new empty file is created inside the working directory with a particular extension, Incor searches for a template file with the same extension and writes the template into the newly created file.

**Example:**

All the empty files created in the present directory with .cpp extension will have the contents of a.cpp, .c extension will have the contents of a.c and .py extension will have the contents of a.py

``` sourceCode
    incor -t a
```
All the empty files created in the present directory with extension in [cpp,c,py] will have the contents of template.extension if available anywhere in the path/to/the/directory

``` sourceCode
    incor path/to/the/directory -t
```
![template example](https://github.com/lakshmanaram/Incor/blob/master/examples/template.gif)

Using Input files
------------------

You can also add some input files in the directory where incor runs. The default input file is 'input.txt'.
Whenever a program is executed and run, Incor provides the contents of the specified input file as input to the program.

**Example:**

All the successfully compiled and executed programs will use input.txt present in path/to/the/directory or in any of it's sub-directories as input

``` sourceCode
incor path/to/the/directory -i
```
All the successfully compiled and executed programs will use a.txt present in the current working directory or in any of it's sub-directories as input

``` sourceCode
incor -i a.txt
```
Demo
-----

[Youtube link](https://youtu.be/KhJZ1N7fS6o)

Configuring INCOR
-----------------

incor can be configured for a run using these options -

> -i To specify the input file name for the to be compiled program(with extension).
>
> -t To specify the name of template file(without extension).
>
> -c To specify the C compiler to be used.
>
> -cpp To specify the C++ compiler to be used.
>
> -py To specify the python interpreter to be used.

![compiler_option](https://github.com/lakshmanaram/Incor/blob/master/examples/setting_compiler.gif)

Contributors
------------

  [Srivatsan R](https://github.com/srivatsan-ramesh)

  [Adarsh B](https://github.com/badarsh2)

If you have an idea for a new feature that could be added, Go ahead! I will be happy to see a pull request from you! :smile:
