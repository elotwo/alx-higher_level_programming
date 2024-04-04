#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current = head;
	unsigned int count = 0;
	while (current != NULL & count < index)
	{
		current = current->next;
		count++;
	}
	if(current == NULL || count < index)
	{
		return(NULL);
	}
	return(current);
}
