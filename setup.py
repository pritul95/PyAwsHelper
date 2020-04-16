import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyAwsHelper",
    version="0.0.1",
    author="Ritul Patel",
    author_email="author@example.com",
    description="Python AWS Helper Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pritul95/PyAwsHelper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
