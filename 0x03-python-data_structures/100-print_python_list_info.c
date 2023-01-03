#include "Python.h"
/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, lsize;
	PyObject *item;
	const char *item_type;
	PyListObject *cast;

	cast = (PyListObject *)p;
	lsize = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) lsize);
	printf("[*] Allocated = %d\n", (int)cast->allocated);
	for (i = 0; i < lsize; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}
