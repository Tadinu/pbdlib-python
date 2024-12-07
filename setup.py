from setuptools import setup, find_packages

# Setup:
setup(name='pbdlib',
      version='0.1',
      description='Programming by Demonstration module for Python',
      url='',
      author='Emmanuel Pignat',
      author_email='emmanuel.pignat@idiap.ch',
      license='MIT',
      packages=find_packages(),
      install_requires = ['numpy','scipy','matplotlib', 'scikit-learn', 'dtw', 'jupyter', 'termcolor'],
      zip_safe=False)
