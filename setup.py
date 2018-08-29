from distutils.core import setup

setup(
    name='epz',
    version='2.0',
    packages=['epz','epz.core','epz.epsilonpi','epz.tools'],
    url='https://github.com/massimovassalli/epz',
    download_url='https://github.com/massimovassalli/epz/releases/tag/v2.0',
    keywords=['zmq','pyzmq','zeromq'],
    license='',
    author='Massimo Vassalli',
    author_email='massimo.vassalli@nanobioscience.eu',
    description='', requires=['zmq']
)
