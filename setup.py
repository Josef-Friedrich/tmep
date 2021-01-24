import os

from setuptools import setup, find_packages
import versioneer


def read(file_name):
    """
    Read the contents of a text file and return its content.

    :param str file_name: The name of the file to read.

    :return: The content of the text file.
    :rtype: str
    """
    return open(
        os.path.join(os.path.dirname(__file__), file_name),
        encoding='utf-8'
    ).read()


setup(
    name='tmep',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    description=('Template and Macros Expansion for Path names.'),
    license='MIT',
    packages=find_packages(),
    url='https://github.com/Josef-Friedrich/tmep',
    install_requires=[
        'unidecode',
        'six>=1.9',
    ],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    scripts=['bin/tmep-doc'],
    zip_safe=False,
    python_requires='>=3.6',
)
