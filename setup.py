from setuptools import setup, find_packages

setup(
    name='django_angularui',
    version='1.1.5',
    packages=['django_angularui'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    setup_requires=('ci_scripts'),
    install_requires=('ci_scripts'),
)
