from setuptools import setup, find_packages

setup(
    name='xcURL',
    packages=find_packages(),
    install_requires=['click','pywebcopy'],
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'xcurl = xcurl:url',    
        ]
    },
    include_package_data=True,
)