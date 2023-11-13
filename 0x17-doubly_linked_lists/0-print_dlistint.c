#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * print_dlistint - function prints all elements of a dlistint_t list
 * @h: pointer to the head of the list
 *
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0;
	
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		node_count++;
	}
	return (node_count);
}
