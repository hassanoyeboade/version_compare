import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="version-compare",
    version="0.0.3",
    author="Hassan Oyeboade",
    author_email="oyeboadehassan@gmail.com",
    description="A package to compare two version strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hassanoloye/hassan_oyeboade_test/tree/master/version_compare",
    packages=setuptools.find_packages(exclude=("tests", ".venv", )),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
