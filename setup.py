import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.0.1'
DESCRIPTION = 'Solving the aptitude problems'
LONG_DESCRIPTION = 'A package that allows to solve apitude math problems.'

# Setting up
setup(
    name="numbersD",
    version=VERSION,
    author="Dhamodharan",
    author_email="dhamodharan1888@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
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