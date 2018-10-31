#include <stdio.h>
#include <string.h>

int main(){
char s1[10];

scanf("%5s",&s1);
if(strcmp(&s1,"hello")){
    printf("ok!\n");
}
else{
    printf("noo..\n");
}


return 0;
}