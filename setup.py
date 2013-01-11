"""Setup file for arduino_testsuite

Define the options for the "arduino_testsuite" package
Create source Python packages (python setup.py sdist)
Create binary Python packages (python setup.py bdist)
Upload these packages to PyPI (python setup.py sdist upload)

"""
from distutils.core import setup

from arduino_testsuite import __version__


with open('README.txt') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(name='arduino_testsuite',
      version=__version__,
      description='Arduino TestSuite for automated Arduino Unit Testing',
      long_description=LONG_DESCRIPTION,
      author='Jeroen Doggen',
      author_email='jeroendoggen@gmail.com',
      url='http://jeroendoggen.github.com/Arduino-TestSuite/',
      packages=['arduino_testsuite'],
      package_data={'arduino_testsuite': ['*.py', '*.conf']},
      license='GNU General Public License v2 or later (GPLv2+)',
      platforms=['Linux'],
      )
