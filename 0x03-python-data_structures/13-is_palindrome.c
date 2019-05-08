#include "lists.h"
#include <stdlib.h>
/**
*is_palindrome - checks if a singly linked list is a palindrome
*
*@head: first element of the linked list
*
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	int i, j;
	listint_t *aux;
	int buf[10000];

	if (*head == NULL)
	{
		return (1);
	}
	for (i = 0, aux = *head; aux != NULL; aux = aux->next, i++)
	{
		buf[i] = aux->n;
	}
	for (j = 0, i = i - 1; j < i; j++, i--)
	{
		if (buf[j] != buf[i])
		{
			return (0);
		}
	}
	return (1);
}
