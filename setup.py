from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name="pactus-sdk",
    version="2.0.0",
    author="Pactus Development Team",
    python_requires=">=3.11",
    author_email="info@pactus.org",
    description="Pactus Development Kit",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/pactus-project/python-sdk",
    install_requires=["ripemd-hash", "grpcio", "grpcio-tools", "cryptography"],
    keywords=["pactus", "blockchain", "web3", "dapp", "bls", "bech32"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
