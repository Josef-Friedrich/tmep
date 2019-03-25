import versioneer
import os
from setuptools import setup


def read(fname):
    return open(
        os.path.join(os.path.dirname(__file__), fname),
        encoding='utf8'
    ).read()


setup(
    name='tmep',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    description=('Template and Macros Expansion for Path names.'),
    license='MIT',
    packages=['tmep'],
    url='https://github.com/Josef-Friedrich/tmep',
    install_requires=[
        'unidecode',
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
