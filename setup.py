from setuptools import setup

setup(
    name="matching",
    version="0.1.0",
    description="Approximate matching of sift features",
    long_description="Given a new SIFT feature find an approximate nearest neighbor from an atlas of sift features",
    author="Shaowei Lin",
    author_email="shaowei@awecom.com",
    packages=["matching"],
    install_requires=[
        "numpy",
        "matplotlib",
        "opencv-python"
    ]
)
