#include <stdio.h>
  
int main () {
   for (int i = 1; i<= 100; i++) {
      if ( i % 3 == 0 && i % 5 == 0) {
         printf("Minty Bear\n");
      } else if ( i % 3 == 0)  {
         printf("Minty\n");
      } else if ( i % 5 == 0) {
         printf("Bear\n");
      } else {
         printf("%d \n", i);
      }
   }
return 0;
}
