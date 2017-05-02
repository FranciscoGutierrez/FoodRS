fromm setuptools import setup

setup(name='FoodRS',
      version='0.1',
      description='https://github.com/FranciscoGutierrez/FoodRS/',
      url='http://github.com/storborg/funniest',
      author='Franisco G.',
      author_email='francisco.g@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'scipy',
          'sklearn'
      ],
      zip_safe=False)
