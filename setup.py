from setuptools import setup, find_packages

setup(
    name='zwyFramework',
    version='1.0.0',
    packages=find_packages(),
    author='Zwylair',
    author_email='zwylair@gmail.com',
    description="Zwy's tools for more comfortable codding",
    url='https://github.com/Zwylair/zwyFramework',
    install_requires=[
        'requests~=2.31.0',
        'fake_useragent~=1.4.0',
        'flask==3.0.0',
    ]
)
