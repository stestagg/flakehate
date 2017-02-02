from __future__ import with_statement
import setuptools

requires = [
    "flake8 > 3.0.0",
]

flake8_entry_point = "flake8.extension"

setuptools.setup(
    name="flakehate",
    license="MIT",
    version="0.1.0",
    description="Dojo for fun and profit",
    author="Me",
    packages=[
        "flakehate",
    ],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'X666 = flakehate.one:PluginOne',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)