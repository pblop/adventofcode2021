#include <stdio.h>

int main(void)
{
  int increases = 0;

  // number | windows
  // 199    | A
  // 200    | A B
  // 208    | A B C
  // 210    |   B C D
  // 200    |     C D E
  // 207    |       D E F

  // For the number 210 (iteration 4), win_n1 would be the sum of window A,
  // win_0 would be the sum of window B,
  // win_1 would be the (still not finished) sum of window C,
  // win_2 would be the (just started) sum of window D.
  // This pattern repeats for every number. win_n1 is the window that ends just before
  // the number, win_0 is the window that ends on that number, win_1 is the window
  // that ends on the next number, and win_2 is the window that ends on the number after
  // that.
  // /\ That can be written as, win[-1] is the window that ends on iteration i-1.
  // win[0] is the window that ends on iteration i.
  // win[1] .... iteration i+1
  // win[2] .... iteration i+2
  int win_n1 = 0, win_0 = 0, win_1 = 0, win_2 = 0;
  int i = 0;

  while (1)
  {
    int n;
    scanf("%d\n", &n);
    if (n == -1)
      break;

    win_0 += n;
    win_1 += n;
    win_2 += n;

    // We need to do a few iterations before windows A and B are filled, and
    // we can start comparing for real.
    // That happens on the fourth iteration (i==3).
    if (i >= 3 && win_0 > win_n1)
      increases++;

    win_n1 = win_0;
    win_0 = win_1;
    win_1 = win_2;
    win_2 = 0;

    i++;
  }

  printf("%d\n", increases);

  return 0;
}