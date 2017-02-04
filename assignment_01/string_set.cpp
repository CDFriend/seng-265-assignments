#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

string_set::string_set() {
	//initialize iterator index to 0
	iterator_index = 0;
	//set all hash table values to null
	for (int i = 0; i < HASH_TABLE_SIZE; i++) {
		hash_table[i] = NULL;
	}
}

void string_set::add(const char *s) {
	reset(); //reset iterator
	if (contains(s) == 1) {
		duplicate_exception ex;
		throw ex;
	}
	//get index of the desired linked list
	int headIndex = hash_function(s);
	node *n;
	try {
		n = new node;
	}
	catch (...) {
		throw memory_exception();
	}
	n->s = new char[strlen(s) + 1];
	strcpy(n->s, s);
	n->next = hash_table[headIndex];
	hash_table[headIndex] = n;
}

void string_set::remove(const char *s) {
	//get element's list index
	int headIndex = hash_function(s);
	//no elements in list
	if (!hash_table[headIndex]) {
		throw not_found_exception();
	}
	//1st element
	if (strcmp(hash_table[headIndex]->s, s) == 0) {
		node *next = hash_table[headIndex]->next;
		delete hash_table[headIndex];
		hash_table[headIndex] = next;
	}
	//iterate through list
	else {
		bool found = false;
		node *current = hash_table[headIndex]->next;
		node *previous = hash_table[headIndex];
		while (current) {
			cout << current->s << endl;
			//delete node if found
			if (strcmp(current->s, s) == 0) {
				previous->next = current->next;
				delete current;
				found = true;
				break;
			}
			//advance pointers
			previous = current;
			current = current->next;
		}
		if (!found) {
			throw not_found_exception();
		}
	}
	reset(); //reset iterator
}

int string_set::contains(const char *s) {
	int headIndex = hash_function(s);
	node *current = hash_table[headIndex];
	while (current) {
		if (strcmp(current->s, s) == 0) {
			return 1;
		}
		current = current->next;
	}
	//not found
	return 0;
}

void string_set::reset() {
	iterator_index = 0;
	iterator_node = hash_table[iterator_index];
}

const char *string_set::next() {
	//find list with data
	while (iterator_node == NULL && iterator_index < HASH_TABLE_SIZE) {
		iterator_index++;
		iterator_node = hash_table[iterator_index];
	}
	if (iterator_index >= HASH_TABLE_SIZE) {
		return NULL;
	}
	const char *output = iterator_node->s;
	//advance iterator
	iterator_node = iterator_node->next;
	return output;
}

string_set::~string_set() {
	//iterate through hash table
	for (int i = 0; i < HASH_TABLE_SIZE; i++) {
		node *nextNode = hash_table[i];
		//iterate through list
		while (nextNode) {
			delete nextNode->s;
			node *current = nextNode;
			nextNode = nextNode->next;
			delete current; 
		}
	}
}

int string_set::hash_function(const char *s) {
	int sumChars = 0;
	for (int i = 0; s[i] != '\0'; i++) {
		sumChars += s[i];
	}
	return sumChars % HASH_TABLE_SIZE;
}
