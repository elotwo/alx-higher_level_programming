#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	dlistint_t *temp;
	while( current != NULL)
	{
		temp = current;
		current = current->next;
		free(temp);
	}
}
