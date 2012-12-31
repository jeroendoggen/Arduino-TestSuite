from distutils.core import setup

from arduino_testsuite import __version__


with open('README.txt') as file:
    long_description = file.read()

setup(name='arduino_testsuite',
      version=__version__,
      description='Arduino TestSuite for automated Arduino Unit Testing',
      long_description=long_description,
      author='Jeroen Doggen',
      author_email='jeroendoggen@gmail.com',
      url='http://jeroendoggen.github.com/Arduino-TestSuite/',
      packages=['arduino_testsuite'],
      package_data={'arduino_testsuite': ['*.py', '*.conf']},
      license='GNU General Public License v2 or later (GPLv2+)',
      platforms=['Linux'],
      )
