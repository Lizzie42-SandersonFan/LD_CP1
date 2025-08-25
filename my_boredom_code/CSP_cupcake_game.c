// Project from CSP but written in C

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int cakeFlavor = 1;
char cakeFlavorReview[50];
int frostingFlavor = 2;
char frostingFlavorReview[50];

int cakePan = 1;
char cakePanReview[50];
int cakeStat = 2;
int ovenTemp = 0;

int frostPiped = 1;
char forstPipedReview[50];
char allToppings[3][30] = {"sprinkles", "strawberries", "fudge sauce"};
bool isSprinkles = false;
bool isStrawberries = false;
bool isFudge = false;
char toppingReview[100];
char toppings[100];
char response[10];

char explanationMessage[100];
char customerAnswer[200];
int userNotTrying = 0;
int certificate = 0;

void toppingRequest(char allToppings[3]) {
    printf("\nWould you like %s (YES or NO)?\n", allToppings[3]);
    scanf("%s", response);
    
}

int main(void){
    printf("\nWelcome to Baking Simulator.\nIn this game you will get to bake a cake and have a critic try it.\nThe critic will give feedback based on your cake.\nYour goal is to have the critic love your cake!\n");
    printf("IMPORTANT NOTE:\nWhen answering questions, answer with the number of the option you want,\nUNLESS a different answering method is specified.\n:)\n");
    printf("Also, if you choose to not play the game correctly, something bad will happen...");

    int flavor;
    printf("\nWhat kind of cake would you like to make?\n (1 a vanilla cake\n (2 a chocolate cake\n (3 A carrot cake\n");
    scanf("%d", &flavor);

    if (flavor == 1){
        cakeFlavor = 1;
    } else if (flavor == 2){
        cakeFlavor = 2;
    } else if (flavor == 3){
        cakeFlavor = 3;
    } else {
        printf("We don't have the ingredients to make that type of cake.\n");
        userNotTrying = 1;
    }
    printf("%d\n", cakeFlavor);

    int frosttype;
    printf("\nWhat type of frosting do you want on your cake?\n (1 A buttercream frosting\n (2 A cream cheese frosting\n (3 A swiss meringue frosting\n");
    scanf("%d", &frosttype);

    if (frosttype== 1){
        frostingFlavor = 1;
    } else if (frosttype == 2){
        frostingFlavor = 2;
    } else if (frosttype == 3){
        frostingFlavor = 3;
    } else { 
        printf("We don't have this type of frosting in stock.\n");
        userNotTrying = 1;
    }
    printf("%d\n", frostingFlavor);

    int shape;
    printf("\nWhat kind of cake will you bake?\n (1 A circle cake\n (2 a square cake\n (3 multi tier cake\n");
    scanf("%d", &shape);

    if (shape==1) {
        cakePan=1; // there is a review variable
    } else if (shape==2){
        cakePan=2;
    } else if (shape==3){
        cakePan=3;
    } else {
        printf("We don't have that kind of cakepan\n");   
        userNotTrying = 1;
    }
    printf("%d\n", cakePan);

    int temp;
    printf("\nWhat temperature will you set the oven to in fahrenheit(NUMBER PLEASE)?\n");
    scanf("%d", &temp); 
    if (temp>=350 && temp<=375){
        ovenTemp = 2;
        cakeStat = 2;
        printf("Your cake is perfect!\n");
    } else if (temp<349 && temp >= 300){
        ovenTemp = 1;
        cakeStat = 1;
        printf("Your cake is a little undercooked but it will work\n");
    } else if (temp>376 && temp<=420) {
        ovenTemp = 3;
        cakeStat = 3;
        printf("Your cake is a little overcooked but it will work\n");
    } else if (temp<=300){
        printf("Your cake is still batter and the customer is furious. Game over. :(\n");
        exit(1);
    } else {
        printf("The oven has lit on fire and burned down the bakery, game over. :(\n");
        exit(1);
    }
    printf("%d\n", temp);

    int frostingPiped;
    printf("\nHow would you like to add the frosting:\n (1 Piped\n (2 Spooned on\n (3 No frosting\n");
    scanf("%d", &frostingPiped);
    if (frostingPiped == 1){
        frostPiped = 1;
    } else if (frostingPiped == 2){
        frostPiped = 2;
    } else if (frostingPiped == 3){
        frostPiped = 3;
    } else {
        printf("We are unable to apply the frosting that way.");
        userNotTrying = 1;
    }
    printf("%d\n", frostPiped);

    // NEED HELP PLEASE
    int i;
    for(i = 0; i < 3; i++){
        toppingRequest(allToppings[i]);
        //int x;
        //for (int x = 0; response[x] != '\0'; x++) {
            //response[x] = toupper(response[x]);
        //}
        if (i == "sprinkles"){
            if (response == "YES" || response == "YA" || response == "SURE" || response == "YEAH" || response == "YEE"){
                isSprinkles = true;
            }
        }
        if (i == "strawberries"){
            if (response == "YES" || response == "YA" || response == "SURE" || response == "YEAH" || response == "YEE"){
                isStrawberries = true;
            }
        }
        if (i == "fudge sauce"){
            if (response == "YES" || response == "YA" || response == "SURE" || response == "YEAH" || response == "YEE"){
                isFudge = true;
            }
        }
    }

    printf("%s\n", isSprinkles);
    printf("%s\n", isStrawberries);
    printf("%s\n", isFudge);
    return 0;
}