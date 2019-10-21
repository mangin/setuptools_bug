from setuptools import setup, find_packages


setup(
    name='mangin_project',
    url='http://ya.ru',
    maintainer='Aleksandr Mangin',
    maintainer_email='mangin.alexander@yandex.ru',
    license='MIT',
    zip_safe=False,
    packages=find_packages('src'),
    install_requires=[
        'mangin-library',
        'mangin-library-of-library',
    ],
    dependency_links=[
        'https://test.pypi.org/simple/mangin-library-of-library/',
        'https://test.pypi.org/simple/mangin-library/',
    ],
)
