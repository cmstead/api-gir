import pathlib
from setuptools import setup, find_packages

setup(
    name='api-gir',
    version='0.1.0',
    packages=["api_gir"],
    author="Chris Stead",
    author_email="cmstead@gmail.com",
    url="https://github.com/cmstead/api-gir#readme",
    platforms=['any'],
    description="GIR! Run these lambdas for me!",
    license='MIT',
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "api-gir = api_gir.__main__:main"
        ]
    }
)