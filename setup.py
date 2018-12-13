from setuptools import setup, find_packages

setup(
    name='neuroner',

    version='1.0.0',

    packages=find_packages(),

    package_data={
        'neuroner': [
            'parameters.ini',
        ]
    },

    install_requires=[
        'tensorflow==1.6.0rc1',
        'networkx==2.1',
        'matplotlib==2.2.0rc1',
        'scikit-learn==0.19.1',
        'scipy==1.0.0',
        'pycorenlp==0.3.0',
        'spacy==2.0.9',
    ],


)
