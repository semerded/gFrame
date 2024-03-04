from setuptools import find_packages, setup

setup(
    name='gFrame',
    packages=find_packages(),
    version='1.0.0',
    description='gFrame is built on the widely used pygame library. It aims for a more user friendly programming process by including easier setup and a lot of widgets',
    author='Sem Van Broekhoven',
    install_requires=['pygame'],
)