#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"
/**
 * main - A function that prints the number of element in alist
 * @h: varible for entering structured list
 * Return: (0)success
 */
size_t dlistint_len(const dlistint_t *h)
{
        const dlistint_t *current = h;
        size_t count = 0;
        while (current != NULL)
        {
                current = current->next;
                count++;
        }
        return(count);
}
