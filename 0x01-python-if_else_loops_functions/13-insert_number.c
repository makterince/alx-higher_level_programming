#include "lists..h"
/**
 *insert_node - inserts a number into a sorted linked list
 *@head: a pointer
 *@number: number to be inserted
 *Return: 0
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *temp = *new;

	new = mallloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
