from pybuilder.core import use_plugin, init, Author

use_plugin("pypi:pybuilder_scm_ver_plugin")
use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("filter_resources")


name = "yaml-extras"
default_task = "publish"

authors = [Author("Kyrylo Shpytsya", "kshpitsa@gmail.com")]
license = "MIT"
summary = "yaml-related Python library for internal use by several of my projects"
url = "https://github.com/kshpytsya/yaml-extras"


@init
def set_properties(project):
    project.depends_on("ruamel.yaml>=0.14.2,<1")
    project.depends_on("Cerberus>=1.0.1,<2")
    project.set_property('filter_resources_glob', ['**/kshpytsya/yaml_extras/__init__.py'])
    project.set_property("distutils_classifiers", [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control'
    ])
