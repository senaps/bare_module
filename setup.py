from setuptools import find_packages, setup
import re

# packages required for this module
with open('requirements.txt', 'r') as requirements_file:
    REQUIRED_PACKAGES = requirements_file.read()


# Import the README and use it as the description.
with open('README.md', 'r') as readme_file:
    DESCRIPTION = '\n' + readme_file.read()

# Load the package's __version__.py
regex = r"(\d*\.\d*\.\d*)"
with open('__version__.py') as version_file:
    VERSION = re.findall(regex, version_file.read())[0]



setup(name='',
      version=VERSION,
      description='',
      long_description=DESCRIPTION,
      long_description_content_type='text/markdown',
      author='',
      author_email='',
      url='',
      packages=find_packages(exclude=('tests', 'docs')),
      # py_modules=['mypackage'],

      install_requires=REQUIRED_PACKAGES,
      include_package_data=True,

      #license='MIT',
      # classifiers=[# Trove classifiers
      #       'License :: OSI Approved :: MIT License',
      #       'Programming Language :: Python',
      #       'Programming Language :: Python :: 3',
      #       'Programming Language :: Python :: 3.6',
      #       'Programming Language :: Python :: Implementation :: CPython',
      #       'Programming Language :: Python :: Implementation :: PyPy'],

      # entry_points={
      #     'console_scripts': ['mycli=module:cli'],
      # },
      )

