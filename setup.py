
# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata_richard_olson",
    version="1.00.1",
    author="R Olson",
    author_email="rchiro@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/richardOlson/lamdata-richard-olson",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)