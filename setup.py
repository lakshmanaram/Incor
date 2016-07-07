import incor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='incor',
      version=incor.__version__,
      install_requires=['watchdog>=0.8.2', 'psutil>=4.3.0'],
      description='INstant COde Runner compiles and executes the programs present in the mentioned folder '
                  'instantaneously as and when changes are .',
      url='https://github.com/lakshmanaram/Incor',
      author='lakshmanaram, srivatsan-ramesh',
      author_email='lakshmanaram.n@gmail.com, sriramesh4@gmail.com',
      license='MIT',
      packages=['incor'],
      entry_points={
          'console_scripts': ['incor=incor.main:main'],
      },
      keywords=['Algorithms', 'Competitive Programming', 'Automatic', 'run', 'compile', 'execute'],
      zip_safe=False)
