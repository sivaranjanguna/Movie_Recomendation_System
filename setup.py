from setuptools import setup

with open("README.md", "r" , encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'sivaranjanguna'
REPO_NAME = 'Movie_Recomendation_System'
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']
VERSION = '0.0.1'

setup(
    name=REPO_NAME,
    author=AUTHOR_NAME,
    version=VERSION,
    author_email="sivaranjang@gmail.com",
    description="A simple movie recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir = {"" : "src"},
    python_requires=">=3.9",
    install_requires=LIST_OF_REQUIREMENTS,
)