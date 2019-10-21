from setuptools import setup, find_packages


setup(
    name='mangin_library_of_library',
    version='0.0.1',
    description='library of library',
    url='https://ya.ru',
    author='Mangin Aleksandr',
    author_email='mangin.alexander@yandex.ru',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=True,
    setup_requires=['setuptools_scm'],
)
