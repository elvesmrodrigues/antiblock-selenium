import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antiblock-selenium",
    version="0.0.3",
    author="Elves M. Rodrigues",
    author_email="elvesmateusrodrigues@gmail.com",
    description="Selenium Firefox e Chrome webdrivers com alguns mecanismos antibloqueios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvesrodrigues/antiblock-selenium",
    packages=setuptools.find_packages(),
    install_requires=[
        'pysocks==1.7.1',
        'requests==2.23.0',
        'selenium==3.141.0',
        'stem==1.8.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.0',
)
