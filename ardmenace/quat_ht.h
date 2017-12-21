
//NEED INCLUDE GUARDS


#include "plattest.h"
#include "board.h"

// const int SIZE_LIST[6] = {101, 211, 431, 863, 1741, 3491}

#define HT_TABLE_SIZE 431

struct _ht_element_t_ {
	int key;
	uint8_t moves[9];
};
typedef struct _ht_element_t_ ht_element_t;

void error(char* msg);
void ht_sprint_element(char* buf, int indx);
void ht_clear();
int ht_hash(int key);
int ht_find_element_slot(int key);
void ht_put(int key);
void ht_print_fulltable();

//REPLACE MAIN WITH Get tableused count
int main();
