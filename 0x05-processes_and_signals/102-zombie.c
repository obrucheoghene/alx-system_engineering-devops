#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * loop_forever - loops continues to make the program hang
 * Return: always 0
*/
int loop_forever(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
*/
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	loop_forever();
	return (0);
}
