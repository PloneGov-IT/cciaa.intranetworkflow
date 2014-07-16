from setuptools import setup, find_packages
import os

version = '2.1.0.dev0'

setup(name='cciaa.intranetworkflow',
      version=version,
      description="Workflow of the CCIAA - C4P project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='c2p c3p c4p cciaa workflow',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://code.redturtle.it/svn/camera-di-commercio-fe/cciaa.intranetworkflow/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cciaa'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'redturtle.deletepolicy',
          'rt.lastmodifier',
          'TurtledGazette',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
