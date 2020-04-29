#include<stdio.h>

int func1(int p1){
	printf("Called from main function: %d\n", p1);
}

int main() {
	printf("Hello World");
	func1(123);
}
