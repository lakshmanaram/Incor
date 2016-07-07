import incor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='incor',
      version=incor.__version__,
      install_requires=['watchdog>=0.8.2', 'psutil>=4.3.0', 'subprocess32>=3.2.7'],
      description='INstant COde Runner runs the programs present in the mentioned folder '
                  'instantaneously as and when changes are made.',
      url='https://github.com/lakshmanaram/Program-runner/',
      author='lakshmanaram, srivatsan-ramesh',
      author_email='lakshmanaram.n@gmail.com, sriramesh4@gmail.com',
      license='MIT',
      packages=['incor'],
      entry_points={
          'console_scripts': ['incor=incor.incor:main'],
      },
      zip_safe=False)
