from setuptools import setup

setup(
    name='doonfraction',
    version='1.0',
    packages=['doonfraction'],
    entry_points={
        'console_scripts': [
            'doonfraction = doonfraction.__main__:main'
        ]
    },
    package_data={'doonfraction': ['tests/*.py']},
    author='Somil',
    author_email='iamsomilsharma@email.com',
    description='A Python class for working with fractions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)

