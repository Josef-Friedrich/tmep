from setuptools import setup

setup(
    name = 'tmep',
    version = '0.0.2',
    author = 'Josef Friedrich',
    author_email = 'josef@friedrich.rocks',
    description = ('Template and Macros Expansion for Path names.'),
    license = 'MIT',
    packages = ['tmep'],
    url = 'https://github.com/Josef-Friedrich/tmep',
    install_requires = [
        'unidecode', 'six',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
