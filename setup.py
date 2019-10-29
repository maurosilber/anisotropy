from setuptools import setup

setup(
    name='anisotropy',
    version='0.0.1',
    packages=['anisotropy'],
    url='https://github.com/maurosilber/anisotropy',
    license='MIT',
    author='Mauro Silberberg',
    author_email='maurosilber@gmail.com',
    description='Fluorescence anisotropy microscopy analysis.',
    install_requires=['numpy', 'pywavelets']
)
