#!/usr/bin/python3
f = __import__('add_0', globals(), locals(), [], 0)
a = 1;
b = 2

print("<a {}> + <b {}> = <add({}, {}) {}>".format(a, b, a, b, f.add(1, 2)))
