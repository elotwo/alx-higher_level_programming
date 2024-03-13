#include "lists.h"

/**
 * check_cycle - checks if a linked list have a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slo = list;
	listint_t *fas = list;

	if (!list)
		return (0);

	while (slo && fast && fas->next)
	{
		slo = slo->next;
		fas = fas->next->next;
		if (slo == fas)
			return (1);
	}

	return (0);
}


