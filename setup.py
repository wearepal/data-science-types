"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="data-science-types",
    version="0.2.7",
    author="PAL",
    description="Type stubs for Python machine learning libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "matplotlib-stubs": [
            "__init__.pyi",
            "artist.pyi",
            "axes.pyi",
            "image.pyi",
            "legend.pyi",
            "pyplot.pyi",
            "style.pyi",
            "text.pyi",
        ],
        "numpy-stubs": ["__init__.pyi", "linalg.pyi", "ma.pyi", "random.pyi", "testing.pyi"],
        "pandas-stubs": ["__init__.pyi", "testing.pyi"],
        "pandas-stubs.core": [
            "__init__.pyi",
            "frame.pyi",
            "indexing.pyi",
            "series.pyi",
            "strings.pyi",
        ],
        "pandas-stubs.core.groupby": ["__init__.pyi", "generic.pyi"],
        "pandas-stubs.core.indexes": ["__init__.pyi", "base.pyi", "frozen.pyi", "multi.pyi"],
    },
    packages=[
        "matplotlib-stubs",
        "numpy-stubs",
        "pandas-stubs",
        "pandas-stubs.core",
        "pandas-stubs.core.groupby",
        "pandas-stubs.core.indexes",
    ],
    python_requires=">=3.6",
    # use `pip install data-science-types[dev]` to install development packages
    extras_require={"dev": ["black", "mypy"]},
    classifiers=[  # classifiers can be found here: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Typing :: Typed",
    ],
    zip_safe=False,
)
