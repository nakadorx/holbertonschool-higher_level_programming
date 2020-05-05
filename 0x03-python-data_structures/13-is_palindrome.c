#include "lists.h"
/**
* is_palindrome - holebrton
* @head: int
* Return: 0
*/
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j = 0;
	listint_t *tmp = *head;
	int *array;

	if (!*head)
		return (1);
	while (tmp)
	{
		tmp = tmp->next;
		len++;
	}
	array = (int *) malloc(len * sizeof(int));
	tmp = *head;
	while (tmp)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	while (array)
	{
		if (array[j] != array[i])
		{
			free(array);
			return (0);
		}
		i--;
		j++;
	}
	return (1);
}
