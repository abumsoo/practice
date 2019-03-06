#include <stdio.h>

void hello(int n) {
  for (int i = 0; i < n; i++){
    puts("hello");
  }
}

int main(int argc, char** argv) {
  /*
  for (int i = 0; i < 5; i++) {
    puts("Hello");
  }

  int i = 0;
  while (i < 5) {
    puts("Hello");
    i++;
  }
  */
  hello(5);

  return 0;
}
