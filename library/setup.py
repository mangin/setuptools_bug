from setuptools import setup, find_packages

setup(
    name='mangin_library',
    version='0.0.1',
    author='AleksandrMangin',
    author_email='mangin.alexander@yandex.ru',
    dependency_links=[
        'https://test.pypi.org/simple/mangin-library-of-library/'
    ],
    install_requires=[
          'mangin_library_of_library',
    ],
    license='MIT',

    url='https://ya.ru',
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    zip_safe=True,
    setup_requires=['setuptools_scm'],
)
