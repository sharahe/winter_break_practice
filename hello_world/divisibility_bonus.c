#include <stdio.h>
  
int main () {
   int numOne, numTwo;
   char wordOne[255], wordTwo[255];
   printf ("First word: ");
   scanf ("%s", &wordOne);
   printf ("Second word: ");
   scanf ("%s", &wordTwo);
   printf ("'%s' will be printed when the number is divisible by: ", wordOne);
   scanf ("%d", &numOne);
   printf ("'%s' will be printed when the number is divisible by: ", wordTwo);
   scanf ("%d", &numTwo);

   for (int i = 1; i<= 100; i++) {
      if ( i % numOne == 0 && i % numTwo == 0) {
         printf("%s %s\n", wordOne, wordTwo);
      } else if ( i % numOne  == 0)  {
         printf("%s\n", wordOne);
      } else if ( i % numTwo == 0) {
         printf("%s\n", wordTwo);
      } else {
         printf("%d \n", i);
      }
   }
   return 0;
}
