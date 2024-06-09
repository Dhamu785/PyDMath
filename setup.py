from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.2'
DESCRIPTION = 'Solving the maths problems'
LONG_DESCRIPTION = 'A package that allows to solve fundamental math problems.'

# Setting up
setup(
    name="PyDMath",
    version=VERSION,
    author="Dhamodharan",
    author_email="dhamodharan1888@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['math', 'numpy'],
    keywords=['python', 'math', 'problems', 'mathematics', 'scientific calculations'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)