from setuptools import setup, find_packages

setup(
    name="SmartTestPy",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pytest-cov",
        "Faker",
        "freezegun",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "smarttestpy=smarttestpy.core.test_runner:run_tests",
        ],
    },
    author="Roberto Lima",
    author_email="robertolima.izphera@gmail.com",
    description="Pacote para testes automatizados em Python, com integração ao pytest, geração de dados fake, mocks avançados e manipulação de tempo.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robertolima-dev/SmartTestPy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
