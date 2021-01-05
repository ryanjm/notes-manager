# When changing this file, be sure to rerun:
# `$ pip install --editable .`

from setuptools import setup
setup(
    name='notes',
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        notes=notes:cli
    '''
)