from setuptools import setup

setup(
    name='ADS1299Monitor',
    version='1.0',
    author='Aryan Akbarpour',
    author_email='aryan.akr@yahoo.com',
    description='Monitoring software for ADS1299 chip',
    url="https://www.aryanakr.com/project/eegmonitor",
    license='MIT',
    long_description=open('README.rst', 'r').read(),
    keywords='ads1299 eeg bci',
    project_urls={'Author Website': 'https://www.aryanakr.com'},
    packages=['ads1299monitor'],
    install_requires=['PyQt5','PyQt5-sip','XlsxWriter','pyparsing','pyqtgraph'],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points={
        'console_scripts': ['ads1299monitor = ads1299monitor.__main__:main']
    }
)