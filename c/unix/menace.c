
#include "menace.h"

struct _menace_history_t_
{
	int key;
	uint8_t indx;
};
typedef struct _menace_history_t_ menace_history_t;

uint8_t history_indx = 0;
uint8_t my_symbol = -1;
bool has_init = false;

menace_history_t history[9];

void menace_reset(uint8_t symb)
{
	if (!has_init)
		srand(time(NULL));
	history_indx = 0;
	my_symbol = symb;
}

void menace_make_move(board_t* from, board_t* to)
{
	int fromkey = board_to_key(from);
	board_t board_matched;
	board_t board_post_move;
	board_t board_post_transback;
	ht_element_t* ht_matched;

	uint8_t transid = 0;
	int testkey = fromkey;

	while (1)
	{
		int slot = ht_find_element_slot(testkey);
		ht_get_element(slot, &ht_matched);
		if (ht_matched->key == testkey)
			break;
		transid++;
		if (transid >= 6)
			break;
		board_transform_generic(from, &board_matched, transid);
		testkey = board_to_key(&board_matched);
	}

	if (transid >= 6)
	{
		ht_put(fromkey);
		ht_get_element(ht_find_element_slot(fromkey), &ht_matched);
	}

	int sum = 0;
	for(int i = 0; i < 9; i++)
	{
		sum += ht_matched->moves[i];
	}

	int rnd = rand() % sum;
// VERY UNFINISHED




	
}