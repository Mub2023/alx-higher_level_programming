#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to the list.
 * Return: Always Nothing (Success)
 */
void print_python_list(PyObject *p)
{
Py_ssize_t s, a, i;
const char *ty;
PyListObject *list = (PyListObject *)p;
PyVarObject *v = (PyVarObject *)p;

s = v->ob_size;
a = list->allocated;

fflush(stdout);

printf("[*] Python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}
printf("[*] Size of the Python List = %ld\n", s);
printf("[*] Allocated = %ld\n", a);
for (i = 0; i < s; i++)
{
ty = list->ob_item[i]->ob_type->tp_name;
printf("Element %ld: %s\n", i, ty);
if (strcmp(ty, "bytes") == 0)
print_python_bytes(list->ob_item[i]);
else if (strcmp(ty, "float") == 0)
print_python_float(list->ob_item[i]);
}
}
/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: pointer of the Pyobject,
 * Return Always nothing.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t s, i;
PyBytesObject *b = (PyBytesObject *)p;

fflush(stdout);
printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", b->ob_sval);

if (((PyVarObject *)p)->ob_size >= 10)
s = 10;
else
s = ((PyVarObject *)p)->ob_size + 1;
printf("  first %ld bytes: ", s);
for (i = 0; i < s; i++)
{
printf("%02hhx", b->ob_sval[i]);
if (i == (s - 1))
printf("\n");
else
printf(" ");
}
}
/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: is the pointerof the PyObyject
 * Return:Always Nothing (successs)
 */
void print_python_float(PyObject *p)
{
char *b = NULL;

PyFloatObject *flot = (PyFloatObject *)p;

fflush(stdout);
printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
b = PyOS_double_to_string(flot->ob_fval, 'r', 0,
Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", b);
PyMem_Free(b);
}
