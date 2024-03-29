
## Plugin Template for making a Ginga scientific viewer plugin

This is a template for creating a plugin to be used in the [Ginga
viewer](https://github.com/ejeschke/ginga).

For full instructions on writing a plugin, please [see the Ginga
documentation](http://ginga.readthedocs.io/en/latest/manual/plugins.html)
on plugins.


### Quick and Dirty Instructions for the impatient

You will want to do something like the following steps:

1. Pick a name for your new package which can be different from the name(s)
   of the plugin(s).  As an example, lets call our new package "rgbtools".

2. Clone the repository in the name of your new separately distributed
   package of plugin(s).

```bash
$ git clone https://github.com/ejeschke/ginga-plugin-template.git rgbtools
```

3. Change the name of the directory "template_plugins" to reflect the name
   of your separately distributed package. Use a different name than the
   module or class name(s) of the plugin(s).  In our example case, we'll
   use "rgbtools_plugins":

```bash
$ cd rgbtools
$ git mv template_plugins rgbtools_plugins
```

4. Decide on the names of your plugins.  In our example, suppose we want
   one plugin named "WhiteBalance" and one named "Curves".  (You can have
   as many plugins as you want in one package).  We will follow the standard
   Python convention of using lower case module names and camel-case class
   names.  In addition, you can specify different names for the menu to
   invoke the plugin and the tab that is shown when the plugin is activated,
   so keep that in mind when thinking of names.

5. Edit setup.py

   This file controls how the package is installed and what external
   packages it needs.  Nominally, you will want to change the name, title,
   url, etc. Be sure to change the name and the entries in the entry_points
   accordingly.  Something like:

```python
entry_points = """
[ginga.rv.plugins]
WhiteBalance=rgbtools_plugins:setup_WhiteBalance
Curves=rgbtools_plugins:setup_Curves
"""

setup(
    name = 'rgbtools',
    ...
)
```

6. Copy and modify one or more of the two files in the newly renamed 
   "rgbtools_plugins" directory.

   If you are making a global type plugin (the most general) you would
   want to start with "myglobalplugin.py".  If a local plugin (see the
   link above for a description of the difference) use "mylocalplugin.py".
   Copy and modify accordingly.  Let's suppose our two plugins will be
   of the global type, so we'll make two copies for our own plugins:

```bash
$ cd rgbtools_plugins

# copy the ones we want
$ cp myglobalplugin.py whitebalance.py
$ cp myglobalplugin.py curves.py

# don't forget later to "git add" your new plugins and to "git rm" the older
 example plugins
```

7. Edit whitebalance.py and curves.py

   You are now editing the modules that actually define your plugins.
   You'll want to edit the class names to reflect the change.  E.g.
   from "MyGlobalPlugin" to "WhiteBalance".  There are two places that
   are most important for the rename: in the class initializer (class name
   and superclass initializer call) and in the __str__ method at the end,
   which should be a lower case spelling of the class name.

8. Edit rgbtools_plugins/__init__.py

   This has the functions that are actually called to fetch the information
   needed to register the plugin.  Edit/rename function names as appropriate:

```python
...

def setup_WhiteBalance():
    spec = Bunch(path=os.path.join(p_path, 'whitebalance.py'),
                 module='whitebalance', klass='WhiteBalance',
                 ptype='global', workspace='right',
                 category='RGB Tools', menu="White Balance",
                 tab='White Balance')
    return spec

def setup_Curves():
    spec = Bunch(path=os.path.join(p_path, 'curves.py'),
                 module='curves', klass='Curves',
                 ptype='global', workspace='right',
                 category='RGB Tools', menu="Curves",
                 tab='Curves')
    return spec
```

9. Once you think you have the plugin(s) created correctly, install it using
   the usual "pip install ." installation method.  Then run the program
   "util/test_registration.py" to see whether your plugins will be seen by
   Ginga.  You should see a separate line for all separately distributable
   plugins:

```bash
$ cd ..
$ python setup.py install
...

$ python util/test_registration.py
          Name    Type                 Class                Module
 White Balance  global          WhiteBalance          whitebalance
        Curves  global                Curves                curves
...
```

NOTE: when you run test_registration, you will see ALL externally loadable
plugins, not just those for your own package.
