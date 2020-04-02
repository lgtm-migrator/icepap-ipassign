from distutils.core import setup

setup(
     name='icepap-ipassign',
     version='0.0.0',
     author='Cyril Danilevski',
     author_email='cyril.danilevski@esrf.fr',
     description='',
     url='https://github.com/cydanil/icepap-ipassign',
     packages=['ipassign'],
     install_requires=['PyQt5>=5.12.0'],
     tests_require=['pytest'],
     python_requires='>=3.7',
     entry_points={
          "console_scripts": [
              'ipassign = gui.main:main',
              'ipassign-listener = utils.listener:main',
          ],
     },
     classifiers=[
         'Development Status :: 6 - Mature',
         'Environment :: X11 Applications :: Qt',
         'Intended Audience :: Developers',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: BSD License',
         'Operating System :: POSIX :: Linux',
         'Operating System :: Microsoft :: Windows',
         'Topic :: Scientific/Engineering',
        ],
)
