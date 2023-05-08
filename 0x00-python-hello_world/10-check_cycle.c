#include "lists.h"
/**
 * check_cycle - check for cycle in linked listed
 * @list: linked list to check
 * Return: 1 if the list has cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
