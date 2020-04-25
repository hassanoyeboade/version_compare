## Version Compare
Compares two version strings and returns whether one is greater than, equal to, or less than the other.

#### Setting up
- Setup a virtual environment 
	- Run `python3 -m venv .venv` to create the environment
	- Run `source .venv/bin/activate` to activate created environment
- Run `pip3 install -i https://test.pypi.org/simple/ version-compare` to install the package


#### Example Usage
- Run `python3` to set up interactive mode
- Import `compare_versions` and call with arguments `compare_versions(version_1, version_2)`
```
>>> from version_compare import compare_versions
>>> compare_versions('1.2', '1.3')
'"1.2" is less than "1.3"'
>>> compare_versions('1.2.0', '1.2')
'"1.2.0" is equal to "1.2"'
>>> compare_versions('3.0', '2.2')
'"3.0" is greater than "2.2"'
>>> compare_versions('3.0.3', '2.2')
'"3.0.3" is greater than "2.2"'
>>> compare_versions('3.0.3', '3.0.3')
'"3.0.3" is equal to "3.0.3"'
```
