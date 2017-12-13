
#include "plattest.h"
#include "board.h"

// const int SIZE_LIST[6] = {101, 211, 431, 863, 1741, 3491}
#define HT_TABLE_SIZE = 431

int ht_used_slots = 0;

struct _ht_element_t_ {
	int key;
	uint8_t moves[9];
};
typedef struct _ht_element_t_ ht_element_t;

ht_element_t ht_arr[HT_TABLE_SIZE];

void ht_clear()
{
	for (int i = 0; i < HT_TABLE_SIZE; i++)
		ht_arr[i].key = 0;
}

// void ht_put_withmoves(int key, )
void ht_put(int key)
{
	
}


