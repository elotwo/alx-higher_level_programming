#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node = (dlistint_t*)malloc(sizeof(dlistint_t));
	dlistint_t *current = new_node;
	new_node->n = n;
	new_node->prev = *head;
	new_node->next = NULL;

	if (new_node == NULL)
	{
		return(NULL);
	}
	if (*head == NULL)
	{
		(*head) = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		current->next = new_node;
		new_node->prev = current;
	}
	return(new_node);
}
