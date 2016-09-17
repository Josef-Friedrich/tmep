import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='tmep',
    version='0.0.3',
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    description=('Template and Macros Expansion for Path names.'),
    license='MIT',
    packages=['tmep'],
    url='https://github.com/Josef-Friedrich/tmep',
    install_requires=[
        'unidecode',
        'six',
    ],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
    ],
    zip_safe=False, )
