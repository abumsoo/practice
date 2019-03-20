#include <stdio.h>
#include <stdlib.h>

/* If compiling on Windows compile these functions */
#ifdef _WIN32
#include <string.h>

static char buffer[2048];

/* Fake readline function */
char* readline(char* prompt) {
  fputs(prompt, stdout);
  fgets(buffer, 2048, stdin);
  char* cpy = malloc(strlen(buffer)+1);
  strcpy(cpy, buffer);
  cpy[strlen(cpy)-1] = '\0';
  return cpy;
}

/* Fake add_history function */
void add_history(char* unused) {}

/* Otherwise include the editline headers */
#else
#include <editline/readline.h>
#endif

/* Declare a buffer for user input of size 2048 */
/* static char input[2048]; */

int main(int argc, char** argv) {


  /* line number */
  int line = 1;

  /* In a never ending loop */
  while (1) {

    /* Print Version and Exit Information */
    puts("buzpy Version 0.0.0.1.0");
    puts("Press Ctrl+c to Exit\n");

    /* Output our prompt */
    /* fputs("lispy> ", stdout); */
    
    /* Read a line of user input of max size 2048 */
    /* fgets(input, 2048, stdin); */

    /* Output our prompt and get input */
    char* input = readline("buzpy> ");

    /* Add input to history */
    add_history(input);

    /* Echo input back to user */
    printf("%d: %s %s\n", 2.0, input, input);
    line++;

    /* Free retrieved input */
    free(input);

  }
  
  return 0;

}
