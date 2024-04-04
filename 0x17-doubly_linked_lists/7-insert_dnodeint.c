#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *current = *h;
	unsigned int x;
	for (x = 0; current != NULL; x++)
	{
		if (x == idx)
		{
			current->n = n;
			break;
		}
	}
	return(current);
}
