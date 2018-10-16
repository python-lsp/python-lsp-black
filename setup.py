from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyls-black",
    version="0.3.0",
    description="Black plugin for the Python Language Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rupert/pyls-black",
    author="Rupert Bedford",
    author_email="rupert@rupertb.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=["python-language-server", "black>=18.9b0", "toml"],
    extras_require={"dev": ["isort", "flake8", "pytest", "mypy", "pytest"]},
    entry_points={"pyls": ["pyls_black = pyls_black.plugin"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
