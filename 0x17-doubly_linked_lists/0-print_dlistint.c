#include "lists.h"
#include <stdio.h>
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int x;
	dlistint_t *runner;

	x = 0;
	runner = h;
	while (runner != NULL)
	{
		x++;
		runner = h->next;
	}
}
