from setuptools import setup, find_packages

setup(
    name='file_organizer',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'file-organizer = file_organizer.main:main',
        ],
    },
)