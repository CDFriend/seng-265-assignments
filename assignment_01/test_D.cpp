#include <iostream>
#include <stdio.h>

#include "string_set.h"

using namespace std;

int main() {
	string_set set;
	set.add("abc");
	set.add("a");
	set.add("c");
	set.add("123");
	const char *c = set.next()
	while(*c != NULL) {
		cout << c << endl;
	}
}
