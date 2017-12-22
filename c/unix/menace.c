
#include "menace.h"

uint8_t moves_indx = 0;
uint8_t my_symbol = -1;

int key_buf[9];


void menace_reset(uint8_t symb)
{
	moves_indx = 0;
	my_symbol = symb;
}

void menace_make_move(board_t* from, board_t* to)
{
	int fromkey = board_to_key(from);
	board_transform_generic(from,to,0);
	board_t ht_matched_board;

	uint8_t* moves;

	ht_get_moves(fromkey,&moves);
}