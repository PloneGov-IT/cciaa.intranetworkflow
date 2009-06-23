from setuptools import setup, find_packages
import os

version = '1.3.2'

setup(name='cciaa.intranetworkflow',
      version=version,
      description="Workflow della Camera di Commercio - progetto C3P",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='c2p cciaa workflow',
      author='RedTurtle Technology S.r.L.',
      author_email='info@redturtle.net',
      url='https://code.redturtle.it/svn/camera_di_commercio_fe/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cciaa'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
