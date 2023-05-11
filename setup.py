from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in delivery/__init__.py
from delivery import __version__ as version

setup(
	name="delivery",
	version=version,
	description="Shows delivery trips to clients and drivers",
	author="Nigel Jena",
	author_email="nigel@stokdirect.africa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
