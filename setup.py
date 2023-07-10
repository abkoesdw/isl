from setuptools import find_packages, setup

__version__ = "0.0.0"
PACKAGE_NAME = "ISL"
MAINTAINER = "abkoesdw"
MAINTAINER_EMAIL = "ariefbarkah@gmail.com"

DESCRIPTION = "This is my repo to reproduce examples in ISL"

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=PACKAGE_NAME,
    version=__version__,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas==2.0.3",
        "ipython==8.14.0",
        "ipykernel==6.24.0",
    ],
    extras_require={
        "dev": [
            "black==23.3.0",
            "flake8==6.0.0",
            "isort==5.12.0",
        ]
    },
    license="",
    python_requires=">=3.11",
)
