ccsyspath 
=========

**ccsyspath helps you find the system include path of your c/c++ compilers system include path**

Supports gcc and clang c compilers.

|license| |build| |coverage|

Usage
-----

You can retrieve all of the system include paths for a specific compiler with
the `system_include_paths` function.

.. code:: python

    import ccsyspath

    paths = ccsyspath.system_include_paths('/path/to/clang')


Acknowledgements
----------------

This package is based on the approach demonstrated in a `stackoverflow answer`_
licensed under the `cc by-sa 3.0 with attribution required`_

Contributing
------------

If you experience problems with ccsyspath, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _stackoverflow answer: http://stackoverflow.com/a/11946295/2246
.. _log them on Github: https://github.com/AndrewWalker/ccsyspath/issues
.. _fork the code: https://github.com/AndrewWalker/ccsyspath
.. _submit a pull request: https://github.com/AndrewWalker/ccsyspath/pulls
.. _cc by-sa 3.0 with attribution required: https://creativecommons.org/licenses/by-sa/3.0/

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/andrewwalker/ccsyspath/master/LICENSE
   :alt: MIT License

.. |build| image:: https://travis-ci.org/AndrewWalker/ccsyspath.svg?branch=master
   :target: https://travis-ci.org/AndrewWalker/ccsyspath
   :alt: Continuous Integration

.. |coverage| image:: https://coveralls.io/repos/github/AndrewWalker/ccsyspath/badge.svg?branch=master
   :target: https://coveralls.io/github/AndrewWalker/ccsyspath?branch=master
   :alt: Coverage Testing Results

