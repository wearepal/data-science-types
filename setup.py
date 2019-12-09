"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="data-science-types",
    version="0.1.6",
    author="PAL",
    description="Type stubs for Python machine learning libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "matplotlib-stubs": [
            "__init__.pyi",
            "artist.pyi",
            "image.pyi",
            "legend.pyi",
            "pyplot.pyi",
            "style.pyi",
            "text.pyi",
        ],
        "numpy-stubs": ["__init__.pyi", "_core.pyi", "ma.pyi", "random.pyi", "testing.pyi"],
        "pandas-stubs": ["__init__.pyi", "_core.pyi", "testing.pyi"],
        "pandas-stubs.core": [
            "__init__.pyi",
            "frame.pyi",
            "indexes.pyi",
            "indexing.pyi",
            "series.pyi",
        ],
        "pandas-stubs.core.groupby": ["__init__.pyi", "generic.pyi"],
        "tensorflow-stubs": [
            "__init__.pyi",
            "_core.pyi",
            "data.pyi",
            "metrics.pyi",
            "optimizers.pyi",
            "random.pyi",
            "train.pyi",
        ],
        "tensorflow-stubs.keras": ["__init__.pyi", "_core.pyi", "layers.pyi"],
        "tensorflow-stubs.summary": ["__init__.pyi", "experimental.pyi"],
        "tensorflow_probability-stubs": ["__init__.pyi", "bijectors.pyi", "distributions.pyi"],
    },
    packages=[
        "matplotlib-stubs",
        "numpy-stubs",
        "pandas-stubs",
        "pandas-stubs.core",
        "tensorflow-stubs",
        "tensorflow-stubs.keras",
        "tensorflow-stubs.summary",
        "tensorflow_probability-stubs",
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
