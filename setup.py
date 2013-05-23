import os
from os.path import join, dirname
from distutils.core import setup


def recursiveFileGenerator(rootDir):
    """Recursively yield every file within the specified directory."""
    for folder, subs, files in os.walk(rootDir):
        for fileName in files:
            dummy,dummy,result = os.path.join(folder,fileName).partition("/")
            yield result


def makeRecursiveFileList(rootDir):
    """Return a list of every file within the specified directory."""
    return list(recursiveFileGenerator(rootDir))


try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-angularui',
    version='0.3',
    url="---",
    description='Angularui packaged in a handy django app to speed up new applications and reduce duplication.',
    long_description=long_description,
    author='---',
    author_email='---',
    keywords='django angular angularui staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['angularui'],
    package_data={'angularui':makeRecursiveFileList("angularui")},
)
