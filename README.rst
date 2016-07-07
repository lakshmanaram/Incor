INCOR
=====

INstant COde Runner
runs the programs present in the mentioned directory instantaneously as and when changes are saved. 

Requirements
------------

* python>=2.7
* watchdog>=0.8.2
* psutil>=4.3.0

Getting Started
---------------

Clone this repository to get started.

.. code-block:: bash

    git clone https://github.com/lakshmanaram/Program-runner.git

And install it.

.. code-block:: bash

    python setup.py install
    
You can also install it for development.

.. code-block:: bash

    python setup.py develop

How to Use
----------

Nagigate to the folder where you want the files to be compiled and run instantly and type this in the terminal

.. code-block:: bash

    incor

Or else you can run it directly with the path of the directory.

.. code-block:: bash

    incor /path/to/the/directory

General template for running incor.

.. code-block:: bash

    incor /optional/path/to/the/directory [<option> <value> ...]

Using Templates
---------------

You can also add some template files in the directory where incor runs. The template files should be of the form 'template.(some_extension)' for example 'template.c' or 'template.py'. 
Whenever a new empty file is created inside the working directory with a particular extension, Incor searches for a template file with the same extension and writes the template into the newly created file.

Configuring INCOR
-----------------

incor can be configured for a run using these options -

    -i    To specify the input file for the to be compiled program.
    -t    To specify the name of template file(without extension).
    -c    To specify the C compiler to be used.
    -cpp  To specify the C++ compiler to be used.
    -py   To specify the python interpreter to be used.
    

Contributors
------------
`Srivatsan R <https://github.com/srivatsan-ramesh>`_

Feel free to make a Pull Request
