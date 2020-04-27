#include<stdio.h>

int func1(int a) {
    if (a == 1) {
        return func1(2);
    } else {
        return 2;
    }
}

int main() {
    int res = func1(1);
    printf("res: %d\n", res);
}