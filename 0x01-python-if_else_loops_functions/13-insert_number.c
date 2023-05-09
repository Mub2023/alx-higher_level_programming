#include "lists.h"
/**
 * insert_node - nserts a number into a sorted singly linked list.
 * @head: is the pointer of pointer.
 * @number: is integer.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mynode = *head, new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (mynode == NULL || mynode->n >= number)
	{
		new->next = mynode;
		*head = new;
		return (new);
	}
	while (mynode && mynode->next && mynode->next->n < number)
		mynode = mynode->next;

	new->next = mynode->next;
	mynode->next = new;

	return (new);
}
