from setuptools import setup, find_packages

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AutoMorphoTrack",
    version="1.0.0",
    author="Armin Bayati, Ph.D.",
    author_email="a.bayati.brain@gmail.com",
    description="Automated pipeline for mitochondrial and lysosomal detection, tracking, morphology, and colocalization analysis in microscopy images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arminbayati/AutoMorphoTrack",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.23.0",
        "pandas>=1.5.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "opencv-python>=4.6.0",
        "scikit-image>=0.19.0",
        "scipy>=1.9.0",
        "tifffile>=2022.8.12"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    include_package_data=True,
    license="MIT",
    project_urls={
        "Documentation": "https://github.com/arminbayati/AutoMorphoTrack",
        "Source": "https://github.com/arminbayati/AutoMorphoTrack",
        "Tracker": "https://github.com/arminbayati/AutoMorphoTrack/issues",
    },
)
