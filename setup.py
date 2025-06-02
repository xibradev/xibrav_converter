from setuptools import setup, find_packages

setup(
    name="xibrav_converter",
    version="1.0.0",
    description="Simple wrapper for Xibrav video conversion API (mp3/mp4)",
    author="ibrahim",
    author_email="ibra@gmail.com",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
