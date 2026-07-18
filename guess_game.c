#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int target, guess, attempts;
    int maxAttempts = 7;
    srand((unsigned int)time(NULL));
    target = (rand() % 100) + 1;
    printf("=== Number Guessing Game ===\n");
    printf("I'm thinking of a number from 1 to 100.\n");
    printf("You have %d attempts. Let's go!\n\n", maxAttempts);
    attempts = 0;
    while (attempts < maxAttempts) {
        printf("Attempt %d/%d - Enter your guess: ", attempts + 1, maxAttempts);

        if (scanf("%d", &guess) != 1) {
            printf("\nPlease enter a valid number.\n");
            return 0;
        }
        attempts++;
        if (guess < 1 || guess > 100) {
            printf("Out of range! Guess between 1 and 100.\n\n");
            attempts--; // don't count invalid input
            continue;
        }
        if (guess == target) {
            printf("\nCorrect! You got it in %d attempt(s). 🎉\n", attempts);
            printf("Thanks for playing!\n");
            return 0;
        } else if (guess < target) {
            printf("Not quite. Try higher.\n\n");
        } else {
            printf("Not quite. Try lower.\n\n");
        }
    }
    printf("\nSorry! You ran out of attempts.\n");
    printf("The number was %d.\n", target);
    printf("Better luck next time!\n");
    return 0;
}
