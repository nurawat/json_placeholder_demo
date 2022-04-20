from setuptools import setup

setup(
    name='userstat',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
        'certifi',
        'charset-normalizer',
        'click',
        'idna',
        'requests',
        'urllib3',
        'prettytable'
    ],
    entry_points='''
        [console_scripts]
        userstat=main:callAPI
    ''',
)
