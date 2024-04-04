#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"
/**
 * main - A function that prints the number of element in alist
 * @h: varible for entering structured list
 * Return: (0)success
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;
	size_t count = 0;
	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		count++;
	}
	return(count);
}
