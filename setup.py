#!/usr/bin/env python
from setuptools import setup

setup(
    name='python-binance-aio',
    version='0.0.3',
    packages=['aiobinance'],
    description='Asynchronous Binance REST API python implementation',
    url='https://github.com/BlockHub/python-binance-aio',
    author='Karel Kubat',
    license='MIT',
    author_email='Karel@blockhub.nl',
    install_requires=['aiohttp', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity', 'dateparser', 'urllib3', 'chardet', 'certifi', 'cryptography', ],
    keywords='binance exchange rest api bitcoin ethereum btc eth neo aiohttp asyncio',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
