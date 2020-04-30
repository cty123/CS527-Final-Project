#include<stdio.h>
#include<stdlib.h>

void func1(){
    printf("Test");
}

int main() {
    func1();
    malloc(20);
    return 0;
}
