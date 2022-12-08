#include<stdio.h>

FILE *fpointer;
int greatest[3];    //Holds the three greatest sums by the end of the program
int sum;    //Holds the sum of each group of values

//Function that stores the three greatest sums in the greatest array
void sortSums()
{
    int min_index=0;
    //Loop to keep track of index with lowest value in array
    for(int i=0;i<3;i++)
    {
        if(greatest[i]<greatest[min_index])
        {
            min_index = i;
        }
    }
    //Compare lowest value in array to sum
    if(sum>greatest[min_index])
    {
        greatest[min_index] = sum;
    }
}


void main()
{
    int num, total;
    fpointer = fopen("calories_elves.txt", "r");
    if(fpointer==NULL)
    {
        printf("Error opening file\n");
    }

    char buffer[10];
    while(!feof(fpointer))
    {
        fgets(buffer, 10, fpointer);
        if(strcmp(buffer, "\n")!=0)
        {
            num = atoi(buffer); //Converting the array of characters(buffer) into an integer
            sum += num;
        }
        else if(strcmp(buffer, "\n")==0) //Checking for line that only has new line character to know if end of a group of numbers is reached
        {
            sortSums();
            sum = 0;
        }
    }

    /*If the very last line of the file is not the new line character, the block of code above will add it to the sum but will not compare the sum to the values in the greatest array
     *The if block below ensures that this final sum is compared to the values in the greatest array*/
    if(feof(fpointer) && strcmp(buffer, "\n")!=0)
    {
        sortSums();
    }
    fclose(fpointer);

    for(int i=0;i<3;i++)
    {
        total += greatest[i];
    }
    printf("The greatest sum is: %d", total);

}


