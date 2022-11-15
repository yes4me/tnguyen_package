from setuptools import setup

setup(
    name='tnguyen_package',
    version='0.0.1',
    description='my private pip package',
    url='git@github.com:yes4me/tnguyen_package.git',
    author='Thomas Nguyen',
    author_email='yes4me@hotmail.com',
    license='unlicense',
    packages=['tnguyen_package'],
    zip_safe=False,
)


def my_print(name):
    print("hello world", name)
