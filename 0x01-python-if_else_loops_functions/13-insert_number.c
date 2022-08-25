#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node of linked list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *temp;
	int n;

	n = number;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (current)
	{
		if (current->n >  number)
		{
			new->next = current;
			*head = new;
			break;
		}
		else if ((current->n <= n) && (current->next)->n > n)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			break;
		}
		else if ((current->n <= n) && current->next == NULL)
		{
			new->next = NULL;
			current->next = new;

		}

		current = current->next;
	}
	return (new);
}
