#include<stdio.h>

int func3(int b) {
    printf("Inside func3 %d, called from main\n", b);
    return 123;
}

int func2(int a) {
    printf("Inside func2 %d, called from func1\n", a);
    return 345;
}

void func1() {
    printf("Inside func1\n");
    int a = func2(12);
    printf("Result %d\n", a);
}

int main() {
    func1();
    int res = func3(123);
    printf("res : %d\n", res);
}