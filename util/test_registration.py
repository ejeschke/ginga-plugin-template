"""
This program allows you to test whether your plugin will register
itself correctly.
"""
from pkg_resources import iter_entry_points

groups = ['ginga.rv.plugins']

available_methods = []

for group in groups:
    for entry_point in iter_entry_points(group=group, name=None):
        available_methods.append(entry_point.load())

d = dict(name='Name', ptype='Type', klass='Class', module='Module')
print("%(name)14.14s  %(ptype)6.6s  %(klass)20s  %(module)20s" % d)

for method in available_methods:
    spec = method()
    # for debugging
    #print(spec)

    d = dict(spec)
    d.setdefault('name', spec.get('name', spec.get('menu', spec.get('klass', spec.get('module')))))
    d.setdefault('klass', spec.get('module'))
    d.setdefault('ptype', 'local')
    print("%(name)14.14s  %(ptype)6.6s  %(klass)20s  %(module)20s" % d)
