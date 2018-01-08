from setuptools import setup

setup(
    name='trading-platform',
    version='1.0',
    description='Trading platform for low frequency trading',
    author='Khoa Le',
    author_email='khoatatle@gmail.com',
    packages=['trading-platform'],
    install_requires=['numpy', 'pandas', 'quandl']
)
