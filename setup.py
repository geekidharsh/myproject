from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    description="A dummy package to try out distribution of a Python package. Built by Harsh",
    author="Harshvardhan Pandey",
    author_email="your@email.com",
    url="https://github.com/yourusername/mypackage",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
