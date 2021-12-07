#include <stdio.h>

int main(void)
{
  int increases = 0;
  int prev = -1;
  while (1)
  {
    int n;
    scanf("%d\n", &n);
    if (n == -1)
      break;

    if (n > prev && prev != -1)
      increases++;

    prev = n;
  }

  printf("%d\n", increases);

  return 0;
}