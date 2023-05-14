#include "lists.h"
/**
 * reverse - Reverse a singly linked list.
 * @head: Apointer to starting node of the list.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse(listint_t **head)
{
	listint_t *N = *head, *next, *prev = NULL;

	while (N)
	{
		next = N->next;
		N->next = prev;
		prev = N;
		N = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head:poimter of pointer.
 * Return:0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *tm, *rev, *midl;
size_t s = 0, x;

if (*head == NULL || (*head)->next == NULL)
	return (1);
tm = *head;
while (tm)
{
	s++;
	tm = tm->next;
}
tm = tm->next->next;
rev = reverse(&tm);
midl = rev;
tm = rev;
while (rev)
{
	if (tm->n != rev->n)
		return (0);
	tm = tm->next;
	rev = rev->next;
}
reverse(&midl);

return (1);
}
