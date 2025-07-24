import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'

REPO_NAME='Text-summarizer'
AUTOR_NAME="bsshewale"
SRC_REPO='textSummarizer'
AUTHOR_EMAIL='bsshewale1630@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for cnn app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/bsshewale/Text-summarizer",
    project_urls={
    "Bug Tracker": "https://github.com/bsshewale/Text-summarizer/issues"},
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)