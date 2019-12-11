from setuptools import setup, find_packages
setup(
    name='redisgraph',
    version='2.1',

    description='RedisGraph Python Client (b33j0r fork)',
    url='https://github.com/b33j0r/redisgraph-py',
    packages=find_packages(),
    install_requires=['redis', 'PTable'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database'
    ]
)
