import sys
import setuptools
from setuptools import find_packages, setup
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from os.path import join, dirname, realpath

str_version = '0.0.1'



def configuration(parent_package='', top_path=''):
    # this will automatically build the scattering extensions, using the
    # setup.py files located in their subdirectories
    config = Configuration(None, parent_package, top_path)

    pkglist = setuptools.find_packages()
    for i in pkglist:
        config.add_subpackage(i)
    # config.add_data_files(join('mtutils', 'assets', '*.json'))
    # config.add_data_files(join('mtutils', 'assets', '*.jpg'))

    return config


if __name__ == '__main__':
    pass
    setup(
        configuration=configuration,
        name='mario',
        version=str_version,
        description='Commonly used function library by VVD',
        url='https://github.com/zywvvd/mario',
        author='zywvvd',
        author_email='zywvvd@mail.ustc.edu.cn',
        license='MIT',
        packages=['mario'],
        zip_safe=False,
        install_requires= [],
        python_requires='>=3')
