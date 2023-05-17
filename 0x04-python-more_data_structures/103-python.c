#include "stdio.h"
#include "stdlib.h"
#include "Python.h"
/**
 * print_python_list - print Python bytes objects.
 * @p: poiter of the Python bytes objects.
 * Return: Always 0 (Success)
 */
void print_python_bytes(PyObject *p)
{
char *mys;
long int size, x, li;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = ((PyVarObject *)(p))->ob_size;
mys = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", mys);

if (size >= 10)
li = 10;
else
li = size + 1;

printf("  first %ld bytes:", li);

for (x = 0; x < li; x++)
if (mys[x] >= 0)
printf(" %02x", mys[x]);
else
printf(" %02x", 256 + mys[x]);


printf("\n");
}
/**
 * print_python_list - print Python lists
 * @p: pointer of the python list.
 * Return: Always 0 (Success)
 */
void print_python_list(PyObject *p)
{
long int size, x;
PyListObject *mylist;
PyObject *myob;

size = ((PyVarObject *)(p))->ob_size;
mylist = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", mylist->allocated);

for (x = 0; x < size; x++)
{
myob = ((PyListObject *)p)->ob_item[x];
printf("Element %ld: %s\n", x, ((myob)->ob_type)->tp_name);
if (PyBytes_Check(myob))
print_python_bytes(myob);
}
}
