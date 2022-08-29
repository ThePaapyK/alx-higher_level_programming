#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *l_array, j, k;

	listint_t *current = *head;
	int i = 0, l = 0;

	while (current != NULL)
	{
		current = current->next;
		i++;
	}

	l_array = malloc(sizeof(int) * i);

	while (l < i)
	{
		l_array[l] = (*head)->n;
		(*head) = (*head)->next;
		l++;
	}

	for (k = 0, (j = i - 1); k < (i / 2); k++, j--)
	{
		if (l_array[k] != l_array[j])
			return (0);
	}
	free(l_array);
	return (1);
}
