## main setup file
from os import path
import sys
from setuptools import setup,find_packages
from setuptools.extension import Extension
    
setup(name='rakun',
      version='0.2',
      description="Rank-based unsupervised keyword detection via metavertex aggregation",
      url='http://github.com/skblaz/rakun',
      author='Blaž Škrlj',
      author_email='blaz.skrlj@ijs.si',
      license='GPL3',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['nltk','networkx','editdistance','pandas','numpy'],
      include_package_data=True)

