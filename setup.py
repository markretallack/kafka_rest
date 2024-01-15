import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlp-kafka-rest-api",
    version="1.0.1",
    author="shashi1991, mark.retallack@yunextraffic.com",
    author_email="mark.retallack@yunextraffic.com",
    description="fork of nlp-kafka-rest-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    url="https://pypi.org/project/nlp-kafka-rest-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)