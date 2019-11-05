#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
/**
 * infinite_while - infinite loop
 *
 * Return: void
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates five zombie processes while it is waiting
 *
 * Return: 0 success
 */

int main(void)
{
	int my_pid1, my_pid2, my_pid3, my_pid4, my_pid5;

	my_pid1 = fork();
	if (my_pid1)
		printf("Zombie process created, PID: %d\n", my_pid1);
	else
		exit(0);

	my_pid2 = fork();
	if (my_pid2)
		printf("Zombie process created, PID: %d\n", my_pid2);
	else
		exit(0);

	my_pid3 = fork();
	if (my_pid3)
		printf("Zombie process created, PID: %d\n", my_pid3);
	else
		exit(0);

	my_pid4 = fork();
	if (my_pid4)
		printf("Zombie process created, PID: %d\n", my_pid4);
	else
		exit(0);

	my_pid5 = fork();
	if (my_pid5)
		printf("Zombie process created, PID: %d\n", my_pid5);
	else
		exit(0);

	infinite_while();
}
