from setuptools import setup, find_packages
import os


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents


setup(
    name         = "ccsyspath",
    version      = "1.0.1",
    description  = "Find the system include paths for clang and gcc C/C++ compilers",
    long_description = read('README.rst'),
    author       = "Andrew Walker",
    author_email = "walker.ab@gmail.com",
    url          = "http://github.com/AndrewWalker/ccsyspath",
    license      = "MIT",
    packages     = find_packages(), 
    classifiers  = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],
    tests_require=['unittest2'],
    test_suite='unittest2.collector'
)

