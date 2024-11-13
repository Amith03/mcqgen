from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='amith maiya',
    author_email='amithmaiya3@gmail.com',
    install_requires=["langchain_huggingface","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)