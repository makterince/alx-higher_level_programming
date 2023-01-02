#include "lists.h"
/**
 *check_cycle - basically checks if there is a loop by placing a slow and fast
 *pointer
 *@list: pointer
 *Return:1 if loop is found and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *fast;

	*temp = root;
	*fast = root;

	while (temp != NULL && fast->next != NULL)
	{
		temp = slow->next;
		fast = fast->next->next;

		if (temp == fast)
			return (1);

	}
	return (0);
}



