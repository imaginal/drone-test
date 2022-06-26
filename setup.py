from distutils.core import setup

setup(name='Mavic',
      version='1.0',
      packages=['mavic'],
      entry_points={'console_scripts':['mavic=mavic:run']}
      )
