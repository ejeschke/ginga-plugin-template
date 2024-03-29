from setuptools import setup, find_packages

# You can have one or more plugins.  Just list them all here.
# For each one, add a setup function in plugins/__init__.py
#
entry_points = """
[ginga.rv.plugins]
MyGlobalPlugin = template_plugins:setup_MyGlobalPlugin
MyLocalPlugin = template_plugins:setup_MyLocalPlugin
"""

setup(
    name = 'mygingaplugins',
    version = "0.2.dev",
    description = "Plugin examples for the Ginga reference viewer",
    author = "Tycho Brahe",
    license = "BSD",
    # change this to your URL
    url = "http://ejeschke.github.com/ginga-plugin-template",
    install_requires = ["ginga>=3.4.1"],
    packages = find_packages(),
    include_package_data = True,
    package_data = {},
    entry_points = entry_points,
)
