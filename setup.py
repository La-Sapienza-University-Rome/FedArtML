# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="FedArtML",
    version="0.1.33",
    description="Federated learning for Artificial Intelligence and Machine Learning library ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Daniel Mauricio Jimenez Gutierrez, Aris Anagnostopoulos, Ioannis Chatzigiannakis, Andrea Vitaletti",
    author_email="jimenezgutierrez@diag.uniroma1.it",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["fedartml"],
    include_package_data=True,
    install_requires=["numpy", "ipywidgets", "matplotlib", "pandas", "scipy", "keras", "tensorflow"]
)
