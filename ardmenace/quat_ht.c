
#include "plattest.h"
#include "board.h"
#include <stdlib.h>
#include <stdio.h>

// const int SIZE_LIST[6] = {101, 211, 431, 863, 1741, 3491}
#define HT_TABLE_SIZE 431

const uint8_t bbb[9] ={0, 2, 0,
			 0, 1, 0,
			 0, 0, 0};

int ht_used_slots = 0;

struct _ht_element_t_ {
	int key;
	uint8_t moves[9];
};
typedef struct _ht_element_t_ ht_element_t;

ht_element_t ht_arr[HT_TABLE_SIZE];

void error(char* msg)
{
	printf("ERROR: %s",msg );
	exit(-1);
}

void ht_sprint_element(char* buf, int indx)
{
	int n = 0;
	n += sprintf(buf+n, "key=%06d  ", ht_arr[indx].key);
	for(int i = 0; i < 9; i++)
	{
		n += sprintf(buf+n, "%02d ", (ht_arr[indx].moves[i]%100));
	}
}

void ht_clear()
{
	ht_used_slots = 0;
	for (int i = 0; i < HT_TABLE_SIZE; i++)
		ht_arr[i].key = 0;
}

int ht_hash(int key)
{
	long long int horner = 0;
	while (key > 0)
	{
		horner = 31 * horner + (key%10);
		key /= 10;
	}
	return horner % HT_TABLE_SIZE;
}

int ht_find_element_slot(int key)
{
	int slot = ht_hash(key);
	int add = 1;
	while (1)
	{
		if (ht_arr[slot].key == key)
			return slot;
		if (ht_arr[slot].key == 0)
			return slot;
		if (add > 300)
			error("ht too full");
		slot += add;
		add += 2;
	}
}

void ht_put(int key)
{
	int fountslot = ht_find_element_slot(key);
	if (ht_arr[fountslot].key != 0)
		error("find element slot wants to reinsert a key");
	ht_arr[fountslot].key = key;
	board_fill_empty_moves(key,(ht_arr[fountslot].moves));
	ht_used_slots++;
}

void ht_print_fulltable()
{
	char buf[256];
	for(int i = 0; i < HT_TABLE_SIZE; i++)
	{
		ht_sprint_element(buf, i);
		printf("indx=%03d %s\n",i,buf);
	}
}

int main()
{
	ht_print_fulltable();

	board_t a;
	for (int i = 0; i < 9; i++)
		a.arr[i] = bbb[i];

	print_board(&a);

	ht_put(board_to_key(&a));

	ht_print_fulltable();

	int slot = ht_find_element_slot(board_to_key(&a));
	board_fill_from_key(&a, ht_arr[slot].key);
	print_board(&a);

}


