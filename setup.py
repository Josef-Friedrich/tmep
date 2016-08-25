from setuptools import setup

setup(
    name = 'path-macrotemplate',
    version = '0.0.1',
    author = 'Josef Friedrich',
    author_email = 'josef@friedrich.rocks',
    description = ('Template and macros expansion for path names.'),
    license = 'MIT',
    packages = ['path-macrotemplate'],
    url = 'https://github.com/Josef-Friedrich/path-macrotemplate',
    install_requires = [
        'unidecode', 'six',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
