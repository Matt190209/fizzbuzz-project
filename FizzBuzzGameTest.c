#include <stdio.h>
#include <string.h>

// ==== Definición mínima de FizzBuzzGame para test ====
typedef struct {
    int divisor1;
    int divisor2;
} FizzBuzzGame;

// ==== Función que vamos a testear ====
const char* fizzbuzz_value(FizzBuzzGame *game, int number) {
    static char buffer[20];
    if (number % game->divisor1 == 0 && number % game->divisor2 == 0)
        return "fizzbuzz";
    else if (number % game->divisor1 == 0)
        return "fizz";
    else if (number % game->divisor2 == 0)
        return "buzz";
    else {
        sprintf(buffer, "%d", number);
        return buffer;
    }
}

// ==== Test unitario  ====
int main() {
    FizzBuzzGame game;
    game.divisor1 = 3;
    game.divisor2 = 5;

    struct {
        int number;
        const char* expected;
    } tests[] = {
        {1, "1"},
        {3, "fizz"},
        {5, "buzz"},
        {15, "fizzbuzz"},
        {7, "7"}
    };

    int num_tests = sizeof(tests)/sizeof(tests[0]);
    int passed = 0;

    for(int i = 0; i < num_tests; i++) {
        const char* result = fizzbuzz_value(&game, tests[i].number);
        if(strcmp(result, tests[i].expected) == 0) {
            printf("Test %d passed ✅ (%d -> %s)\n", i+1, tests[i].number, result);
            passed++;
        } else {
            printf("Test %d Failed ❌ (%d -> %s, expected %s)\n", i+1, tests[i].number, result, tests[i].expected);
        }
    }

    printf("\n%d/%d tests passed.\n", passed, num_tests);

    return 0;
}
