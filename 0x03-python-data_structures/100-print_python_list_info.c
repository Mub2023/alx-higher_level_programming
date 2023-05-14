#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer of list
 * Returne: Always 0(Success)
 */
void print_python_list_info(PyObject *p)
{
	int size, al, x;
	PyObject *obi;

	size = Py_SIZE(p);
	al = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", al);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		obi = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obi)->tp_name);
	}
}
