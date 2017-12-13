#include "board.h"

const uint8_t IND_CIRCLE[8] = {0,1,2,5,8,7,6,3}; 

const uint8_t bbb[9] ={0, 2, 0,
			 0, 1, 0,
			 0, 0, 0};


char get_char_from_symbol(uint8_t symb)
{
	if (symb == 2)
		return 'X';
	else if (symb == 1)
		return 'O';
	else
		return '-';
}

int sprint_board(char* buf, board_t* b)
{
	int count = 0;
	// count += sprintf(buf+count,"\n");
	for(int i = 0; i < 9; i++)
	{

		count += sprintf(buf + count,"%c",get_char_from_symbol(b->arr[i]));
		count += sprintf(buf+count," ");
		if (i % 3 == 2)
		{
			count += sprintf(buf+count,"\n");
		}
	}
	// count += sprintf(buf + count,"\n");
	return count;
}

void print_board(board_t* b)
{
	char buf[30];
	sprint_board(buf,b);
	printf("%s",buf);
	printf("key: %d\n\n", board_to_key(b));
}

bool boards_hard_equal(board_t a, board_t b)
{
	for (int i = 0; i < 9; i++)
	{
		if (a.arr[i] != b.arr[i])
			return false;
	}
	return true;
}

void board_transform_circular(board_t* from, board_t* to, int amount)
{
	for (int i = 0; i < 8; i++)
	{
		int indx = (i+amount) % 8;
		to->arr[IND_CIRCLE[indx]] = from->arr[IND_CIRCLE[i]];
	}
	to->arr[4] = from->arr[4];
}

void board_transform_flip_LR(board_t* from, board_t* to)
{
	for (int i = 0; i < 9; i++)
	{
		if (i%3==0)
			to->arr[i+2] = from->arr[i];
		else if (i%3==2)
			to->arr[i-2] = from->arr[i];
		else
			to->arr[i] = from->arr[i];
	}
}

void board_transform_flip_TB(board_t* from, board_t* to)
{
	for (int i = 0; i < 9; i++)
	{
		if (i/3==0)
			to->arr[6+(i%3)] = from->arr[i];
		else if (i/3==2)
			to->arr[i%3] = from->arr[i];
		else
			to->arr[i] = from->arr[i];
	}
}

void board_transform_generic(board_t* from, board_t* to, uint8_t tid)
{
	if (tid == ID_TRANS_NONE)
		for (int i = 0; i < 9; i++)
			to->arr[i] = from->arr[i];
	else if (tid == ID_TRANS_CLOCKWISE)
		board_transform_circular(from,to,2);
	else if (tid == ID_TRANS_180)
		board_transform_circular(from,to,4);
	else if (tid == ID_TRANS_COUNTERCLOCKWISE)
		board_transform_circular(from,to,6);
	else if (tid == ID_TRANS_FLIP_LR)
		board_transform_flip_LR(from,to);
	else if (tid == ID_TRANS_FLIP_TB)
		board_transform_flip_TB(from,to);
}


bool board_is_full(board_t* board)
{
	for (int i = 0; i < 9; i++)
		if (board->arr[i] == SYMBOL_E)
			return false;
	return true;
}

int board_to_key(board_t* board)
{
	int num = 0;
	for (int i = 0; i < 9; i++)
	{
		int mult = 0;
		if (board->arr[i] == SYMBOL_O)
			mult = 1;
		else if (board->arr[i] == SYMBOL_X)
			mult = 2;
		num = 3*num + mult;
	}
	return num + 1;
}

void board_fill_from_key(board_t* board, int key)
{
	for (int i = 0; i < 9; i++)
	{

	}
}

void board_fill_empty_moves(int key, uint8_t* movearr)
{

}

int main()
{
	board_t a;
	for (int i = 0; i < 9; i++)
		a.arr[i] = bbb[i];
	printf("Orig board:\n");
	print_board(&a);

	board_t to;
	for (int i = 0; i <= 5; i++)
	{
		board_transform_generic(&a,&to,i);
		print_board(&to);
	}

}