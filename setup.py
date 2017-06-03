from setuptools import setup, find_packages
setup(
    name='weaver',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        weaver=weaver.manage:cli
    ''',
)
