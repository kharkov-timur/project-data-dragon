from setuptools import setup, find_packages

setup(
    name="PersonalHelper",
    version="0.1.0",
    author="Timur Kharkov",
    author_email="kharkov.timur@gmail.com",
    description="Personal contacts and notes helper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/project-data-dragon",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    entry_points={
        "console_scripts": [
            "personal-helper=main:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="personal helper notes contacts",
)
