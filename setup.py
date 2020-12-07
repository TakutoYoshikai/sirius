from setuptools import setup, find_packages

setup(
    name = 'sirius',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/sirius.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "sirius is an encoder/decoder of data",
    install_requires = ['setuptools'],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "sirius = sirius.sirius:main",
        ]
    }
)
