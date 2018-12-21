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

   int j = 101;
   while(j<=200) {
      if ( j % 3 == 0 && j % 5 == 0) {
         printf("Minty Bear\n");
      } else if ( j % 3 == 0)  {
         printf("Minty\n");
      } else if ( j % 5 == 0) {
         printf("Bear\n");
      } else {
         printf("%d \n", j);
      }
      j++;
   }

   div(201, 300);
   return 0;

}

int div (int m, int n) {
   if(m>n) {
      return 0;
   } else if (m % 3 == 0 && m % 5 == 0){
      printf ("Minty Bear\n");
      div(m+1, n);
   } else if (m % 3 == 0) {
      printf ("Minty\n");
      div(m+1, n);
   } else if (m % 5 == 0) {
      printf("Bear\n");
      div(m+1, n);
   } else {
      printf ("%d\n", m);
      div(m+1, n);
   }
}
