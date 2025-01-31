from setuptools import setup, find_packages

setup(
    name="bytea",
    version="1.0.0",
    author="Athul Raj.K",
    author_email="your-email@example.com",
    description="A modern, lightweight programming language.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/bytea",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "bytea=bytea.bytea:main",
        ],
    },
    install_requires=[],
)