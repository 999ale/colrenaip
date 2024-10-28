# setup.py
from setuptools import setup, find_packages

setup(
    name="colrenaip",
    version="0.1",
    packages=find_packages(),
    description="Libreria per colorare testo nel terminale",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/999ale/colrenaip",  # Sostituisci con l'URL del tuo repository GitHub
    author="Alessandro",
    author_email="alessandro.bressan@enaip.piemonte.it",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
