#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Caitlin Kavenaugh',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO wrapper for a Feedforward Neural Net surrogate model that can be slotted into the MetaModel component',
 'download_url': '',
 'entry_points': '[openmdao.surrogatemodel]\nneural_net.neural_net.NeuralNet=neural_net.neural_net:NeuralNet\n\n[openmdao.container]\nneural_net.neural_net.NeuralNet=neural_net.neural_net:NeuralNet',
>>>>>>> 2d9e8256330ab475b967533e4780e956723fcff9
 'include_package_data': True,
 'install_requires': ['openmdao.main', 'ffnet'],
 'keywords': ['openmdao'],
 'license': 'GNU General Public License, version 2',
 'maintainer': 'Kenneth T. Moore',
 'maintainer_email': 'kenneth-t-mooore-1@nasa.gov',
 'name': 'neural_net',
<<<<<<< HEAD
 'package_data': {'neural_net': ['sphinx_build/html/index.html',
                                 'sphinx_build/html/.buildinfo',
                                 'sphinx_build/html/py-modindex.html',
                                 'sphinx_build/html/objects.inv',
                                 'sphinx_build/html/searchindex.js',
                                 'sphinx_build/html/search.html',
                                 'sphinx_build/html/pkgdocs.html',
                                 'sphinx_build/html/usage.html',
                                 'sphinx_build/html/genindex.html',
                                 'sphinx_build/html/srcdocs.html',
                                 'sphinx_build/html/_sources/usage.txt',
                                 'sphinx_build/html/_sources/pkgdocs.txt',
                                 'sphinx_build/html/_sources/index.txt',
                                 'sphinx_build/html/_sources/srcdocs.txt',
                                 'sphinx_build/html/_static/plus.png',
                                 'sphinx_build/html/_static/comment-bright.png',
                                 'sphinx_build/html/_static/comment.png',
                                 'sphinx_build/html/_static/down-pressed.png',
                                 'sphinx_build/html/_static/sidebar.js',
                                 'sphinx_build/html/_static/doctools.js',
                                 'sphinx_build/html/_static/ajax-loader.gif',
                                 'sphinx_build/html/_static/default.css',
                                 'sphinx_build/html/_static/down.png',
                                 'sphinx_build/html/_static/jquery.js',
                                 'sphinx_build/html/_static/underscore.js',
                                 'sphinx_build/html/_static/minus.png',
                                 'sphinx_build/html/_static/up-pressed.png',
                                 'sphinx_build/html/_static/up.png',
                                 'sphinx_build/html/_static/pygments.css',
                                 'sphinx_build/html/_static/searchtools.js',
                                 'sphinx_build/html/_static/file.png',
                                 'sphinx_build/html/_static/basic.css',
                                 'sphinx_build/html/_static/websupport.js',
                                 'sphinx_build/html/_static/comment-close.png',
                                 'sphinx_build/html/_modules/index.html',
                                 'sphinx_build/html/_modules/neural_net/neural_net.html',
                                 'sphinx_build/html/_images/NNTutorial.png',
                                 'sphinx_build/html/_downloads/NN_sin.py',
                                 'test/openmdao_log.txt',
                                 'test/test_neural_net.py']},
=======
 'package_data': {'neural_net': []},
>>>>>>> 2d9e8256330ab475b967533e4780e956723fcff9
 'package_dir': {'': 'src'},
 'packages': ['neural_net'],
 'url': 'https://github.com/OpenMDAO-Plugins/neural_net',
 'version': '0.6',
 'zip_safe': False}


setup(**kwargs)

