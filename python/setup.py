from distutils.core import setup, Extension

module = Extension('_sphinx3',
                   include_dirs = ['../../sphinxbase/include',
                                   '../include',
                                   '/usr/local/include/sphinxbase/',
                                   '/usr/local/include/sphinx3',
                                   ],
                   libraries = ['sphinxutil', 'sphinxfe', 'sphinxfeat',
                                'sphinxad', 's3decoder'],
                   library_dirs = ['../../sphinxbase/src/libsphinxutil/.libs',
                               '../../sphinxbase/src/libsphinxad/.libs',
                               '../../sphinxbase/src/libsphinxfe/.libs',
                               '../../sphinxbase/src/libsphinxfeat/.libs',
                               '../src/libs3decoder/.libs',
                               ],
                   sources = ['_sphinx3module.c'])

setup(name = 'Sphinx3',
      version = '0.1',
      description = 'Python interface to Sphinx3 speech recognition',
      ext_modules = [module])
