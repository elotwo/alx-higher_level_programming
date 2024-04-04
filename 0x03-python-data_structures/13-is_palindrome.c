#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 */
int is_palindrome(listint_t **head)
{
	int j = 0;
	int z = 0;
	const listint_t *back = *head, *forward = *head;
	if (*head == NULL || (*head)->next == NULL)
        return (1);
	while (forward != NULL)
	{
		forward = forward->next;
		j++;
	}
	for (z = 0; z < j/2; z++)
	{
		back = back->next;
	}
	while (back != NULL)
	{
		if (back->n != forward->n)
			return (0);
		back = back->next;
		forward = forward->next;
	}
	return (1);
}
