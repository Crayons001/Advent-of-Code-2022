#include<stdio.h>

FILE *fpointer;

void main()
{
    int greatest=0, sum=0, num=0;
    fpointer = fopen("calories_elves.txt", "r");
    if(fpointer==NULL)
    {
        printf("Error opening file\n");
    }

    char buffer[10];
    while(!feof(fpointer))
    {
        fgets(buffer, 10, fpointer);
        if(strcmp(buffer, "\n")==0)
        {
            sum = 0;
            continue;
        }
        num = atoi(buffer); //Converting the array of characters(buffer) into an integer
        sum += num;
        if(sum>greatest)
        {
            greatest = sum;
        }
    }
    fclose(fpointer);
    printf("The greatest sum is: %d", greatest);

}

