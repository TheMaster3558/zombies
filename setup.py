import re
import setuptools


with open("zombies/__init__.py", "r") as file:
    text = file.read()

    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', text, re.MULTILINE
    ).group(1)
    description = re.search(r'"""([\w\s.]+)"""', text).group(1)


with open("README.rst", "r") as file:
    readme = file.read()


packages = ["zombies"]


extra_requires = {"dev": ["black"]}


setuptools.setup(
    name="zombies",
    author="The Master",
    license="MIT",
    description=description,
    long_description=readme,
    long_description_content_type="text/x-rst",
    version=version,
    packages=packages,
    include_package_data=True,
    python_requires=">=3.6.0",
    extra_requires=extra_requires,
    entry_points={
        "console_scripts": [
            "zombies = zombies.cli:main",
        ]
    },
)
