from setuptools import setup, find_packages

setup(
    name="meupia-testes",
    version="1.0.0",
    packages=find_packages(),
    description="Plugin oficial de testes e asserções para o compilador meuPiá",
    author="Henry Hamon",
    author_email="henryhamon@gmail.com",
    url="https://github.com/meuPia/testes.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)