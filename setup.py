from setuptools import setup

setup(
    name='python-validity',
    version='0.5',
    packages=['proto9x'],
    scripts=['validity-sensors-tools'],
    url='https://github.com/uunicorn/python-validity',
    license='',  # TODO (upstream): pick license
    author='uunicorn',  # TODO (upstream): update contact info if desired
    author_email='',
    description='Validity fingerprint sensor prototype',
    install_requires=(
        'fastecdsa',
        'pyusb',
        'pycrypto'
    ),
    dependency_links=(
        'https://github.com/fabiant7t/pycrypto/tarball/master#egg=pycrypto',
    )
)
